import wx
from TorrentPanel import TorrentPanel
class TorrentFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='TNT Downloader')
        self.panel = TorrentPanel(self)
        self.Show()
