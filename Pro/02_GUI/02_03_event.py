# -------------------- 事件03(wxPython) --------------------
import wx


class EventFrame(wx.Frame):
    def __init__(self, *arges, **kwargs):
        super(EventFrame, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.frm = wx.Frame(None, title='BLAME', style=wx.RESIZE_BORDER | wx.CLOSE_BOX, size=(600, 600),
                            pos=(100, 100))
        # 创建一个 菜单栏 对象
        menubar = wx.MenuBar()
        # 设置菜单栏
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_quit)
        # 创建wx.Panel组件,并指定其父容器
        panel = wx.Panel(self.frm, size=(200, 200), pos=(100, 100))
        # 创建image对象,指定图片路径以及类型
        self.image = wx.Image('../img/kino1.png', wx.BITMAP_TYPE_PNG)

        my_pic = self.image.ConvertToBitmap()

        self.frm.Center()

        # 显示图片
        wx.StaticBitmap(panel, -1, my_pic)
        self.frm.Show()

    def on_quit(self, event):
        self.Close(True)


def main():
    app = wx.App()
    ex = EventFrame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
