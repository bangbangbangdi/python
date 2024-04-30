import wx
from socket import *
import threading
from faker import Faker

class Client(wx.Frame):
    # 构造方法
    def __init__(self):
        # 实例属性

        self.name =  Faker('zh_CN').name() # 客户端的名字
        self.isConnected = False  # 客户端是否连接服务器
        self.client_socket = None

        # 界面布局
        wx.Frame.__init__(self,None,title=self.name+"聊天室客户端",size=(450,660),pos=(100,50))
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        # 加入聊天室
        self.conn_btn = wx.Button(self.pl,label="加入聊天室",pos=(10,10),size=(200,40))
        # 离开聊天室
        self.dis_conn_btn = wx.Button(self.pl, label="离开聊天室", pos=(220, 10), size=(200, 40))
        # 清空按钮
        self.clear_btn = wx.Button(self.pl, label="清空", pos=(10, 580), size=(200, 40))
        # 发送按钮
        self.send_btn = wx.Button(self.pl, label="发送", pos=(220, 580), size=(200, 40))
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.pl,size=(400,400),pos=(10,60),style=wx.TE_READONLY|wx.TE_MULTILINE)
        # 创建输入文本框
        self.input_text = wx.TextCtrl(self.pl,size=(400,100),pos=(10,470),style=wx.TE_MULTILINE)
        # 按钮的事件绑定
        self.Bind(wx.EVT_BUTTON,self.clear,self.clear_btn)
        self.Bind(wx.EVT_BUTTON, self.conn, self.conn_btn)
        self.Bind(wx.EVT_BUTTON, self.dis_conn, self.dis_conn_btn)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_btn)

    # 点击 加入聊天室 按钮 触发
    def conn(self,event):
        print('conn方法')
        if self.isConnected==False:
            self.isConnected=True
            self.client_socket=socket()
            self.client_socket.connect(('127.0.0.1',8999))
            # 发送用户名
            self.client_socket.send(self.name.encode('utf8'))

            main_thread = threading.Thread(target=self.recv_data)
            main_thread.daemon=True
            main_thread.start()

    def recv_data(self):
        print(22222222222)
        while self.isConnected:
            print(111111111)
            text = self.client_socket.recv(1024).decode('utf8')
            print(text)
            self.text.AppendText(text+'\n')

    # 点击 离开聊天室 按钮 触发
    def dis_conn(self,event):
        print('dis_conn方法')
        self.client_socket.send('断开连接'.encode('utf8'))
        self.isConnected=False


    # 点击 清空 按钮 触发
    def clear(self, event):
        print('clear方法')
        self.input_text.Clear()


    # 点击 发送 按钮 触发
    def send(self, event):
        print('send方法')
        if self.isConnected:
            text = self.input_text.GetValue()
            if text !='':
                self.client_socket.send(text.encode('utf8'))
                self.input_text.Clear()



# 程序入口
if __name__ =='__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建客户端窗口
    client = Client()
    # 显示客户端窗口
    client.Show()
    # 一直循环显示
    app.MainLoop()
