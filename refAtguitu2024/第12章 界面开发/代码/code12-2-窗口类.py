import wx

class MyFrame(wx.Frame):
    # 构造方法
    def __init__(self):
        wx.Frame.__init__(self,None,title='mia学习系统')
        # 创建面板
        pl = wx.Panel(self)
        # 创建静态文本
        staticText = wx.StaticText(pl,label='欢迎学习python')
        # 创建按钮
        btn = wx.Button(pl,label='开始学习',pos=(300,400))


# 创建应用程序对象
app = wx.App()
# 创建窗口
frm = MyFrame()
# 显示窗口
frm.Show()
# 让窗口一直显示
app.MainLoop()