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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.first = wx.StaticText( self, wx.ID_ANY, u"FIRST FRAME", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.first.Wrap( -1 )
		self.first.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.first, 1, wx.ALL|wx.EXPAND, 5 )
		
		Update ProductChoices = []
		self.Update Product = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, Update ProductChoices, 0 )
		self.Update Product.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.Update Product, 1, wx.ALIGN_RIGHT, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
app=wx.app()
frame=MyFrame1(None)
frame.Show()
app.MainLoop()