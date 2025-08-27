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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,434 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"login" )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.username = wx.StaticText( self.m_panel1, wx.ID_ANY, u"USERNAME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )
		gSizer1.Add( self.username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.name_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.name_textCtrl3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.password = wx.StaticText( self.m_panel1, wx.ID_ANY, u"PASSWORD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )
		gSizer1.Add( self.password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.password_textCtrl4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.password_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.email = wx.StaticText( self.m_panel1, wx.ID_ANY, u"EMAIL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		gSizer1.Add( self.email, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.email_textCtrl5 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.email_textCtrl5, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.login = wx.Button( self.m_panel1, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer1.Add( self.login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.signIn = wx.Button( self.m_panel1, wx.ID_ANY, u"SIGN IN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.signIn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer1.Add( self.signIn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer1 )
		self.m_panel1.Layout()
		bSizer1.Fit( self.m_panel1 )
		bSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.Hide()
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.username1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"USERNAME :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username1.Wrap( -1 )
		gSizer2.Add( self.username1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.username_textCtrl6 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.username_textCtrl6, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.password1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"PASSWORD :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password1.Wrap( -1 )
		gSizer2.Add( self.password1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.password_textCtrl7 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.password_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.email1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"EMAIL :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email1.Wrap( -1 )
		gSizer2.Add( self.email1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.email_textCtrl8 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.email_textCtrl8, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.sign_in_panel = wx.Button( self.m_panel2, wx.ID_ANY, u"Sign-in", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sign_in_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer2.Add( self.sign_in_panel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer3.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.login )
		self.signIn.Bind( wx.EVT_BUTTON, self.sign_in_panel )
		self.sign_in_panel.Bind( wx.EVT_BUTTON, self.sign_in )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def login( self, event ):
		event.Skip()
	
	def sign_in_panel( self, event ):
		event.Skip()
	
	def sign_in( self, event ):
		event.Skip()
	

