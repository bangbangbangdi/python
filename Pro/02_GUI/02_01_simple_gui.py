# -------------------- 界面开发01(wxPython) --------------------
import random

import wx

# -- wxPython简介 --
'''
wxPython是python语言的一套优秀的GUI(Graphical user interface 图形用户界面)库
允许python程序员很方便的创建完整的、功能健全的GUI用户界面.

reference from https://github.com/necan/wxPython-tutorial/blob/master
'''


# -- 第一个wx程序
# 使用之前记得要先安装wxPython库哈~
def first_wx():
    # 创建一个应用程序对象(每一个wxPython程序都必须又一个应用程序对象)
    app = wx.App()

    # 创建了一个wx.Frame对象. wx.Frame是其他组件的父组件,以后我们会经常见到它.
    frm = wx.Frame(None, title='First wxPython application')
    # 创建了wx.Frame之后,还必须调用Show()方法将其显示在屏幕上.
    frm.Show()

    # 进入主循环,该循环是一个无限循环,它负责捕获和分发我们应用程序生命周期中存在的所有事件
    app.MainLoop()


def about_frame():
    app = wx.App()
    # construct 构造函数
    frm = wx.Frame(None, title='这是标题参数', size=(500, 200), pos=(300, 300),
                   style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.CLOSE_BOX)

    # style
    '''
    style参数有点奇怪是吧.
    顾名思义,该参数决定的是Frame的风格(那怎么还能同时拥有三种风格呢?)
    因为这里的风格粒度非常的小,单独拿出来几乎没有意义,一般都是组合使用的;具体如下
    wx.MINIMIZE_BOX = 拥有最小化按钮
    RESIZE_BORDER  = 窗口大小可调节
    CLOSE_BOX = 拥有窗口关闭按钮
    (中间的 | 是或运算符)
    '''

    frm.Show()
    # size and position
    '''同样是在构造函数中,我们可以通过size和pos参数指定Frame的大小和位置'''

    app.MainLoop()


def gui_kino():
    # 创建一个应用程序对象(每一个wxPython程序都必须又一个应用程序对象)
    app = wx.App()

    frm = wx.Frame(None, title='BLAME', style=wx.RESIZE_BORDER | wx.SYSTEM_MENU, size=(600, 600), pos=(100, 100))
    # 创建wx.Panel组件,并指定其父容器
    panel = wx.Panel(frm, size=(200, 200), pos=(100, 100))
    # 创建image对象,指定图片路径以及类型
    image = wx.Image('../img/kino.png', wx.BITMAP_TYPE_PNG)

    my_pic = image.ConvertToBitmap()

    bitmap = wx.Bitmap('../img/kino.png')

    frm.Center()

    # 显示图片
    # wx.StaticBitmap(panel, -1, my_pic)
    wx.StaticBitmap(panel, -1, bitmap)

    frm.Show()

    app.MainLoop()


def on_click(event):
    print('xxx')


def main():
    # first_wx()
    # about_frame()
    gui_kino()


if __name__ == '__main__':
    main()
