# -------------------- 界面开发02(wxPython) --------------------
import wx


# ------ 菜单 ------
class MenuExample(wx.Frame):
    '''
    一个只包含退出功能的菜单栏案例(MacOS中显示会有问题)
    '''

    def __init__(self, *args, **kwargs):
        super(MenuExample, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        # 创建一个 菜单栏 对象
        menubar = wx.MenuBar()
        # 创建一个菜单
        file_menu = wx.Menu()

        # 创建一个菜单项,分配快捷键 command + Q
        quit_item = wx.MenuItem(file_menu, wx.ID_EXIT, '&Quit', 'Quit application')

        # 将菜单添加到菜单栏对象
        menubar.Append(file_menu, 'File')

        # 设置菜单栏
        self.SetMenuBar(menubar)
        # 将quit_item菜单项和self.on_quit方法绑定
        self.Bind(wx.EVT_MENU, self.on_quit, quit_item)

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
