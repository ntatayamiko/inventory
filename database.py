import sqlite3
import wx


def create_table() -> None:
    conn = sqlite3.connect('animals.db')
    a = conn.cursor()

    # Creating the table
    a.execute("""
                    CREATE TABLE IF NOT EXISTS user_accounts (
                        username TEXT UNIQUE,
                        hashed_password TEXT UNIQUE
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





