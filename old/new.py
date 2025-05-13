import wx
import sqlite3


# -----------------------------------------------------------
# Database Manager: handles all SQLite operations.
# -----------------------------------------------------------
class DBManager:
    def __init__(self, db_name="inventory.db"):
        self.db_name = db_name
        self.conn = None
        self.connect_db()

    def connect_db(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.create_table()
        except sqlite3.Error as e:
            wx.MessageBox(f"Database connection error: {e}", "Error", wx.ICON_ERROR)

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            # The 'item_name' field is unique so that duplicate names (items) are not allowed.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT NOT NULL UNIQUE,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    description TEXT
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error creating table: {e}", "Error", wx.ICON_ERROR)

    def add_item(self, item_name, quantity, price, description):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO inventory (item_name, quantity, price, description)
                VALUES (?, ?, ?, ?)
            """, (item_name, quantity, price, description))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            wx.MessageBox("Item already exists. Please use a unique name.", "Warning", wx.ICON_WARNING)
            return False
        except sqlite3.Error as e:
            wx.MessageBox(f"Error adding item: {e}", "Error", wx.ICON_ERROR)
            return False

    def get_items(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, item_name, quantity, price, description FROM inventory")
            return cursor.fetchall()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error fetching items: {e}", "Error", wx.ICON_ERROR)
            return []

    def update_item(self, item_id, item_name, quantity, price, description):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE inventory 
                SET item_name = ?, quantity = ?, price = ?, description = ?
                WHERE id = ?
            """, (item_name, quantity, price, description, item_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            wx.MessageBox(f"Error updating item: {e}", "Error", wx.ICON_ERROR)
            return False

    def delete_item(self, item_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            wx.MessageBox(f"Error deleting item: {e}", "Error", wx.ICON_ERROR)
            return False

    def close(self):
        if self.conn:
            self.conn.close()


# -----------------------------------------------------------
# InventoryDialog: a dialog for adding or editing an inventory item.
# -----------------------------------------------------------
class InventoryDialog(wx.Dialog):
    def __init__(self, parent, title="Add Item", item_data=None):
        super().__init__(parent, title=title, size=(350, 300))
        panel = wx.Panel(self)

        self.item_data = item_data

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Item Name Row
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lblName = wx.StaticText(panel, label="Item Name:")
        hbox1.Add(lblName, flag=wx.RIGHT, border=8)
        self.txtName = wx.TextCtrl(panel)
        hbox1.Add(self.txtName, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.ALL, border=10)

        # Quantity Row
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        lblQty = wx.StaticText(panel, label="Quantity:")
        hbox2.Add(lblQty, flag=wx.RIGHT, border=25)
        self.txtQty = wx.TextCtrl(panel)
        hbox2.Add(self.txtQty, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Price Row
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        lblPrice = wx.StaticText(panel, label="Price:")
        hbox3.Add(lblPrice, flag=wx.RIGHT, border=30)
        self.txtPrice = wx.TextCtrl(panel)
        hbox3.Add(self.txtPrice, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Description Row
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        lblDesc = wx.StaticText(panel, label="Description:")
        hbox4.Add(lblDesc, flag=wx.RIGHT, border=5)
        self.txtDesc = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox4.Add(self.txtDesc, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.ALL, border=10)

        # Buttons Row
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btnOk = wx.Button(panel, label="OK", id=wx.ID_OK)
        btnCancel = wx.Button(panel, label="Cancel", id=wx.ID_CANCEL)
        hbox5.Add(btnOk)
        hbox5.Add(btnCancel, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        # If editing an existing item, pre-fill the fields.
        if self.item_data:
            self.txtName.SetValue(self.item_data.get("item_name", ""))
            self.txtQty.SetValue(str(self.item_data.get("quantity", "")))
            self.txtPrice.SetValue(str(self.item_data.get("price", "")))
            self.txtDesc.SetValue(self.item_data.get("description", ""))

    def get_data(self):
        item_name = self.txtName.GetValue().strip()
        qty_str = self.txtQty.GetValue().strip()
        price_str = self.txtPrice.GetValue().strip()
        description = self.txtDesc.GetValue().strip()

        # Basic validation for input fields.
        if not item_name:
            wx.MessageBox("Item Name cannot be empty.", "Error", wx.ICON_ERROR)
            return None

        try:
            quantity = int(qty_str)
        except ValueError:
            wx.MessageBox("Quantity must be an integer.", "Error", wx.ICON_ERROR)
            return None

        try:
            price = float(price_str)
        except ValueError:
            wx.MessageBox("Price must be a number.", "Error", wx.ICON_ERROR)
            return None

        return {
            "item_name": item_name,
            "quantity": quantity,
            "price": price,
            "description": description
        }


# -----------------------------------------------------------
# MainFrame: the primary window where inventory items are listed.
# -----------------------------------------------------------
class MainFrame(wx.Frame):
    def __init__(self, parent, title="Inventory Control System"):
        super().__init__(parent, title=title, size=(600, 400))
        self.db_manager = DBManager()
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # ListCtrl for displaying inventory items.
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, "ID", width=50)
        self.list_ctrl.InsertColumn(1, "Item Name", width=150)
        self.list_ctrl.InsertColumn(2, "Quantity", width=80)
        self.list_ctrl.InsertColumn(3, "Price", width=80)
        self.list_ctrl.InsertColumn(4, "Description", width=200)
        vbox.Add(self.list_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Button panel for CRUD operations.
        btnPanel = wx.Panel(panel)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btnAdd = wx.Button(btnPanel, label="Add Item")
        btnEdit = wx.Button(btnPanel, label="Edit Item")
        btnDelete = wx.Button(btnPanel, label="Delete Item")
        btnRefresh = wx.Button(btnPanel, label="Refresh")
        hbox.Add(btnAdd, flag=wx.RIGHT, border=5)
        hbox.Add(btnEdit, flag=wx.RIGHT, border=5)
        hbox.Add(btnDelete, flag=wx.RIGHT, border=5)
        hbox.Add(btnRefresh)
        btnPanel.SetSizer(hbox)
        vbox.Add(btnPanel, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        # Bind button events.
        btnAdd.Bind(wx.EVT_BUTTON, self.on_add)
        btnEdit.Bind(wx.EVT_BUTTON, self.on_edit)
        btnDelete.Bind(wx.EVT_BUTTON, self.on_delete)
        btnRefresh.Bind(wx.EVT_BUTTON, self.on_refresh)
        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.refresh_list()

    def refresh_list(self):
        """Refresh the ListCtrl with the latest data from the database."""
        self.list_ctrl.DeleteAllItems()
        items = self.db_manager.get_items()
        for item in items:
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), str(item[0]))
            self.list_ctrl.SetItem(index, 1, item[1])
            self.list_ctrl.SetItem(index, 2, str(item[2]))
            self.list_ctrl.SetItem(index, 3, str(item[3]))
            self.list_ctrl.SetItem(index, 4, item[4] if item[4] else "")

    def on_add(self, event):
        """Handle the Add Item event."""
        dialog = InventoryDialog(self, title="Add Inventory Item")
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.get_data()
            if data:
                if self.db_manager.add_item(data["item_name"], data["quantity"], data["price"], data["description"]):
                    wx.MessageBox("Item added successfully.", "Info", wx.ICON_INFORMATION)
                    self.refresh_list()
        dialog.Destroy()

    def on_edit(self, event):
        """Handle the Edit Item event."""
        selected_item = self.list_ctrl.GetFirstSelected()
        if selected_item == -1:
            wx.MessageBox("No item selected for editing.", "Warning", wx.ICON_WARNING)
            return

        # Retrieve item details from the selected row.
        try:
            item_id = int(self.list_ctrl.GetItemText(selected_item))
        except ValueError:
            wx.MessageBox("Invalid item ID.", "Error", wx.ICON_ERROR)
            return

        item_data = {
            "id": item_id,
            "item_name": self.list_ctrl.GetItem(selected_item, 1).GetText(),
            "quantity": int(self.list_ctrl.GetItem(selected_item, 2).GetText()),
            "price": float(self.list_ctrl.GetItem(selected_item, 3).GetText()),
            "description": self.list_ctrl.GetItem(selected_item, 4).GetText()
        }

        dialog = InventoryDialog(self, title="Edit Inventory Item", item_data=item_data)
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.get_data()
            if data:
                if self.db_manager.update_item(item_id, data["item_name"], data["quantity"], data["price"],
                                               data["description"]):
                    wx.MessageBox("Item updated successfully.", "Info", wx.ICON_INFORMATION)
                    self.refresh_list()
        dialog.Destroy()

    def on_delete(self, event):
        """Handle the Delete Item event."""
        selected_item = self.list_ctrl.GetFirstSelected()
        if selected_item == -1:
            wx.MessageBox("No item selected for deletion.", "Warning", wx.ICON_WARNING)
            return

        try:
            item_id = int(self.list_ctrl.GetItemText(selected_item))
        except ValueError:
            wx.MessageBox("Invalid item ID.", "Error", wx.ICON_ERROR)
            return

        confirm = wx.MessageBox("Are you sure you want to delete this item?",
                                "Confirm Deletion", wx.YES_NO | wx.ICON_QUESTION)
        if confirm == wx.YES:
            if self.db_manager.delete_item(item_id):
                wx.MessageBox("Item deleted successfully.", "Info", wx.ICON_INFORMATION)
                self.refresh_list()

    def on_refresh(self, event):
        """Handler for the Refresh button."""
        self.refresh_list()

    def on_close(self, event):
        """Ensure the database connection is closed on exit."""
        self.db_manager.close()
        self.Destroy()


# -----------------------------------------------------------
# Application Entry Point
# -----------------------------------------------------------
class InventoryApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, title="Inventory Control System")
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = InventoryApp()
    app.MainLoop()
