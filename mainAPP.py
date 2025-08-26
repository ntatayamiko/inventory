import wx
import gui
import database

class SignIn (SignInPanel):
    def __init__(self):
        super().__init__(parent)

    def sign_in(self, event):
        username = self.username_textCtrl6.GetValue()
        password = self.password_textCtrl7.GetValue()
        email = self.email_textCtrl8.GetValue()

        if not username or not password:
            self.signup_status.SetLabel("username and password are required")
            return

        if len(password) < 6:
            self.signup_status.SetLabel("password must be at least 6 characters")
            return

        if self.db.add_user(username,password,email):
            self.signup_status.SetLabel("account created successfully")
            #clear fields
            self.username_textCtrl6.SetValue("")
            self.password_textCtrl7.SetValue("")
            self.email_textCtrl8.SetValue("")
            #switch to log in panel
            self.panel.SetSelection(0)
        else:
            self.signup_status.SetLabel("Username already exists")