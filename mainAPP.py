import wx
import sqlite3
import database
from GUI import gui
import hashlib


#function to refresh data
def refresh_data():
    cnn=connect()
    cur=cnn.cursor()
    cur.execute("SELECT * FROM animals")
    rows=cur.fetchall()

    for i in range(0,len(rows)):
        for j in range(0,4):
            cell=rows[i]
            self.m_grid1.SetCellValue(i,j,str(cell[j]))

####_______________________________________________________________##
#function to create user account
conn=sqlite3.connect("database.db") #connect to database
cursor=conn.cursor()
###create users table
cursor.execute("""CREATE TABLE IF NOT EXIST users (username TEXT PRIMARY KEY, password TEXT)""")
###function definition
def create_account(username,password):
    hashed_password=hashlib.sha256(password.encode()).hexdigest() # Hash password
    #insert into database
    cursor.execute("INSERT INTO users VALUES(?,?)", (username,hashed_password))
    cursor.commit()
#get user input
username=input("enter username")
password=input("enter password")
#create account
create_account(username,password)
##_____________________________________________________________________##


###___________________________________________________________________##
#function to loging in
conn=sqlite3.connect("animals,db")
cursor=conn.cursor()

#define the function
def login(username,password):
    # retrieve user stored details
    cursor.execute("SELECT password FROM users WHERE username=?", (username))
    stored_hashed_password=cursor.fetchone()
    # hash input password
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    #verify password
    if stored_hashed_password and stored_hashed_password[0]== hashed_password:
        return True
    else:
        return False

#get user input
username=input("enter username")
password=input("enter password")
#login
if login(username,password):
    print("login successful")
else:
    print("invalid credentials")
#####_______________________________________________________________________________##
