import sqlite3


#### the main database class#####
class TheDatabase:
    def __init__(self, db_name="animals.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

################################################################
    def create_inventory_table(self):
        self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS inventory (
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
        self.conn.commit()
        self.conn.close()

#####################################################################
    def create_user_table(self):
        # Creating the table
        self.conn.execute("""
                        CREATE TABLE IF NOT EXISTS user_accounts (
                            username TEXT UNIQUE,
                            hashed_password TEXT UNIQUE
                        )
                    """)
        self.conn.commit()
        self.conn.close()

########################################################
    def insert_user(self,username,password):
        hashed_password = sha256(password.encode()).hexdigest()  # hashing user input password
        self.conn.execute('''INSERT INTO user_accounts (username,hashed_password)  VALUES(?,?)''',
                  (username, hashed_password))  # storing into database
        self.conn.commit()
        self.conn.close()

###################################################
    def insert_employee(self,):
        self.conn.execute(
            """INSERT INTO TABLE employees VALUES(?,?)""", (username, password)
        )
        self.conn.commit()
        self.conn.close()

###################################
    def add_inv(self,inv_id, name, weight, age, date_purchased, status, purchase_price, market_value, quantity):
        try:
            self.conn.execute(
                "INSERT INTO inventory (inv_id, name, weight, age, date_purchased,status,purchase_price,market_value, quantity)"
                " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (inv_id, name, weight, age, date_purchased, status, purchase_price, market_value, quantity))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("This inventory ID already exists. Try a different one.")

        conn.close()

###########################################
    def search_inventory_by_name(self,name):
        self.conn.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + name + '%',))
        inventory = self.conn.fetchall()
        self.conn.close()
        return inventory

###############################################
    def update_inv_details(self,inv_id, new_name=None, new_weight=None, new_age=None, new_date_purchased=None,
                           new_status=None, new_purchase_price=None, new_market_value=None, new_quantity=None):

        # Build a dynamic update query
        if new_name:
            self.conn.execute("UPDATE inventory SET name = ? WHERE inv_id = ?", (new_name, inv_id))
        if new_weight:
            self.conn.execute("UPDATE inventory SET weight = ? WHERE inv_id = ?", (new_weight, inv_id))
        if new_age:
            self.conn.execute("UPDATE inventory SET age = ? WHERE inv_id = ?", (new_age, inv_id))
        if new_date_purchased:
            self.conn.execute("UPDATE inventory SET date_purchased = ? WHERE inv_id = ?", (new_date_purchased, inv_id))
        if new_status:
            self.conn.execute("UPDATE inventory SET status = ? WHERE inv_id = ?", (new_status, inv_id))
        if new_purchase_price:
            self.conn.execute("UPDATE inventory SET purchase_price = ? WHERE inv_id = ?", (new_purchase_price, inv_id))
        if new_market_value:
            self.conn.execute("UPDATE inventory SET market_value = ? WHERE inv_id = ?", (new_market_value, inv_id))
        if new_quantity:
            self.conn.execute("UPDATE inventory SET quantity = ? WHERE inv_id = ?", (new_quantity, inv_id))

        self.conn.commit()
        print(f"animal ID {inv_id} updated successfully.")
        self.conn.close()

#################################################################
    def delete_inventory(self,inv_id):

        self.conn.execute("DELETE FROM inventory WHERE inv_id = ?", (inv_id,))
        self.conn.commit()

        if self.conn.rowcount > 0:
            print(f"inventory ID {inv_id} has been deleted.")
        else:
            print(f"No inventory found with ID {inv_id}.")

        self.conn.close()

######################################################
    def view_inventory(self):
        # Query all animals from the database
        self.conn.execute("SELECT * FROM inventory")  # we are selecting from the table
        inventory = self.conn.fetchall()  # this is getting all entries

        # Displaying the books using if-else condition statements
        if inventory:
            print("\n--- All animals in Inventory ---")
            for animl in inventory:
                print(
                    f"inv_id: {animl[0]} | name: {animl[1]} | weight: {animl[2]} | age: {animl[3]} | date_purchased: {animl[4]}| status: {animl[5]} | purchase_price: {animl[6]} | market_value: {animl[7]} | Quantity: {animl[8]}")
        else:
            print("No animals found in the inventory.")

        self.conn.close()

    def login(self):
        self.conn.execute("SELECT FROM user_accounts WHERE username=?", (self.username,))
        database_hashed_password = cursor.fetchone()  # retrieving from database

        hashed_input_password = sha256(self.password.encode()).hexdigest()  # hashing input password to verify
        if database_hashed_password == hashed_input_password:
            return True
        else:
            return False

print("table created")




