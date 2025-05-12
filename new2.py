import wx
import sqlite3
import datetime

# ----------------------------------------------------------------------
# Database Manager: Wraps SQLite3 operations and creates necessary tables.
# ----------------------------------------------------------------------
class DBManager:
    def __init__(self, db_name="livestock.db"):
        try:
            self.conn = sqlite3.connect(db_name)
        except Exception as e:
            wx.MessageBox("Database connection error: " + str(e), "Error", wx.ICON_ERROR)
        self.create_tables()

    def create_tables(self):
        try:
            cursor = self.conn.cursor()
            # Users table for login/registration.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT
                )
            """)
            # Inventory: summary of each animal type.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS livestock_inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    animal_type TEXT,
                    total_available INTEGER,
                    price REAL,
                    gender TEXT,
                    feed TEXT
                )
            """)
            # Details for each individual animal record.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS livestock_details (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    inventory_id INTEGER,
                    weight REAL,
                    health_status TEXT,
                    date_arrived TEXT,
                    feed_per_day TEXT,
                    age INTEGER,
                    status TEXT,
                    FOREIGN KEY(inventory_id) REFERENCES livestock_inventory(id)
                )
            """)
            self.conn.commit()
        except Exception as e:
            wx.MessageBox("Table creation error: " + str(e), "Error", wx.ICON_ERROR)

    # -----------------------------------------------------------
    # User Methods
    # -----------------------------------------------------------
    def add_user(self, username, password):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except Exception as e:
            wx.MessageBox("Error adding user: " + str(e), "Error", wx.ICON_ERROR)
            return False

    def check_user(self, username, password):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            result = cursor.fetchone()
            return result is not None
        except Exception as e:
            wx.MessageBox("Error checking user: " + str(e), "Error", wx.ICON_ERROR)
            return False

    # -----------------------------------------------------------
    # Inventory Methods (summary table)
    # -----------------------------------------------------------
    def add_inventory(self, animal_type, total_available, price, gender, feed):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO livestock_inventory (animal_type, total_available, price, gender, feed)
                VALUES (?, ?, ?, ?, ?)
            """, (animal_type, total_available, price, gender, feed))
            self.conn.commit()
            return True
        except Exception as e:
            wx.MessageBox("Error adding inventory: " + str(e), "Error", wx.ICON_ERROR)
            return False

    def get_inventory(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM livestock_inventory")
            return cursor.fetchall()
        except Exception as e:
            wx.MessageBox("Error fetching inventory: " + str(e), "Error", wx.ICON_ERROR)
            return []

    def update_inventory(self, inventory_id, animal_type, total_available, price, gender, feed):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE livestock_inventory 
                SET animal_type=?, total_available=?, price=?, gender=?, feed=?
                WHERE id=?
            """, (animal_type, total_available, price, gender, feed, inventory_id))
            self.conn.commit()
            return True
        except Exception as e:
            wx.MessageBox("Error updating inventory: " + str(e), "Error", wx.ICON_ERROR)
            return False

    def delete_inventory(self, inventory_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM livestock_inventory WHERE id=?", (inventory_id,))
            self.conn.commit()
            return True
        except Exception as e:
            wx.MessageBox("Error deleting inventory: " + str(e), "Error", wx.ICON_ERROR)
            return False

    # -----------------------------------------------------------
    # Livestock Detail Methods (individual records)
    # -----------------------------------------------------------
    def add_detail(self, inventory_id, weight, health_status, date_arrived, feed_per_day, age, status):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO livestock_details 
                (inventory_id, weight, health_status, date_arrived, feed_per_day, age, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (inventory_id, weight, health_status, date_arrived, feed_per_day, age, status))
            self.conn.commit()
            return True
        except Exception as e:
            wx.MessageBox("Error adding detail: " + str(e), "Error", wx.ICON_ERROR)
            return False

    def get_details(self, inventory_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM livestock_details WHERE inventory_id=?", (inventory_id,))
            return cursor.fetchall()
        except Exception as e:
            wx.MessageBox("Error fetching details: " + str(e), "Error", wx.ICON_ERROR)
            return []

    def update_detail(self, detail_id, weight, health_status, date_arrived, feed_per_day, age, status):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE livestock_details 
                SET weight=?, health_status=?, date_arrived=?, feed_per_day=?, age=?, status=?
                WHERE id=?
            """, (weight, health_status, date_arrived, feed_per_day, age, status, detail_id))
            self.conn.commit()
            return True
        except Exception as e:
            wx.MessageBox("Error updating detail: " + str(e), "Error", wx.ICON_ERROR)
            return False

    def delete_detail(self, detail_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM livestock_details WHERE id=?", (detail_id,))
            self.conn.commit()
            return True
        except Exception as e:
            wx.MessageBox("Error deleting detail: " + str(e), "Error", wx.ICON_ERROR)
            return False

    def close(self):
        if self.conn:
            self.conn.close()


# ----------------------------------------------------------------------
# LoginFrame: Allows user to login or click to register a new account.
# ----------------------------------------------------------------------
class LoginFrame(wx.Frame):
    def __init__(self, db_manager):
        wx.Frame.__init__(self, None, title="Login", size=(300, 250))
        self.db_manager = db_manager
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        st_username = wx.StaticText(panel, label="Username:")
        self.tc_username = wx.TextCtrl(panel)
        st_password = wx.StaticText(panel, label="Password:")
        self.tc_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        btn_login = wx.Button(panel, label="Login")
        btn_register = wx.Button(panel, label="Register")

        vbox.Add(st_username, flag=wx.ALL, border=5)
        vbox.Add(self.tc_username, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(st_password, flag=wx.ALL, border=5)
        vbox.Add(self.tc_password, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(btn_login, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(btn_register, flag=wx.ALL | wx.EXPAND, border=5)

        panel.SetSizer(vbox)
        btn_login.Bind(wx.EVT_BUTTON, self.on_login)
        btn_register.Bind(wx.EVT_BUTTON, self.on_register)

    def on_login(self, event):
        username = self.tc_username.GetValue().strip()
        password = self.tc_password.GetValue().strip()
        if not username or not password:
            wx.MessageBox("Please enter both username and password", "Error", wx.ICON_ERROR)
            return
        if self.db_manager.check_user(username, password):
            wx.MessageBox("Login successful.", "Info", wx.ICON_INFORMATION)
            self.Close()
            home = HomeFrame(self.db_manager)
            home.Show()
        else:
            wx.MessageBox("Invalid credentials", "Error", wx.ICON_ERROR)

    def on_register(self, event):
        reg = RegisterFrame(self.db_manager)
        reg.Show()


# ----------------------------------------------------------------------
# RegisterFrame: Allows new users to create an account.
# ----------------------------------------------------------------------
class RegisterFrame(wx.Frame):
    def __init__(self, db_manager):
        wx.Frame.__init__(self, None, title="Register", size=(300, 250))
        self.db_manager = db_manager
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        st_username = wx.StaticText(panel, label="New Username:")
        self.tc_username = wx.TextCtrl(panel)
        st_password = wx.StaticText(panel, label="New Password:")
        self.tc_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        btn_register = wx.Button(panel, label="Create Account")

        vbox.Add(st_username, flag=wx.ALL, border=5)
        vbox.Add(self.tc_username, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(st_password, flag=wx.ALL, border=5)
        vbox.Add(self.tc_password, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(btn_register, flag=wx.ALL | wx.EXPAND, border=5)

        panel.SetSizer(vbox)
        btn_register.Bind(wx.EVT_BUTTON, self.on_create_account)

    def on_create_account(self, event):
        username = self.tc_username.GetValue().strip()
        password = self.tc_password.GetValue().strip()
        if not username or not password:
            wx.MessageBox("Please enter username and password", "Error", wx.ICON_ERROR)
            return
        if self.db_manager.add_user(username, password):
            wx.MessageBox("Account created successfully. Please login.", "Info", wx.ICON_INFORMATION)
            self.Close()


# ----------------------------------------------------------------------
# HomeFrame: Main application page after login.
# Contains a search control, date/time display, and navigation buttons.
# ----------------------------------------------------------------------
class HomeFrame(wx.Frame):
    def __init__(self, db_manager):
        wx.Frame.__init__(self, None, title="Home", size=(600, 400))
        self.db_manager = db_manager
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Top panel contains a search field and a date/time display.
        top_panel = wx.Panel(panel)
        htop = wx.BoxSizer(wx.HORIZONTAL)
        self.search_ctrl = wx.SearchCtrl(top_panel, style=wx.TE_PROCESS_ENTER)
        self.date_time_txt = wx.StaticText(top_panel, label="")
        htop.Add(self.search_ctrl, proportion=1, flag=wx.ALL, border=5)
        htop.Add(self.date_time_txt, flag=wx.ALL, border=5)
        top_panel.SetSizer(htop)
        vbox.Add(top_panel, flag=wx.EXPAND)

        # Buttons for various modules.
        btnPanel = wx.Panel(panel)
        grid = wx.GridSizer(rows=2, cols=4, gap=(10, 10))
        btn_employees = wx.Button(btnPanel, label="Employees")
        btn_inventory = wx.Button(btnPanel, label="Inventory")
        btn_finances = wx.Button(btnPanel, label="Finances")
        btn_reports = wx.Button(btnPanel, label="Reports")
        btn_resources = wx.Button(btnPanel, label="Resources")
        btn_sales = wx.Button(btnPanel, label="Sales")
        btn_events = wx.Button(btnPanel, label="Events")
        btn_placeholder = wx.Button(btnPanel, label=" ")  # Filler

        grid.AddMany([
            (btn_employees, 0, wx.EXPAND),
            (btn_inventory, 0, wx.EXPAND),
            (btn_finances, 0, wx.EXPAND),
            (btn_reports, 0, wx.EXPAND),
            (btn_resources, 0, wx.EXPAND),
            (btn_sales, 0, wx.EXPAND),
            (btn_events, 0, wx.EXPAND),
            (btn_placeholder, 0, wx.EXPAND),
        ])
        btnPanel.SetSizer(grid)
        vbox.Add(btnPanel, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        # Bind navigation button events.
        btn_employees.Bind(wx.EVT_BUTTON, self.on_employees)
        btn_inventory.Bind(wx.EVT_BUTTON, self.on_inventory)
        btn_finances.Bind(wx.EVT_BUTTON, self.on_finances)
        btn_reports.Bind(wx.EVT_BUTTON, self.on_reports)
        btn_resources.Bind(wx.EVT_BUTTON, self.on_resources)
        btn_sales.Bind(wx.EVT_BUTTON, self.on_sales)
        btn_events.Bind(wx.EVT_BUTTON, self.on_events)

        # Timer for automatic date/time updates.
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_date_time, self.timer)
        self.timer.Start(1000)

    def update_date_time(self, event):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_time_txt.SetLabel(now)

    def on_employees(self, event):
        wx.MessageBox("Employees module under construction.", "Info", wx.ICON_INFORMATION)

    def on_inventory(self, event):
        inv_frame = InventoryFrame(self.db_manager)
        inv_frame.Show()

    def on_finances(self, event):
        wx.MessageBox("Finances module under construction.", "Info", wx.ICON_INFORMATION)

    def on_reports(self, event):
        wx.MessageBox("Reports module under construction.", "Info", wx.ICON_INFORMATION)

    def on_resources(self, event):
        wx.MessageBox("Resources module under construction.", "Info", wx.ICON_INFORMATION)

    def on_sales(self, event):
        wx.MessageBox("Sales module under construction.", "Info", wx.ICON_INFORMATION)

    def on_events(self, event):
        wx.MessageBox("Events module under construction.", "Info", wx.ICON_INFORMATION)


# ----------------------------------------------------------------------
# InventoryFrame: Displays the summary list of livestock inventory.
# Supports adding, editing, deleting, and viewing details.
# ----------------------------------------------------------------------
class InventoryFrame(wx.Frame):
    def __init__(self, db_manager):
        wx.Frame.__init__(self, None, title="Livestock Inventory", size=(700, 400))
        self.db_manager = db_manager
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        # ListCtrl to display inventory records.
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, "ID", width=50)
        self.list_ctrl.InsertColumn(1, "Animal Type", width=150)
        self.list_ctrl.InsertColumn(2, "Total Available", width=100)
        self.list_ctrl.InsertColumn(3, "Price", width=80)
        self.list_ctrl.InsertColumn(4, "Gender", width=80)
        self.list_ctrl.InsertColumn(5, "Feed", width=150)
        vbox.Add(self.list_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Button Panel for CRUD operations.
        btnPanel = wx.Panel(panel)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btnAdd = wx.Button(btnPanel, label="Add Inventory")
        btnEdit = wx.Button(btnPanel, label="Edit Inventory")
        btnDelete = wx.Button(btnPanel, label="Delete Inventory")
        btnViewDetails = wx.Button(btnPanel, label="View Details")
        btnRefresh = wx.Button(btnPanel, label="Refresh")
        hbox.Add(btnAdd, flag=wx.RIGHT, border=5)
        hbox.Add(btnEdit, flag=wx.RIGHT, border=5)
        hbox.Add(btnDelete, flag=wx.RIGHT, border=5)
        hbox.Add(btnViewDetails, flag=wx.RIGHT, border=5)
        hbox.Add(btnRefresh, flag=wx.RIGHT, border=5)
        btnPanel.SetSizer(hbox)
        vbox.Add(btnPanel, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        # Bind events.
        btnAdd.Bind(wx.EVT_BUTTON, self.on_add)
        btnEdit.Bind(wx.EVT_BUTTON, self.on_edit)
        btnDelete.Bind(wx.EVT_BUTTON, self.on_delete)
        btnViewDetails.Bind(wx.EVT_BUTTON, self.on_view_details)
        btnRefresh.Bind(wx.EVT_BUTTON, self.on_refresh)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_view_details)

        self.refresh_list()

    def refresh_list(self):
        self.list_ctrl.DeleteAllItems()
        inventory = self.db_manager.get_inventory()
        for item in inventory:
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), str(item[0]))
            self.list_ctrl.SetItem(index, 1, str(item[1]))
            self.list_ctrl.SetItem(index, 2, str(item[2]))
            self.list_ctrl.SetItem(index, 3, str(item[3]))
            self.list_ctrl.SetItem(index, 4, str(item[4]))
            self.list_ctrl.SetItem(index, 5, str(item[5]))

    def on_add(self, event):
        dlg = InventoryDialog()
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.get_data()
            if data:
                if self.db_manager.add_inventory(data["animal_type"],
                                                 data["total_available"],
                                                 data["price"],
                                                 data["gender"],
                                                 data["feed"]):
                    wx.MessageBox("Inventory added successfully.", "Info", wx.ICON_INFORMATION)
                    self.refresh_list()
        dlg.Destroy()

    def on_edit(self, event):
        idx = self.list_ctrl.GetFirstSelected()
        if idx == -1:
            wx.MessageBox("No inventory item selected.", "Warning", wx.ICON_WARNING)
            return
        inventory_id = int(self.list_ctrl.GetItemText(idx))
        data = {
            "animal_type": self.list_ctrl.GetItem(idx, 1).GetText(),
            "total_available": self.list_ctrl.GetItem(idx, 2).GetText(),
            "price": self.list_ctrl.GetItem(idx, 3).GetText(),
            "gender": self.list_ctrl.GetItem(idx, 4).GetText(),
            "feed": self.list_ctrl.GetItem(idx, 5).GetText()
        }
        dlg = InventoryDialog(data)
        if dlg.ShowModal() == wx.ID_OK:
            new_data = dlg.get_data()
            if new_data:
                if self.db_manager.update_inventory(inventory_id,
                                                    new_data["animal_type"],
                                                    new_data["total_available"],
                                                    new_data["price"],
                                                    new_data["gender"],
                                                    new_data["feed"]):
                    wx.MessageBox("Inventory updated successfully.", "Info", wx.ICON_INFORMATION)
                    self.refresh_list()
        dlg.Destroy()

    def on_delete(self, event):
        idx = self.list_ctrl.GetFirstSelected()
        if idx == -1:
            wx.MessageBox("No inventory item selected.", "Warning", wx.ICON_WARNING)
            return
        inventory_id = int(self.list_ctrl.GetItemText(idx))
        confirm = wx.MessageBox("Are you sure you want to delete this inventory item?",
                                "Confirm", wx.YES_NO | wx.ICON_QUESTION)
        if confirm == wx.YES:
            if self.db_manager.delete_inventory(inventory_id):
                wx.MessageBox("Inventory deleted.", "Info", wx.ICON_INFORMATION)
                self.refresh_list()

    def on_view_details(self, event):
        idx = self.list_ctrl.GetFirstSelected()
        if idx == -1:
            wx.MessageBox("No inventory item selected.", "Warning", wx.ICON_WARNING)
            return
        inventory_id = int(self.list_ctrl.GetItemText(idx))
        detail_frame = InventoryDetailFrame(self.db_manager, inventory_id)
        detail_frame.Show()

    def on_refresh(self, event):
        self.refresh_list()


# ----------------------------------------------------------------------
# InventoryDialog: Modal dialog to add or edit an inventory record.
# ----------------------------------------------------------------------
class InventoryDialog(wx.Dialog):
    def __init__(self, data=None):
        title = "Add Inventory" if data is None else "Edit Inventory"
        wx.Dialog.__init__(self, None, title=title, size=(350, 300))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Animal Type
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lblType = wx.StaticText(panel, label="Animal Type:")
        self.tcType = wx.TextCtrl(panel)
        hbox1.Add(lblType, flag=wx.RIGHT, border=8)
        hbox1.Add(self.tcType, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.ALL, border=10)

        # Total Available
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        lblTotal = wx.StaticText(panel, label="Total Available:")
        self.tcTotal = wx.TextCtrl(panel)
        hbox2.Add(lblTotal, flag=wx.RIGHT, border=8)
        hbox2.Add(self.tcTotal, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Price
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        lblPrice = wx.StaticText(panel, label="Price:")
        self.tcPrice = wx.TextCtrl(panel)
        hbox3.Add(lblPrice, flag=wx.RIGHT, border=8)
        hbox3.Add(self.tcPrice, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Gender
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        lblGender = wx.StaticText(panel, label="Gender:")
        self.tcGender = wx.TextCtrl(panel)
        hbox4.Add(lblGender, flag=wx.RIGHT, border=8)
        hbox4.Add(self.tcGender, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Feed
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        lblFeed = wx.StaticText(panel, label="Feed:")
        self.tcFeed = wx.TextCtrl(panel)
        hbox5.Add(lblFeed, flag=wx.RIGHT, border=8)
        hbox5.Add(self.tcFeed, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        # Buttons
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        btnOk = wx.Button(panel, id=wx.ID_OK, label="OK")
        btnCancel = wx.Button(panel, id=wx.ID_CANCEL, label="Cancel")
        hbox_buttons.Add(btnOk, flag=wx.RIGHT, border=10)
        hbox_buttons.Add(btnCancel)
        vbox.Add(hbox_buttons, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        if data:
            self.tcType.SetValue(data.get("animal_type", ""))
            self.tcTotal.SetValue(str(data.get("total_available", "")))
            self.tcPrice.SetValue(str(data.get("price", "")))
            self.tcGender.SetValue(data.get("gender", ""))
            self.tcFeed.SetValue(data.get("feed", ""))

    def get_data(self):
        animal_type = self.tcType.GetValue().strip()
        total_available = self.tcTotal.GetValue().strip()
        price = self.tcPrice.GetValue().strip()
        gender = self.tcGender.GetValue().strip()
        feed = self.tcFeed.GetValue().strip()

        if not animal_type or not total_available or not price:
            wx.MessageBox("Animal Type, Total and Price are required.", "Error", wx.ICON_ERROR)
            return None

        try:
            total_available = int(total_available)
        except ValueError:
            wx.MessageBox("Total Available must be an integer.", "Error", wx.ICON_ERROR)
            return None

        try:
            price = float(price)
        except ValueError:
            wx.MessageBox("Price must be a number.", "Error", wx.ICON_ERROR)
            return None

        return {
            "animal_type": animal_type,
            "total_available": total_available,
            "price": price,
            "gender": gender,
            "feed": feed
        }


# ----------------------------------------------------------------------
# InventoryDetailFrame: Display individual animal records for a given inventory item.
# Includes a computed "Days Lived" column based on the arrival date.
# ----------------------------------------------------------------------
class InventoryDetailFrame(wx.Frame):
    def __init__(self, db_manager, inventory_id):
        wx.Frame.__init__(self, None, title="Animal Details", size=(800, 400))
        self.db_manager = db_manager
        self.inventory_id = inventory_id
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # ListCtrl for details.
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, "ID", width=50)
        self.list_ctrl.InsertColumn(1, "Weight", width=100)
        self.list_ctrl.InsertColumn(2, "Health Status", width=120)
        self.list_ctrl.InsertColumn(3, "Date Arrived", width=120)
        self.list_ctrl.InsertColumn(4, "Feed per Day", width=100)
        self.list_ctrl.InsertColumn(5, "Age", width=80)
        self.list_ctrl.InsertColumn(6, "Status", width=100)
        self.list_ctrl.InsertColumn(7, "Days Lived", width=100)
        vbox.Add(self.list_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Button Panel for CRUD operations on details.
        btnPanel = wx.Panel(panel)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btnAdd = wx.Button(btnPanel, label="Add Detail")
        btnEdit = wx.Button(btnPanel, label="Edit Detail")
        btnDelete = wx.Button(btnPanel, label="Delete Detail")
        btnRefresh = wx.Button(btnPanel, label="Refresh")
        hbox.Add(btnAdd, flag=wx.RIGHT, border=5)
        hbox.Add(btnEdit, flag=wx.RIGHT, border=5)
        hbox.Add(btnDelete, flag=wx.RIGHT, border=5)
        hbox.Add(btnRefresh, flag=wx.RIGHT, border=5)
        btnPanel.SetSizer(hbox)
        vbox.Add(btnPanel, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        btnAdd.Bind(wx.EVT_BUTTON, self.on_add)
        btnEdit.Bind(wx.EVT_BUTTON, self.on_edit)
        btnDelete.Bind(wx.EVT_BUTTON, self.on_delete)
        btnRefresh.Bind(wx.EVT_BUTTON, self.on_refresh)

        self.refresh_list()

    def refresh_list(self):
        self.list_ctrl.DeleteAllItems()
        details = self.db_manager.get_details(self.inventory_id)
        for detail in details:
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), str(detail[0]))
            self.list_ctrl.SetItem(index, 1, str(detail[2]))  # weight
            self.list_ctrl.SetItem(index, 2, str(detail[3]))  # health_status
            self.list_ctrl.SetItem(index, 3, str(detail[4]))  # date_arrived
            self.list_ctrl.SetItem(index, 4, str(detail[5]))  # feed_per_day
            self.list_ctrl.SetItem(index, 5, str(detail[6]))  # age
            self.list_ctrl.SetItem(index, 6, str(detail[7]))  # status
            # Calculate days lived from date_arrived.
            days_lived = self.calculate_days_lived(detail[4])
            self.list_ctrl.SetItem(index, 7, str(days_lived))

    def calculate_days_lived(self, date_arrived):
        try:
            date_arrived_dt = datetime.datetime.strptime(date_arrived, "%Y-%m-%d")
            delta = datetime.datetime.now() - date_arrived_dt
            return delta.days
        except Exception:
            return "N/A"

    def on_add(self, event):
        dlg = DetailDialog()
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.get_data()
            if data:
                if self.db_manager.add_detail(self.inventory_id,
                                              data["weight"],
                                              data["health_status"],
                                              data["date_arrived"],
                                              data["feed_per_day"],
                                              data["age"],
                                              data["status"]):
                    wx.MessageBox("Detail added successfully.", "Info", wx.ICON_INFORMATION)
                    self.refresh_list()
        dlg.Destroy()

    def on_edit(self, event):
        idx = self.list_ctrl.GetFirstSelected()
        if idx == -1:
            wx.MessageBox("No detail selected.", "Warning", wx.ICON_WARNING)
            return
        detail_id = int(self.list_ctrl.GetItemText(idx))
        data = {
            "weight": self.list_ctrl.GetItem(idx, 1).GetText(),
            "health_status": self.list_ctrl.GetItem(idx, 2).GetText(),
            "date_arrived": self.list_ctrl.GetItem(idx, 3).GetText(),
            "feed_per_day": self.list_ctrl.GetItem(idx, 4).GetText(),
            "age": self.list_ctrl.GetItem(idx, 5).GetText(),
            "status": self.list_ctrl.GetItem(idx, 6).GetText()
        }
        dlg = DetailDialog(data)
        if dlg.ShowModal() == wx.ID_OK:
            new_data = dlg.get_data()
            if new_data:
                if self.db_manager.update_detail(detail_id,
                                                 new_data["weight"],
                                                 new_data["health_status"],
                                                 new_data["date_arrived"],
                                                 new_data["feed_per_day"],
                                                 new_data["age"],
                                                 new_data["status"]):
                    wx.MessageBox("Detail updated successfully.", "Info", wx.ICON_INFORMATION)
                    self.refresh_list()
        dlg.Destroy()

    def on_delete(self, event):
        idx = self.list_ctrl.GetFirstSelected()
        if idx == -1:
            wx.MessageBox("No detail selected.", "Warning", wx.ICON_WARNING)
            return
        detail_id = int(self.list_ctrl.GetItemText(idx))
        confirm = wx.MessageBox("Are you sure you want to delete this detail?",
                                "Confirm", wx.YES_NO | wx.ICON_QUESTION)
        if confirm == wx.YES:
            if self.db_manager.delete_detail(detail_id):
                wx.MessageBox("Detail deleted.", "Info", wx.ICON_INFORMATION)
                self.refresh_list()

    def on_refresh(self, event):
        self.refresh_list()


# ----------------------------------------------------------------------
# DetailDialog: Modal dialog to add or edit a livestock detail record.
# ----------------------------------------------------------------------
class DetailDialog(wx.Dialog):
    def __init__(self, data=None):
        title = "Add Detail" if data is None else "Edit Detail"
        wx.Dialog.__init__(self, None, title=title, size=(350, 400))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Weight
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lblWeight = wx.StaticText(panel, label="Weight:")
        self.tcWeight = wx.TextCtrl(panel)
        hbox1.Add(lblWeight, flag=wx.RIGHT, border=8)
        hbox1.Add(self.tcWeight, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.ALL, border=10)

        # Health Status
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        lblHealth = wx.StaticText(panel, label="Health Status:")
        self.tcHealth = wx.TextCtrl(panel)
        hbox2.Add(lblHealth, flag=wx.RIGHT, border=8)
        hbox2.Add(self.tcHealth, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.ALL, border=10)

        # Date Arrived
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        lblDate = wx.StaticText(panel, label="Date Arrived (YYYY-MM-DD):")
        self.tcDate = wx.TextCtrl(panel)
        hbox3.Add(lblDate, flag=wx.RIGHT, border=8)
        hbox3.Add(self.tcDate, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.ALL, border=10)

        # Feed per Day
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        lblFeed = wx.StaticText(panel, label="Feed per Day:")
        self.tcFeed = wx.TextCtrl(panel)
        hbox4.Add(lblFeed, flag=wx.RIGHT, border=8)
        hbox4.Add(self.tcFeed, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.ALL, border=10)

        # Age
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        lblAge = wx.StaticText(panel, label="Age:")
        self.tcAge = wx.TextCtrl(panel)
        hbox5.Add(lblAge, flag=wx.RIGHT, border=8)
        hbox5.Add(self.tcAge, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.ALL, border=10)

        # Status (in stock or sold)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        lblStatus = wx.StaticText(panel, label="Status (in stock/sold):")
        self.tcStatus = wx.TextCtrl(panel)
        hbox6.Add(lblStatus, flag=wx.RIGHT, border=8)
        hbox6.Add(self.tcStatus, proportion=1)
        vbox.Add(hbox6, flag=wx.EXPAND | wx.ALL, border=10)

        # Buttons
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        btnOk = wx.Button(panel, id=wx.ID_OK)


if __name__ == "__main__":
    # Create a wx.App instance.
    app = wx.App(False)

    # Create the database manager instance.
    db = DBManager()

    # Create and show the first frame (LoginFrame in our case).
    login_frame = LoginFrame(db)
    login_frame.Show()

    # Start the wxPython event loop.
    app.MainLoop()
