#!/usr/bin/python

import wx
import os

if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title="usbDescriptorGenerator")
    frm.Show()
    """
    #frame = MainFrame(None, templates)
    #MainWindow(frame, templates)
    #frame.Show(True)
    """
    app.MainLoop()