#!/usr/bin/env python2

from __future__ import print_function
import wx


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.SetTitle('wxPython')

        # Widgets
        self.panel = wx.Panel(self)
        self.button_start = wx.Button(self.panel, label='Start')
        self.button_stop = wx.Button(self.panel, label='Stop')
        self.button_stop.Disable()
        self.progress = wx.Gauge(self.panel)

        # Layout
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.button_start, (0, 0), flag=wx.ALL | wx.EXPAND)
        self.sizer.Add(self.button_stop, (1, 0), flag=wx.ALL | wx.EXPAND)
        self.sizer.Add(self.progress, (2, 0), flag=wx.ALL | wx.EXPAND)
        self.sizer.AddGrowableRow(0, proportion=1)
        self.sizer.AddGrowableRow(1, proportion=1)
        self.sizer.AddGrowableCol(0, proportion=1)

        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        # Callbacks
        # This example is not finished as it is Python 2 only.
        # Long running tasks can be handled using `wx.lib.delayedresult` or normal thread and
        # `wx.CallAfter` to send signals to main thread.

        self.Show()


print('wxPython', wx.__version__)
# print(wx.GetLibraryVersionInfo().GetVersionString())  # Phoenix only
app = wx.App(False)
win = MainWindow(None)
app.MainLoop()
