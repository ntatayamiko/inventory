import sqlite3
import hashlib

class UserDatabase :
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, username UNIQUE NOT NULL, password TEXT NOT NULL, email TEXT ) ''')
        self.conn.commit()

    def add_user(self, username, password, email=None):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute('''INSERT INTO users (username, password,email) VALUES (?,?,?) ''',(username, hashed_password, email))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False #username already exist
                        
    def validate_user (self, username, password ):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute(''' SELECT FROM users WHERE username =? AND password = ? ''', (username, hashed_password))
        return self.cursor.fetchone() is not None

    def close(self):
        self.conn.close()