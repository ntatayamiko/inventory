import wx
import gui
import database

class MainFrame(gui.Welcome):
    def __init__(self,parent):
        super().__init__(parent)
        self.panels = {"main":self.m_panel1, "signup":self.signup_panel2, "login":self.login_panel21, "home":self.main_panel}

    def switchPanel(self,panel_name):
        for panel in self.panels.values():
            panel.Hide()
        #show the requested panel
        self.panels[panel_name].Show()
        #tell the sizer to recalculate the layout
        self.Layout()

    def home_panel(self,event):
        self.switchPanel("home")

    def login_panel(self, event):
        self.switchPanel("login")

    def signup_panel(self, event):
        self.switchPanel("signup")

    def create_account(self, event):
        username = self.username_textCtrl1.GetValue()
        password = self.password_textCtrl3.GetValue()
        email = self.m_textCtrl2.GetValue()

        db = database.UserDatabase()
        if db.add_user(username, password, email):
            # clear fields
            self.username_textCtrl1.SetValue("")
            self.password_textCtrl3.SetValue("")
            self.m_textCtrl2.SetValue("")
            # switch to log in panel
            self.login_panel(event)

    def loginUser(self, event):
        username = self.username_textCtrl11.GetValue()
        password = self.password_textCtrl31.GetValue()

        if not username or not password:
            return
        db = database.UserDatabase()
        if db.validate_user(username, password):
            # open the main application window
            wx.MessageBox(f"welcome, {username}!", "Login success", wx.OK | wx.ICON_INFORMATION)
            self.home_panel(event)
        else:
            wx.MessageBox(f"invalid, create account!", "login unsuccessful", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()