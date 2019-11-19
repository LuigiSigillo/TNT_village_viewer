import wx
from TorrentFrame import TorrentFrame


if __name__ == '__main__':
    app = wx.App()
    frame = TorrentFrame()
    frame.Maximize()
    app.MainLoop()