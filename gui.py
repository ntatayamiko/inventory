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
		
		self.Username = wx.StaticText( self, wx.ID_ANY, u"USERNAME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Username.Wrap( -1 )
		gSizer1.Add( self.Username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.Password = wx.StaticText( self, wx.ID_ANY, u"PASSWORD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Password.Wrap( -1 )
		gSizer1.Add( self.Password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Email = wx.StaticText( self, wx.ID_ANY, u"EMAIL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Email.Wrap( -1 )
		gSizer1.Add( self.Email, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.Login = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Login.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer1.Add( self.Login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SignIn = wx.Button( self, wx.ID_ANY, u"SIGN IN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SignIn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer1.Add( self.SignIn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.Login.Bind( wx.EVT_BUTTON, self.login )
		self.SignIn.Bind( wx.EVT_BUTTON, self.sign_in_panel )
	
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
		
		self.Username = wx.StaticText( self, wx.ID_ANY, u"USERNAME :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Username.Wrap( -1 )
		gSizer2.Add( self.Username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.Password = wx.StaticText( self, wx.ID_ANY, u"PASSWORD :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Password.Wrap( -1 )
		gSizer2.Add( self.Password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Email = wx.StaticText( self, wx.ID_ANY, u"EMAIL :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Email.Wrap( -1 )
		gSizer2.Add( self.Email, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.SigninPanelButt = wx.Button( self, wx.ID_ANY, u"Sign-in", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SigninPanelButt.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer2.Add( self.SigninPanelButt, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		# Connect Events
		self.SigninPanelButt.Bind( wx.EVT_BUTTON, self.sign_in )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sign_in( self, event ):
		event.Skip()
	

