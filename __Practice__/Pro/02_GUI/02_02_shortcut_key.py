import wx

class MenuExample(wx.Frame):
    '''一个只包含退出功能的菜单栏案例（MacOS中有默认显示问题）'''

    def __init__(self, *args, **kwargs):
        super(MenuExample, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        # 创建一个【菜单栏】对象
        menubar = wx.MenuBar()
        # 创建菜单
        file_menu = wx.Menu()
        edit_menu = wx.Menu()