# -------------------- 使用千帆AI模型 + GUI实现一个AI聊天程序 --------------------
import wx


class QianfanFrame(wx.Frame):
    def __init__(self, *arges, **kwargs):
        super().__init__(*arges, **kwargs)
        self.init_ui()

    def init_ui(self):
        # 创建一个 菜单栏 对象 (因为后续的退出快捷键cmd+Q,需要它)
        menubar = wx.MenuBar()
        # 在主窗口中添加 菜单栏
        self.SetMenuBar(menubar)
        # 绑定事件 当按下cmd+Q时触发 on_quit函数
        # (这里为什么会绑定cmd+Q我也没有查到,只能暂时认为是在不指定绑定的快捷键的情况下默认就绑定的是cmd+Q吧)
        self.Bind(wx.EVT_MENU, self.on_quit)

        self.panel = wx.Panel(self, pos=(100, 100))
        # 设置背景图片
        pic_bit = wx.Bitmap()
        pic_bit.LoadFile('../img/kuroniko.jpeg')
        self.bit_map = wx.StaticBitmap(self.panel, -1, pic_bit, pos=(0, 30))

    def on_quit(self, event):
        self.Close(True)

    def test(self, event):
        print('miemei')


def main():
    app = wx.App()
    ex = QianfanFrame(None, title="chat TGP", style=wx.RESIZE_BORDER | wx.CLOSE_BOX, size=(600, 600),
                      pos=(100, 100))
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
