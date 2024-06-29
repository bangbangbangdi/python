import random
import wx


def first_wx():
    app = wx.App()


    frm = wx.Frame(None, title='First wxPython application', size=(600,300), pos=(300,300),
                   style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.CLOSE_BOX)
    frm.Show()

    app.MainLoop()

# first_wx()

def gui_kino():
    app = wx.App()
    frm = wx.Frame(None, title='Kino', style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLOSE_BOX, size=(500,500), pos=(100,100))

    panel = wx.Panel(frm, size=(200,200), pos=(100,100))
    image = wx.Image('./kino.png', wx.BITMAP_TYPE_PNG)

    my_pic = image.ConvertToBitmap()

    frm.Center()

    wx.StaticBitmap(panel, -1, my_pic)

    frm.Show()

    app.MainLoop()

gui_kino()