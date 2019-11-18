import webbrowser
import wx
import requests
from CSVParser import CSVParser
class TorrentPanel(wx.Panel):    
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)


        self.row_obj_dict = {}
        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 800), 
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Titolo', width=140)
        self.list_ctrl.InsertColumn(1, 'Descrizione', width=140)
        self.list_ctrl.InsertColumn(2, 'Dimensione', width=200)
        self.list_ctrl.InsertColumn(3, 'Magnet', width=200)
               
        search_button = wx.Button(self, label='Search')
        search_button.Bind(wx.EVT_BUTTON, self.update_torrent_listing)
        edit_button = wx.Button(self, label='Download')
        edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        self.text_ctrl = wx.TextCtrl(self,style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.update_torrent_listing)
        self.current_file_txt = wx.StaticText(self,  label='Made with <3 by LSigi', pos=(30, 190))
        main_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 5)     
        main_sizer.Add(search_button, 0, wx.ALL | wx.CENTER, 20)        
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 0) 
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5) 
        main_sizer.Add(self.current_file_txt,0,wx.ALL | wx.CENTER,5)   
        self.SetSizer(main_sizer)

    def on_edit(self, event):
        selection = self.list_ctrl.GetFocusedItem()
        if selection >= 0:
            torrent = self.row_obj_dict[selection]
            webbrowser.open(torrent["magnet"])
    
    def update_torrent_listing(self, event):
        data = self.get_data(self.text_ctrl.GetValue())
        self.list_ctrl.ClearAll()
        self.list_ctrl.InsertColumn(0, 'Titolo', width=140)
        self.list_ctrl.InsertColumn(1, 'Descrizione', width=140)
        self.list_ctrl.InsertColumn(2, 'Dimensione', width=200)
        self.list_ctrl.InsertColumn(3, 'Magnet', width=200)

        torrent_objects = []
        index = 0
        for row in data:
            self.list_ctrl.InsertItem(index, data[row]["titolo"])
            self.list_ctrl.SetItem(index, 1, data[row]["descrizione"])
            self.list_ctrl.SetItem(index, 2, data[row]["dimensione"])
            self.list_ctrl.SetItem(index, 3, data[row]["magnet"])
            torrent_objects.append(row)
            self.row_obj_dict[index] = data[row]
            index += 1
   
    def get_data(self,nometorrent):
        parser = CSVParser()
        return parser.do_query(nometorrent)