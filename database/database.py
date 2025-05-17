import sqlite3
import wx
import mainAPP


def create_table():
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()

    # Creating the table
    a.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT UNIQUE
                    )
                """)
    a.execute('''
        CREATE TABLE inventory (
            inv_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            weight INTEGER DEFAULT 0,
            age INTEGER DEFAULT 0,
            date_purchased INTEGER DEFAULT 0,
            status TEXT NOT NULL,
            purchase_price INTEGER DEFAULT 0,
            market_value INTEGER DEFAULT 0,
            quantity INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()


#adding the items
def add_inv(inv_id, name, weight, age, date_purchased,status,purchase_price,market_value, quantity):
        conn = sqlite3.connect('animals.db')
        a = conn.cursor()

        try:
            a.execute("INSERT INTO inventory (inv_id, name, weight, age, date_purchased,status,purchase_price,market_value, quantity)"
                      " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (inv_id, name, weight, age, date_purchased,status,purchase_price,market_value, quantity))
            conn.commit()
            print(f"Added inventory: {name} with id: {inv_id}")
        except sqlite3.IntegrityError:
            print("This inventory ID already exists. Try a different one.")

        conn.close()

add_inv(1, "cow", 300, 5, 10,"alive",300,700,60)
add_inv(2, "pig", 420, 4, 55,"sick",250,600,4)
add_inv(3, "goat", 350, 600.0, 399,"active",250,600,4)
add_inv(4, "chickens", 200, 590.0, 5,"ready",250,600,4)


#create_table()

def view_inventory():
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()

    # Query all animals from the database
    a.execute("SELECT * FROM inventory") #we are selecting from the table
    inventory = a.fetchall() #this is getting all entries

    # Displaying the books using if-else condition statements
    if inventory:
        print("\n--- All animals in Inventory ---")
        for animl in inventory:
            print(f"inv_id: {animl[0]} | name: {animl[1]} | weight: {animl[2]} | age: {animl[3]} | date_purchased: {animl[4]}| status: {animl[5]} | purchase_price: {animl[6]} | market_value: {animl[7]} | Quantity: {animl[8]}")
    else:
        print("No animals found in the inventory.")

    conn.close()

view_inventory() # This function displays all the inventory in the database

def search_inventory_by_name(name):
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()
    a.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + name + '%',))
    inventory = a.fetchall()
    conn.close()
    return inventory

def search_inventory_by_status(status):
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()
    a.execute("SELECT * FROM inventory WHERE status LIKE ?", ('%' + status + '%',))
    inventory = a.fetchall()
    conn.close()
    return inventory


#updating animal details
def update_inv_details(inv_id,new_name=None, new_weight=None, new_age=None, new_date_purchased=None, new_status=None, new_purchase_price=None, new_market_value=None, new_quantity=None):
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()

    # Build a dynamic update query
    if new_name:
        a.execute("UPDATE inventory SET name = ? WHERE inv_id = ?", (new_name, inv_id))
    if new_weight:
        a.execute("UPDATE inventory SET weight = ? WHERE inv_id = ?", (new_weight, inv_id))
    if new_age:
        a.execute("UPDATE inventory SET age = ? WHERE inv_id = ?", (new_age, inv_id))
    if new_date_purchased:
        a.execute("UPDATE inventory SET date_purchased = ? WHERE inv_id = ?", (new_date_purchased, inv_id))
    if new_status:
        a.execute("UPDATE inventory SET status = ? WHERE inv_id = ?", (new_status, inv_id))
    if new_purchase_price:
        a.execute("UPDATE inventory SET purchase_price = ? WHERE inv_id = ?", (new_purchase_price, inv_id))
    if new_market_value:
        a.execute("UPDATE inventory SET market_value = ? WHERE inv_id = ?", (new_market_value, inv_id))
    if new_quantity:
        a.execute("UPDATE inventory SET quantity = ? WHERE inv_id = ?", (new_quantity, inv_id))

    conn.commit()
    print(f"animal ID {inv_id} updated successfully.")
    conn.close()

update_inv_details(2, new_name="goat", new_weight=450.0,new_age=7, new_date_purchased=30, new_status="ready", new_purchase_price=450, new_market_value=650, new_quantity=7)

# Getting an inventory by its title
def get_inventory_by_name(name):
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()

    a.execute("SELECT * FROM inventory WHERE name = ?", (name,))
    inventory = a.fetchone()

    if inventory:
        print(f"Found inventory:\n inv_id: {inventory[0]} | name: {inventory[1]} | weight: {inventory[2]} | age: {inventory[3]} | date_purchased: {inventory[4]}| status: {inventory[5]} | purchase_price: {inventory[6]} | market_value: {inventory[7]} | Quantity: {inventory[8]}")
    else:
        print(f"\nNo inventory found with name '{name}'.")

    conn.close()
#get_inventory_by_name()

#deleting entries
def delete_inventory(inv_id):
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()

    a.execute("DELETE FROM inventory WHERE inv_id = ?", (inv_id,))
    conn.commit()

    if a.rowcount > 0:
        print(f"inventory ID {inv_id} has been deleted.")
    else:
        print(f"No inventory found with ID {inv_id}.")

    conn.close()
#delete_inv(4)
view_inventory()
add_inv(2, "cow", 300, 5, 10,"alive",300,700,60)
view_inventory()
delete_inventory(1)
view_inventory()
get_inventory_by_name("goat")
update_inv_details(3, "cow", 300, 5, 10,"alive",300,700,60)
view_inventory()
add_inv(8, "cow", 300, 5, 10,"alive",300,700,60)
view_inventory()
add_inv(7, "cow", 300, 5, 10,"alive",300,700,60)
view_inventory()


