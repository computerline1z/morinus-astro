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

import dispatch as dispatcher


class MrTopFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		wx.Frame.__init__(self, *args, **kwargs)

		self._activewindow = None

		self._child_win_activated = dispatcher.Signal(providing_args=['isactive', ]	)
		self._child_win_activated.connect(self.__onActivateChildren)

	def __onActivateChildren(self, sender, **kwargs):
		is_activated = kwargs['isactive']
		assert isinstance(is_activated, bool)
		assert isinstance(sender, MrSecondFrame)
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
		assert isinstance(topwindow, MrTopFrame)
		is_active = event.Active
		if is_active:    # window activated
			topwindow.activewindow = self
		else:               # window deactivated
			topwindow.activewindow = None

		topwindow._child_win_activated.send(sender=self, isactive=is_active)

		event.Skip()        # propagates event

	def OnClose(self, event):
		app = wx.GetApp()
		topwindow = app.GetTopWindow()
		if topwindow.activewindow is self:
			topwindow.activewindow = None
			topwindow._child_win_activated.send(sender=self, isactive=False)

		event.Skip()


class MrWindow(wx.Window):
	def __init__(self, *args, **kwargs):
		wx.Window.__init__(self, *args, **kwargs)
