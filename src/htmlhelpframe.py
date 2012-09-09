import wx
import wx.html
import mrclasses


class HtmlHelpFrame(mrclasses.MrSecondFrame):

	def __init__(self, parent, id, title, fname):
		mrclasses.MrSecondFrame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(640, 400))

		self.myhtml = wx.html.HtmlWindow(self, id)
		self.myhtml.LoadPage(fname)







