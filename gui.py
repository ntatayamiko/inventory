# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
#import wx.calendar
import wx.grid
import wx.dataview

###########################################################################
## Class LoginPage
###########################################################################

class LoginPage ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.first = wx.StaticText( self, wx.ID_ANY, u"INVENTORY ACCOUNT", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.first.Wrap( -1 )
		self.first.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.first, 1, wx.ALL|wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"USERNAME :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"PASSWORD :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.loginbutton = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.loginbutton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.signinbutton = wx.Button( self, wx.ID_ANY, u"SIGN-IN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.signinbutton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.loginbutton.Bind( wx.EVT_BUTTON, self.user_login )
		self.signinbutton.Bind( wx.EVT_BUTTON, self.create_user )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def user_login( self, event ):
		event.Skip()
	
	def create_user( self, event ):
		event.Skip()
	

###########################################################################
## Class signUp
###########################################################################

class signUp ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sign-Up Page", pos = wx.DefaultPosition, size = wx.Size( 509,373 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"USERNAME :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl3, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"PASSWORD :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer3.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"EMAIL :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl5, 1, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self, wx.ID_ANY, u"CLOSE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button14, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"SIGN-UP", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button15, 1, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button15.Bind( wx.EVT_BUTTON, self.create_account )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def create_account( self, event ):
		event.Skip()
	

###########################################################################
## Class HomePage
###########################################################################

class HomePage ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 899,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"LIVESTOCK INVENTORY", wx.Point( 40,10 ), wx.Size( 10,50 ), wx.ALIGN_CENTRE )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 71, 90, 92, False, "Book Antiqua" ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 0, 170, 0 ) )
		self.m_staticText4.SetBackgroundColour( wx.Colour( 237, 244, 236 ) )
		
		bSizer3.Add( self.m_staticText4, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"INVENTORY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"EMPLOYEES", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"SALES", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button14 = wx.Button( self, wx.ID_ANY, u"RESOURCES", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"FINANCES", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"REPORTS", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.m_button17 = wx.Button( self, wx.ID_ANY, u"EVENTS", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button18 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button18, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( gSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_calendar1 = wx.calendar.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.calendar.CAL_SHOW_HOLIDAYS )
		bSizer3.Add( self.m_calendar1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class INVENTORY
###########################################################################

class INVENTORY ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 952,797 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 7, 9 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( True )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.SetColSize( 0, 80 )
		self.m_grid1.SetColSize( 1, 80 )
		self.m_grid1.SetColSize( 2, 80 )
		self.m_grid1.SetColSize( 3, 80 )
		self.m_grid1.SetColSize( 4, 163 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"inv_id" )
		self.m_grid1.SetColLabelValue( 1, u"name" )
		self.m_grid1.SetColLabelValue( 2, u"weight" )
		self.m_grid1.SetColLabelValue( 3, u"age" )
		self.m_grid1.SetColLabelValue( 4, u"date_purchased" )
		self.m_grid1.SetColLabelValue( 5, u"status" )
		self.m_grid1.SetColLabelValue( 6, u"purchase_price" )
		self.m_grid1.SetColLabelValue( 7, u"market_value" )
		self.m_grid1.SetColLabelValue( 8, u"quantity" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.AutoSizeRows()
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.m_grid1, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"inv_id :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer7.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl13, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Specie :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer7.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		m_choice3Choices = [ u"CATTLE", u"SHEEP", u"GOAT", u"PIG", u"POULTRY" ]
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		gSizer7.Add( self.m_choice3, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"weight :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer7.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl15, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"age :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gSizer7.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl16, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"date_purchased :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		gSizer7.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_textCtrl17, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Gender :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		gSizer7.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		m_choice2Choices = [ u"MALE", u"FEMALE", u"CASTRATED" ]
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 1 )
		gSizer7.Add( self.m_choice2, 0, wx.ALL, 5 )
		
		
		gSizer6.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"purchase_price :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer8.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl19, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"market_value :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gSizer8.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl20, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"quantity :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer8.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"status :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gSizer8.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl18, 0, wx.ALL, 5 )
		
		
		gSizer6.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"ADD", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button15, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"UPDATE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.m_button17 = wx.Button( self, wx.ID_ANY, u"DELETE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button17, 0, wx.ALL, 5 )
		
		self.m_button18 = wx.Button( self, wx.ID_ANY, u"ADD TO CART", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button18, 0, wx.ALL, 5 )
		
		self.m_button19 = wx.Button( self, wx.ID_ANY, u"HOME", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button19, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EMPLOYEES
###########################################################################

class EMPLOYEES ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1096,806 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 5, 12 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"ID" )
		self.m_grid2.SetColLabelValue( 1, u"NAME" )
		self.m_grid2.SetColLabelValue( 2, u"DEPARTMENT" )
		self.m_grid2.SetColLabelValue( 3, u"AGE" )
		self.m_grid2.SetColLabelValue( 4, u"VILLAGE" )
		self.m_grid2.SetColLabelValue( 5, u"STATUS" )
		self.m_grid2.SetColLabelValue( 6, u"ACCOUNT #" )
		self.m_grid2.SetColLabelValue( 7, u"SALARY" )
		self.m_grid2.SetColLabelValue( 8, u"DATE EMPLOYED" )
		self.m_grid2.SetColLabelValue( 9, u"PAYED" )
		self.m_grid2.SetColLabelValue( 10, u"CONTACT" )
		self.m_grid2.SetColLabelValue( 11, u"EMAIL" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.m_grid2, 0, wx.ALL, 5 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer5.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"NAME :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer5.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"DEPARTMENT :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer5.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"AGE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer5.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"VILLAGE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer5.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"STATUS :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer5.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"ACCOUNT # :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gSizer5.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl12, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"SALARY :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gSizer5.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl22, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"DATE EMPLOYED :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		gSizer5.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl23, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"PAYED :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gSizer5.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl24, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"CONTACT :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gSizer5.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl25, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"EMAIL :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		gSizer5.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		
		gSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"ADD EMPLOYEE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button13, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self, wx.ID_ANY, u"UPDATE EMPLOYEE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button20 = wx.Button( self, wx.ID_ANY, u"DELETE EMPLOYEE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button20, 0, wx.ALL, 5 )
		
		self.m_button21 = wx.Button( self, wx.ID_ANY, u"HOME", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button21, 0, wx.ALL, 5 )
		
		
		gSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class SALES
###########################################################################

class SALES ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		bSizer8.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class FullInventoryView
###########################################################################

class FullInventoryView ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1512,797 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Core Identification" ), wx.VERTICAL )
		
		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText34 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer18.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl2 = wx.dataview.DataViewCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_dataViewCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"SPECIE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gSizer18.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl1 = wx.dataview.DataViewCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_dataViewCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BREED :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer18.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl28 = wx.dataview.DataViewCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_dataViewCtrl28, 0, wx.ALL, 5 )
		
		
		gSizer11.Add( gSizer18, 1, wx.EXPAND, 5 )
		
		gSizer19 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"GENDER :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer19.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl29 = wx.dataview.DataViewCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_dataViewCtrl29, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"AGE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer19.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl30 = wx.dataview.DataViewCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_dataViewCtrl30, 0, wx.ALL, 5 )
		
		
		gSizer11.Add( gSizer19, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( gSizer11, 1, wx.EXPAND, 5 )
		
		
		gSizer10.Add( sbSizer1, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Ownership and Location" ), wx.VERTICAL )
		
		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText35 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"OWNER ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gSizer13.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl5 = wx.dataview.DataViewCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_dataViewCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"LOCATION :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		gSizer13.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl3 = wx.dataview.DataViewCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_dataViewCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"FARM :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer13.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl4 = wx.dataview.DataViewCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_dataViewCtrl4, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( gSizer13, 1, wx.EXPAND, 5 )
		
		
		gSizer10.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Health and medical History" ), wx.VERTICAL )
		
		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer23 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText41 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"VACCINATION RECORD :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		gSizer23.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl6 = wx.dataview.DataViewCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_dataViewCtrl6, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"LAST VET VISIT :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		gSizer23.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl7 = wx.dataview.DataViewCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_dataViewCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"MEDICAL CONDITION :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		gSizer23.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl8 = wx.dataview.DataViewCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_dataViewCtrl8, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( gSizer23, 1, wx.EXPAND, 5 )
		
		gSizer24 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText40 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"MEDICAL HISTORY :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		gSizer24.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl10 = wx.dataview.DataViewCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer24.Add( self.m_dataViewCtrl10, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"HEALTH STATUS :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		gSizer24.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl9 = wx.dataview.DataViewCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer24.Add( self.m_dataViewCtrl9, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( gSizer24, 1, wx.EXPAND, 5 )
		
		
		sbSizer3.Add( gSizer12, 1, wx.EXPAND, 5 )
		
		
		gSizer10.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Reproduction and Breeding" ), wx.VERTICAL )
		
		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText47 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"BREEDING STATUS :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		gSizer25.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl11 = wx.dataview.DataViewCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_dataViewCtrl11, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"PREGNANCY DUE DATE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		gSizer25.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl12 = wx.dataview.DataViewCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_dataViewCtrl12, 0, wx.ALL, 5 )
		
		self.m_staticText45 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"SIRE ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		gSizer25.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl13 = wx.dataview.DataViewCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_dataViewCtrl13, 0, wx.ALL, 5 )
		
		
		gSizer14.Add( gSizer25, 1, wx.EXPAND, 5 )
		
		gSizer26 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText43 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"DAM ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		gSizer26.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl14 = wx.dataview.DataViewCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_dataViewCtrl14, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"OFFSPRING COUNT :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		gSizer26.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl15 = wx.dataview.DataViewCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.m_dataViewCtrl15, 0, wx.ALL, 5 )
		
		
		gSizer14.Add( gSizer26, 1, wx.EXPAND, 5 )
		
		
		sbSizer4.Add( gSizer14, 1, wx.EXPAND, 5 )
		
		
		gSizer10.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Inventory Management" ), wx.VERTICAL )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer27 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText52 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"ACQUISITION DATE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		gSizer27.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_dataViewCtrl20 = wx.dataview.DataViewCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer27.Add( self.m_dataViewCtrl20, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"ACQUISITION SOURCE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		gSizer27.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_dataViewCtrl19 = wx.dataview.DataViewCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer27.Add( self.m_dataViewCtrl19, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"STATUS :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		gSizer27.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_dataViewCtrl18 = wx.dataview.DataViewCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer27.Add( self.m_dataViewCtrl18, 0, wx.ALL, 5 )
		
		
		gSizer15.Add( gSizer27, 1, wx.EXPAND, 5 )
		
		gSizer28 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText49 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"DISPOSITION DATE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		gSizer28.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl16 = wx.dataview.DataViewCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer28.Add( self.m_dataViewCtrl16, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"DISPOSITION REASON :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		gSizer28.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl17 = wx.dataview.DataViewCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer28.Add( self.m_dataViewCtrl17, 0, wx.ALL, 5 )
		
		
		gSizer15.Add( gSizer28, 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( gSizer15, 1, wx.EXPAND, 5 )
		
		
		gSizer10.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Physical Attributes" ), wx.VERTICAL )
		
		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText53 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"WEIGHT :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		gSizer16.Add( self.m_staticText53, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl21 = wx.dataview.DataViewCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_dataViewCtrl21, 0, wx.ALL, 5 )
		
		self.m_staticText54 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"COLOR :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		gSizer16.Add( self.m_staticText54, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl22 = wx.dataview.DataViewCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_dataViewCtrl22, 0, wx.ALL, 5 )
		
		self.m_staticText55 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"TAG # :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		gSizer16.Add( self.m_staticText55, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl23 = wx.dataview.DataViewCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_dataViewCtrl23, 0, wx.ALL, 5 )
		
		self.m_staticText56 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"MICROCHIP ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		gSizer16.Add( self.m_staticText56, 0, wx.ALL, 5 )
		
		self.m_dataViewCtrl24 = wx.dataview.DataViewCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_dataViewCtrl24, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( gSizer16, 1, wx.EXPAND, 5 )
		
		
		gSizer10.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Financial Tracking" ), wx.VERTICAL )
		
		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText57 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"PURCHASE PRICE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		gSizer17.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_dataViewCtrl25 = wx.dataview.DataViewCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.m_dataViewCtrl25, 0, wx.ALL, 5 )
		
		self.m_staticText58 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"CURRENT VALUE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		gSizer17.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_dataViewCtrl26 = wx.dataview.DataViewCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.m_dataViewCtrl26, 0, wx.ALL, 5 )
		
		self.m_staticText59 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"SOLD PRICE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		gSizer17.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_dataViewCtrl27 = wx.dataview.DataViewCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.m_dataViewCtrl27, 0, wx.ALL, 5 )
		
		
		sbSizer7.Add( gSizer17, 1, wx.EXPAND, 5 )
		
		
		gSizer10.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class RESOURCES
###########################################################################

class RESOURCES ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class FINANCE
###########################################################################

class FINANCE ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 863,617 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class REPORTS
###########################################################################

class REPORTS ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EVENTS
###########################################################################

class EVENTS ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

