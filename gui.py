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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 787,721 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Inventory Control System", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 76, 90, 92, False, "@Adobe Myungjo Std M" ) )
		
		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.login_entry = wx.Button( self.m_panel1, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.login_entry, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.signup_entry = wx.Button( self.m_panel1, wx.ID_ANY, u"Sign Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.signup_entry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.signup_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.signup_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.signup_panel2.Hide()
		
		signup_gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.signUser_staticText2 = wx.StaticText( self.signup_panel2, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.signUser_staticText2.Wrap( -1 )
		signup_gSizer2.Add( self.signUser_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.username_textCtrl1 = wx.TextCtrl( self.signup_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		signup_gSizer2.Add( self.username_textCtrl1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.email_staticText31 = wx.StaticText( self.signup_panel2, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email_staticText31.Wrap( -1 )
		signup_gSizer2.Add( self.email_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.signup_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		signup_gSizer2.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.password_staticText4 = wx.StaticText( self.signup_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password_staticText4.Wrap( -1 )
		signup_gSizer2.Add( self.password_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.password_textCtrl3 = wx.TextCtrl( self.signup_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		signup_gSizer2.Add( self.password_textCtrl3, 0, wx.ALL, 5 )
		
		self.signup_button3 = wx.Button( self.signup_panel2, wx.ID_ANY, u"Sign Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		signup_gSizer2.Add( self.signup_button3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.signup_panel2.SetSizer( signup_gSizer2 )
		self.signup_panel2.Layout()
		signup_gSizer2.Fit( self.signup_panel2 )
		bSizer1.Add( self.signup_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.login_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.login_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.login_panel21.Hide()
		
		login_gSizer21 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.loginUser_staticText21 = wx.StaticText( self.login_panel21, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loginUser_staticText21.Wrap( -1 )
		login_gSizer21.Add( self.loginUser_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.username_textCtrl11 = wx.TextCtrl( self.login_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		login_gSizer21.Add( self.username_textCtrl11, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.email_staticText311 = wx.StaticText( self.login_panel21, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email_staticText311.Wrap( -1 )
		login_gSizer21.Add( self.email_staticText311, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self.login_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		login_gSizer21.Add( self.m_textCtrl21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.password_staticText41 = wx.StaticText( self.login_panel21, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password_staticText41.Wrap( -1 )
		login_gSizer21.Add( self.password_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.password_textCtrl31 = wx.TextCtrl( self.login_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		login_gSizer21.Add( self.password_textCtrl31, 0, wx.ALL, 5 )
		
		self.login_button31 = wx.Button( self.login_panel21, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		login_gSizer21.Add( self.login_button31, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.login_panel21.SetSizer( login_gSizer21 )
		self.login_panel21.Layout()
		login_gSizer21.Fit( self.login_panel21 )
		bSizer1.Add( self.login_panel21, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.login_entry.Bind( wx.EVT_BUTTON, self.login_panel )
		self.signup_entry.Bind( wx.EVT_BUTTON, self.signup_panel )
		self.signup_button3.Bind( wx.EVT_BUTTON, self.create_account )
		self.login_button31.Bind( wx.EVT_BUTTON, self.loginUser )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def login_panel( self, event ):
		event.Skip()
	
	def signup_panel( self, event ):
		event.Skip()
	
	def create_account( self, event ):
		event.Skip()
	
	def loginUser( self, event ):
		event.Skip()
	

###########################################################################
## Class homeFrame
###########################################################################

class homeFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HOME", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

