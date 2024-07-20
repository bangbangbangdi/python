# 利用wxPytho库创建GUI界面
import wx
def first_wx():
    # 创建一个应用程序对象（每一个wxpython都必须有一个应用程序对象）
    app = wx.App()

    # 创建了一个wx.Frame对象。wx.Frame是其它组件的父组件。
    frm = wx.Frame(None, title='Hello World')
    # 创建了wx.Frame之后，还必须调用Show的方法将其显示在屏幕上。
    frm.Show()

    # 进入住循环。该循环是一个无限循环，它负责捕获和分发我们应用程序生命周期中存在的所有事件。
    app.MainLoop()

def about_frame():
    app = wx.App()
    # construct 构造函数
    frm = wx.Frame(None, title='Hello World', size=(800, 600), pos=(100, 100), style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.CLOSE_BOX)
    # style决定了frame的功能。使用时根据需求查询。

    '''html+wxPython的可能性？'''

    frm.Show()

