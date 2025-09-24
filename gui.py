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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 985,789 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.Hide()
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText8 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer10.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText9 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Age", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer10.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Supplier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer10.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		
		gSizer6.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"Gender" ), wx.VERTICAL )
		
		self.m_radioBtn3 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Male", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_radioBtn3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Female", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_radioBtn4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer6.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		id_date_sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"id" ), wx.VERTICAL )
		
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.id_label = wx.StaticText( id_date_sbSizer4.GetStaticBox(), wx.ID_ANY, u"Id Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_label.Wrap( -1 )
		gSizer9.Add( self.id_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( id_date_sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.date_staticText16 = wx.StaticText( id_date_sbSizer4.GetStaticBox(), wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_staticText16.Wrap( -1 )
		gSizer9.Add( self.date_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( id_date_sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl15, 0, wx.ALL, 5 )
		
		
		id_date_sbSizer4.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		
		gSizer6.Add( id_date_sbSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		self.add_button = wx.Button( self.main_panel, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.add_button, 0, wx.ALL, 5 )
		
		self.delete_button = wx.Button( self.main_panel, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.delete_button, 0, wx.ALL, 5 )
		
		self.update_button = wx.Button( self.main_panel, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.update_button, 0, wx.ALL, 5 )
		
		
		gSizer4.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		bSizer5.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"Weight" ), wx.VERTICAL )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"unslottered", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer7.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Slottered", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer7.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"Costs" ), wx.VERTICAL )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText13 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Purchase Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer8.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Estimated Selling Cost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gSizer8.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl13, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		gSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.main_panel.SetSizer( gSizer4 )
		self.main_panel.Layout()
		gSizer4.Fit( self.main_panel )
		bSizer1.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
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
	

