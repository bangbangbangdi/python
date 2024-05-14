# -------------------- 事件03(wxPython) --------------------
import wx


class EventFrame(wx.Frame):
    def __init__(self, *arges, **kwargs):
        super(EventFrame, self).__init__(*arges, **kwargs)
        self.init_ui()

    def init_ui(self):
        # 创建一个 菜单栏 对象
        menubar = wx.MenuBar()
        # 设置菜单栏
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_quit)
        # 创建wx.Panel组件,并指定其父容器
        self.panel = wx.Panel(self, size=(200, 200), pos=(100, 100))
        # 创建image对象,指定图片路径以及类型
        self.img_path = '../img/kino1.png'
        self.image = wx.Image(self.img_path, wx.BITMAP_TYPE_PNG)
        my_pic = self.image.ConvertToBitmap()
        # 显示图片
        wx.StaticBitmap(self.panel, -1, my_pic, pos=(0, 30))
        change_btn = wx.Button(self.panel, label='Change Picture')
        test_btn = wx.Button(self.panel, label='test', pos=(200, 4))
        change_btn.Show()
        test_btn.Show()
        self.Bind(wx.EVT_BUTTON, self.change_picture, change_btn)
        self.Bind(wx.EVT_BUTTON, self.test, test_btn)

    def on_quit(self, event):
        self.Close(True)

    def change_picture(self, event):
        self.img_path = '../img/cibo.jpeg' if self.img_path == '../img/kino1.png' else '../img/kino1.png'
        type = wx.BITMAP_TYPE_PNG if self.img_path == '../img/kino1.png' else wx.BITMAP_TYPE_JPEG
        self.image.LoadFile(self.img_path, type)
        my_pic = self.image.ConvertToBitmap()
        # 显示图片
        wx.StaticBitmap(self.panel, 1, my_pic, pos=(0, 30))
        self.SetSize(self.image.GetSize())

    def test(self, event):
        self.image.Resize(size=(400, 400), pos=(0, 30))
        pass


def main():
    app = wx.App()
    ex = EventFrame(None, title='BLAME', style=wx.RESIZE_BORDER | wx.CLOSE_BOX, size=(600, 600), pos=(100, 100))
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
