#!/usr/bin/env python
# encoding: utf-8

"""
mrclasses.py

	defines base classes for application windows and frames

	MrTopFrame      top application frame
	MrSecondFrame   other frames
	MrWindow        base window class

Created by Vaclav Spirhanzl on 2012-08-31.
"""

import wx

from wx.lib.pubsub import Publisher as Pub

CH_ACTIVATED='children.activated'

class MrTopFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		wx.Frame.__init__(self, *args, **kwargs)

		self._activewindow = None

		Pub().subscribe(self.__onActivateChildren, (CH_ACTIVATED) )

	def __onActivateChildren(self, activated):
		is_activated = activated.data
		assert isinstance(is_activated, bool)
		self.OnActivateChildren(is_activated)

	def OnActivateChildren(self, activated):
		raise NotImplementedError('must be overridden in subclass')

	"""
		The activewindow property contains active window or None
	"""
	@property
	def activewindow(self):
		return self._activewindow

	@activewindow.setter
	def activewindow(self, value):
		if isinstance(value, MrTopFrame) or isinstance(value, MrSecondFrame) or value is None:
			self._activewindow = value
		else:
			raise ValueError('property activewindow')

	@activewindow.deleter
	def activewindow(self):
		raise NotImplementedError('property activewindow can not be deleted')


class MrSecondFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		wx.Frame.__init__(self, *args, **kwargs)

		self.Bind(wx.EVT_ACTIVATE, self.OnActivate)
		self.Bind(wx.EVT_CLOSE, self.OnClose)

	def OnActivate(self, event):
		app = wx.GetApp()
		topwindow = app.GetTopWindow()
		is_active = event.Active
		if is_active:    # window activated
			topwindow.activewindow = self
		else:               # window deactivated
			topwindow.activewindow = None

		Pub().sendMessage(CH_ACTIVATED, is_active)

		event.Skip()        # propagates event

	def OnClose(self, event):
		app = wx.GetApp()
		topwindow = app.GetTopWindow()
		if topwindow.activewindow is self:
			topwindow.activewindow = None
			Pub().sendMessage(CH_ACTIVATED, False)

		event.Skip()


class MrWindow(wx.Window):
	def __init__(self, *args, **kwargs):
		wx.Window.__init__(self, *args, **kwargs)
