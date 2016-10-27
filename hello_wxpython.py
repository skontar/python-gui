#!/usr/bin/env python2

import wx


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Widgets
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label='Test')

        # Layout
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.button, 1, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizerAndFit(self.sizer)

        # Callbacks
        self.button.Bind(wx.EVT_BUTTON, self.on_button)

        self.Show()

    def on_button(self, event):
        print('wxPython callback')


app = wx.App(False)
win = MainWindow(None)
app.MainLoop()
