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
        #if TheDatabase.login(self.username,self.password):
        #self.Hide()
        #home_frame = HomePageFrame(self)
        #return home_frame.Show()
        #else:
            #self.Hide()
            #sign_frame = SignUpFrame(self)
            #return sign_frame.Show()


    def create_user(self,event):
        self.Hide()
        sign_frame=SignUpFrame(self)
        return sign_frame.Show()


class SignUpFrame(gui.SignUp):
    def __init__(self, parent):
        gui.SignUp.__init__(self,parent)
        self.username = self.m_textCtrl3.GetValue()
        self.password = self.m_textCtrl4.GetValue()
        self.email = self.m_textCtrl5.GetValue()

    def create_account(self, event):
        self.Hide()
        home_frame = HomePageFrame(self)
        return home_frame.Show()

        #return TheDatabase.insert_user(self.username,self.password)

    def closeFunc(self, event):
        return self.Close()

class HomePageFrame(gui.HomePage):
    def __init__(self, parent):
        gui.HomePage.__init__(self,parent)


#function to refresh data


app=wx.App()
frame= LoginFrame(None)
frame.Show()
app.MainLoop()
