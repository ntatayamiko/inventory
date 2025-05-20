import wx
import sqlite3
import database
import gui
from hashlib import sha256


class LoginFrame(gui.LoginPage):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.username = self.m_textCtrl1.GetValue()
        self.password = self.m_textCtrl2.GetValue()


    #overriding definitions from class login page
    def user_login(self,username,password):
        database.create_table()
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        cursor.execute("SELECT FROM user_accounts WHERE username=?",(username,))
        database_hashed_password= cursor.fetchone() #retrieving from database
        
        hashed_input_password= sha256(password.encode()).hexdigest() #hashing input password to verify
        if database_hashed_password and database_hashed_password[0]== hashed_password:
            return True
        else:
            return False

    user_login(self.username,self.password)

    def create_user(self, event,username,password):
        database.create_table()
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        hashed_password= sha256(password.encode()).hexdigest() #hashing user input password
        cursor.execute("INSERT INTO user_accounts VALUES(?,?)",(username,hashed_password)) #storing into database
        conn.commit()
        self.user_login()

    create_user()

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

app=wx.App()
frame= LoginFrame()
frame.Show()
app.MainLoop()
