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
        # 创建菜单
        file_menu = wx.Menu()
        edit_menu = wx.Menu()

        # 创建一个 退出 菜单项:
        # file_menu : 父容器
        # wx.ID_EXIT : wx.Python定义的标准ID,
        #   部分标准ID会默认绑定快捷键 cmd + Q
        #   如果没有默认绑定快捷键可以通过\t + '快捷键' 声明 (/t是分割符,用于在文本中绑定快捷键)
        # '&Quit' : 菜单项中显示的文本 &后的第一个字符会显示下划线
        # 'Quit application' : 当鼠标悬浮在上面时会显示的提示文本
        quit_item = wx.MenuItem(file_menu, wx.ID_EXIT, '&Quit', 'quit application')
        # 将quit_item 菜单项 添加到 菜单 file_menu中
        file_menu.Append(quit_item)

        # 新建 声明快捷键 cmd + N
        new_item = wx.MenuItem(file_menu, wx.ID_NEW, '&New\tCtrl+N', 'New File')
        file_menu.Append(new_item)

        # 打开
        open_item = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open', 'Open File')
        file_menu.Append(open_item)

        # 保存
        save_item = wx.MenuItem(file_menu, wx.ID_SAVE, '&Save', 'Save File')
        file_menu.Append(save_item)

        # 撤销
        undo_item = wx.MenuItem(edit_menu, wx.ID_UNDO, '&Undo', 'Undo')
        edit_menu.Append(undo_item)

        # 将菜单添加到菜单栏
        menubar.Append(file_menu, 'File')
        menubar.Append(edit_menu, 'Edit')

        # 设置菜单栏
        self.SetMenuBar(menubar)
        # 将quit_item菜单项和self.on_quit方法绑定
        self.Bind(wx.EVT_MENU, self.on_quit, quit_item)
        self.Bind(wx.EVT_MENU, self.on_new, new_item)

        self.SetSize((300, 200))
        self.SetTitle('Simple Menu')

    def on_quit(self, event):
        # 关闭整个应用程序
        self.Close(True)

    def on_new(self, event):
        print('新建事件被触发了...')


def run_menu():
    app = wx.App()
    menu = MenuExample(None)
    menu.Show()
    app.MainLoop()


def main():
    run_menu()


if __name__ == '__main__':
    main()
