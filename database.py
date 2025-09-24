import sqlite3
import hashlib
print("Initializing Database")
class UserDatabase :
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        with sqlite3.connect(self.db_name, timeout=10) as conn:
            conn.execute('PRAGMA journal_mode=WAL;')  # Enable Write-Ahead Logging
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT
                )
            ''')
            conn.commit()
            


    def add_user(self, username, password, email=None):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            with sqlite3.connect(self.db_name, timeout=10) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                            INSERT INTO users (username, password, email)
                            VALUES (?, ?, ?)
                        ''', (username, hashed_password, email))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Username already exists
        except sqlite3.OperationalError as e:
            print(f"Database error: {e}")
            return False
                        
    def validate_user (self, username, password ):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name, timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                        SELECT * FROM users
                        WHERE username = ? AND password = ?
                    ''', (username, hashed_password))
            return cursor.fetchone() is not None

    def close(self):
        self.conn.close()
print("Database was created successfully!")