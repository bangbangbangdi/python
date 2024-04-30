import wx
import random
class MyFrame(wx.Frame):
    # 抽奖列表
    NameList = ['mia','tom','jack']

    # 构造方法
    def __init__(self):
        wx.Frame.__init__(self,None,title='抽奖器',pos=(100,100),size=(400,600))
        # 创建面板
        self.pl = wx.Panel(self,pos=(0,0),size=(400,600))
        # 设置背景颜色
        # self.SetBackgroundColour(wx.BLUE)
        self.SetBackgroundColour((200,0,100))
        # self.SetBackgroundColour('#00FF00')
        self.pl.SetBackgroundColour((180,45,0))
        # 创建静态文本
        self.staticText = wx.StaticText(self.pl,label=random.choice(self.NameList),pos=(0,50),size=(400,400),style=wx.TE_CENTRE)
        # 创建字体
        # 字体大小，字体包，字体风格，加粗
        font = wx.Font(48,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
        # 静态文本设置成我们自己创建的字体
        self.staticText.SetFont(font)
        # 创建按钮
        self.btn1 = wx.Button(self.pl,label='开始抽奖',pos=(100,200))
        self.btn2 = wx.Button(self.pl, label='结束抽奖', pos=(200, 200))
        self.btn1.SetBackgroundColour((0,0,128))
        # 绑定事件
        self.Bind(wx.EVT_BUTTON,self.onClick,self.btn1)
        self.Bind(wx.EVT_BUTTON, self.stop, self.btn2)

    def onClick(self,event):# 抽奖
        # print('click')
        self.timer = wx.Timer(self) #创建了一个定时器
        self.Bind(wx.EVT_TIMER,self.update_name,self.timer)
        self.timer.Start(100) # 每隔100毫秒更新名字

    def update_name(self,event):
        self.staticText.SetLabelText(random.choice(self.NameList))

    def stop(self,event):
        self.timer.Stop()  # 停止计时


if __name__ == "__main__": # python程序主入口
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()
    # 让窗口一直显示
    app.MainLoop()