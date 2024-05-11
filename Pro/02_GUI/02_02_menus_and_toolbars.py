# -------------------- 界面开发02(wxPython) --------------------
import wx


# ------ 菜单 ------
class MenuExample(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MenuExample, self).__init__(*args, **kwargs)

    def init_ui(self):
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_item = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(file_menu, '&File')
        self.SetMenuBar(menubar)
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
