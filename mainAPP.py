import wx
import wx.xrc
#import wx.calendar
import wx.grid
import wx.dataview
import sqlite3
from database import TheDatabase
import gui
from hashlib import sha256


class LoginFrame(gui.LoginPage):


    def __init__(self, parent):
        gui.LoginPage.__init__(self,parent)
        self.username = self.m_textCtrl1.GetValue()
        self.password = self.m_textCtrl2.GetValue()


    #overriding definitions from class login page
    def user_login(self,event):
        return TheDatabase.login(self.username,self.password)


    def create_user(self,event):
        return SignUpFrame(None)


class SignUpFrame(gui.SignUp):
    def __init__(self, parent):
        gui.SignUp.__init__(self,parent)
        self.username = self.m_textCtrl3.GetValue()
        self.password = self.m_textCtrl4.GetValue()
        self.email = self.m_textCtrl5.GetValue()

    def create_account(self, event):
        return TheDatabase.insert_user(self.username,self.password)

    def closeFunc(self, event):
        return self.Close()



#function to refresh data
def refresh_data():
    cnn=sqlite3.connect("animals.db")
    cur=cnn.cursor()
    cur.execute("SELECT * FROM animals")
    rows=cur.fetchall()

    for i in range(0,len(rows)):
        for j in range(0,4):
            cell=rows[i]
            self.m_grid1.SetCellValue(i,j,str(cell[j]))

app=wx.App()
frame= SignUpFrame(None)
frame.Show()
app.MainLoop()
