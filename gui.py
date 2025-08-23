# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Welcome
###########################################################################

class Welcome ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.username = wx.StaticText( self, wx.ID_ANY, u"USERNAME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )
		gSizer1.Add( self.username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.name_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.name_textCtrl3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.password = wx.StaticText( self, wx.ID_ANY, u"PASSWORD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )
		gSizer1.Add( self.password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.password_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.password_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.email = wx.StaticText( self, wx.ID_ANY, u"EMAIL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		gSizer1.Add( self.email, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.email_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.email_textCtrl5, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.login = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer1.Add( self.login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.signIn = wx.Button( self, wx.ID_ANY, u"SIGN IN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.signIn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer1.Add( self.signIn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.login )
		self.signIn.Bind( wx.EVT_BUTTON, self.sign_in_panel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def login( self, event ):
		event.Skip()
	
	def sign_in_panel( self, event ):
		event.Skip()
	

###########################################################################
## Class SignInPanel
###########################################################################

class SignInPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.username = wx.StaticText( self, wx.ID_ANY, u"USERNAME :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )
		gSizer2.Add( self.username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.username_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.username_textCtrl6, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.password = wx.StaticText( self, wx.ID_ANY, u"PASSWORD :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )
		gSizer2.Add( self.password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.password_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.password_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.email = wx.StaticText( self, wx.ID_ANY, u"EMAIL :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		gSizer2.Add( self.email, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.email_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.email_textCtrl8, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.sign_in_panel = wx.Button( self, wx.ID_ANY, u"Sign-in", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sign_in_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer2.Add( self.sign_in_panel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		# Connect Events
		self.sign_in_panel.Bind( wx.EVT_BUTTON, self.sign_in )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sign_in( self, event ):
		event.Skip()
	

