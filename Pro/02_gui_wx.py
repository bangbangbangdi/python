# -------------------- 界面开发(wxPython) --------------------
import wx

# -- wxPython简介 --
'''
wxPython是python语言的一套优秀的GUI(Graphical user interface 图形用户界面)库
允许python程序员很方便的创建完整的、功能健全的GUI用户界面.
'''


# -- 第一个wx程序
# 使用之前记得要先安装wxPython库哈~
def first_wx():
    app = wx.App()
    frm = wx.Frame(None, title='BLAME', size=(600, 600), pos=(100, 100))
    panel = wx.Panel(frm, size=(200, 200), pos=(100, 100))
    image = wx.Image('./img/kino1.png', wx.BITMAP_TYPE_PNG)
    my_pic = image.ConvertToBitmap()

    # 显示图片
    wx.StaticBitmap(panel, -1, my_pic)

    frm.Show()

    app.MainLoop()


def main():
    first_wx()


if __name__ == '__main__':
    main()
