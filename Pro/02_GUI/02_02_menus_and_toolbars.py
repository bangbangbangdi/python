# -------------------- 界面开发02(wxPython) --------------------
import wx


# ------ 菜单 ------
class MenuExample(wx.Frame):
    '''
    一个只包含退出功能的菜单栏案例(mac上基本无效... window能正常运行)
    '''

    def __init__(self, *args, **kwargs):
        super(MenuExample, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        # 创建一个 菜单栏 对象
        menubar = wx.MenuBar()
        # 创建一个 菜单 对象(放在菜单栏中)
        file_menu = wx.Menu()

        # 在 菜单 对象中追加 菜单项(放在菜单中)
        file_item = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        # 将 菜单 对象,放入 菜单栏 中
        menubar.Append(file_menu, '&File')
        # 设置菜单栏
        self.SetMenuBar(menubar)
        # 将菜单退出事件绑定器(即快捷键command + Q) 绑定到on_quit方法
        self.Bind(wx.EVT_MENU, self.on_quit, file_item)

        self.SetSize((300, 200))
        self.SetTitle('Simple Menu')

    def on_quit(self, event):
        self.Close(True)


def run_menu():
    app = wx.App()
    menu = MenuExample(None)
    menu.Show()
    app.MainLoop()


def main():
    run_menu()


if __name__ == '__main__':
    main()
