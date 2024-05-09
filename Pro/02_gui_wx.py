# -------------------- 界面开发(wxPython) --------------------
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

    app.MainLoop()


def gui_kino():
    # 创建一个应用程序对象(每一个wxPython程序都必须又一个应用程序对象)
    app = wx.App()

    frm = wx.Frame(None, title='BLAME', style=wx.RESIZE_BORDER | wx.SYSTEM_MENU, size=(600, 600), pos=(100, 100))
    # 创建wx.Panel组件,并指定其父容器
    panel = wx.Panel(frm, size=(200, 200), pos=(100, 100))
    # 创建image对象,指定图片路径以及类型
    image = wx.Image('./img/kino1.png', wx.BITMAP_TYPE_PNG)
    my_pic = image.ConvertToBitmap()

    frm.Center()

    # 显示图片
    wx.StaticBitmap(panel, -1, my_pic)

    frm.Show()

    app.MainLoop()


def main():
    first_wx()


if __name__ == '__main__':
    main()
