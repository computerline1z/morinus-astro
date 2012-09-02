#!/usr/bin/env python
# encoding: utf-8
"""
mrclasses.py

Created by Vaclav Spirhanzl on 2012-08-31.
"""

import wx


class MrTopFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		wx.Frame.__init__(self, *args, **kwargs)

		self._activewindow = None

	"""
		The activewindow property contains active window or None
	"""
	@property
	def activewindow(self):
		return self._activewindow

	@activewindow.setter
	def activewindow(self, value):
		self._activewindow = value

	@activewindow.deleter
	def activewindow(self):
	# TODO: implement implementation error, activatewindow must not be deleted
		pass


class MrSecondFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		wx.Frame.__init__(self, *args, **kwargs)

		self.Bind(wx.EVT_ACTIVATE, self.OnActivate)
		self.Bind(wx.EVT_CLOSE, self.OnClose)

	def OnActivate(self, event):
		app = wx.GetApp()
		topwindow = app.GetTopWindow()
		if event.Active:    # window activated
			topwindow.mhoros.Enable(topwindow.ID_CloseWindow, True)
			topwindow.activewindow = self
		else:               # window deactivated
			topwindow.mhoros.Enable(topwindow.ID_CloseWindow, False)
			topwindow.activewindow = None

		event.Skip()        # propagates event

	def OnClose(self, event):
		app = wx.GetApp()
		topwindow = app.GetTopWindow()
		topwindow.mhoros.Enable(topwindow.ID_CloseWindow, False)
		if topwindow.activewindow is self:
			topwindow.activewindow = None

		event.Skip()


class MrWindow(wx.Window):
	def __init__(self, *args, **kwargs):
		wx.Window.__init__(self, *args, **kwargs)
