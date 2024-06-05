# -------------------- 聊天室-客户端 --------------------
import wx
from socket import *
import threading
from faker import Faker


class Client(wx.Frame):
    def __init__(self):
        # 定义实例属性
        # 姓名 - 通过Faker模块自动生成
        self.name = Faker('zh_CN').name()
        # 是否处于连接状态 - 初始值为False
        self.isConnected = False
        # 客户端的socket - 初始值为None
        self.client_socket = None

        # 界面布局
        # 调用父类方法进行初始化
        wx.Frame.__init__(self, None, title=self.name + "Chatroom Client", size=(450, 660), pos=(100, 50))
        # 创建面板
        self.pl = wx.Panel(self)

        # 创建加入聊天室按钮
        self.conn_btn = wx.Button(self.pl, label='join chatroom', pos=(10, 10), size=(200, 40))
        # 创建退出聊天室按钮
        self.dis_conn_btn = wx.Button(self.pl, label='quit chatroom', pos=(220, 10), size=(200, 40))
        # 创建清空按钮
        self.clear_btn = wx.Button(self.pl, label='clear', pos=(10, 580), size=(200, 40))
        # 创建发送按钮
        self.send_btn = wx.Button(self.pl, label='send', pos=(220, 580), size=(200, 40))
        # 创建聊天记录文本框
        self.text = wx.TextCtrl(self.pl, size=(400, 400), pos=(10, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # 创建输入文本框
        self.input_text = wx.TextCtrl(self.pl, size=(400, 100), pos=(10, 470), style=wx.TE_MULTILINE)
        # 创建定时器
        self.timer = wx.Timer(self)

        # 为清空按钮绑定相应的函数 - clear
        self.Bind(wx.EVT_BUTTON, self.clear, self.clear_btn)
        # 为加入聊天室按钮绑定相应的函数 - connect
        self.Bind(wx.EVT_BUTTON, self.connect, self.conn_btn)
        # 为退出聊天室按钮绑定相应的函数 - dis_connect
        self.Bind(wx.EVT_BUTTON, self.dis_connect, self.dis_conn_btn)
        # 为发送按钮绑定相应的函数 - send
        self.Bind(wx.EVT_BUTTON, self.send, self.send_btn)
        # 绑定定时器
        self.Bind(wx.EVT_TIMER, self.update_ui, self.timer)
        self.timer.Start(1000)

    # 点击join chatroom会触发该函数 (因为在__init__ 方法中我们将他们绑定到了一起)
    def connect(self, event):
        print('connect')
        # 判断一下,如果当前不是处于连接状态 (即未连接)
        if not self.isConnected:
            # 将连接状态改为连接中
            self.isConnected = True
            # 创建一个socket对象并赋值给client_socket
            self.client_socket = socket()
            # 设置socket连接的IP以及端口
            self.client_socket.connect(('127.0.0.1', 8999))
            # 发送用户名
            self.client_socket.send(self.name.encode('utf8'))
            # 实例化一个线程,并执行 此处的target函数指的是线程要执行的函数(即recv_data函数)
            main_thread = threading.Thread(target=self.recv_data)
            # 将该线程设置为守护线程
            main_thread.daemon = True
            # 开启该线程
            main_thread.start()

    # 接收数据函数
    def recv_data(self):
        print('recv_data')
        # 判断如果当前处于连接状态
        while self.isConnected:
            # 等待接收服务器的消息,并使用utf8字符集解码
            text = self.client_socket.recv(1024).decode('utf8')
            # 打印解码后的内容
            print(text)
            # 将接收到的数据添加到聊天记录(文本框)中,并换行
            self.text.AppendText(text + '\n')

    # 断开连接
    def dis_connect(self, event):
        print('dis_conn')
        # 向服务器发送disconnect (服务器接收到disconnect之后会有一些后置的操作)
        self.client_socket.send('disconnect'.encode('utf8'))
        # 将当前连接状态改为False(未连接)
        self.isConnected = False

    # 清空输入栏
    def clear(self, event):
        print('clear')
        # 调用Clear方法清空输入栏
        self.input_text.Clear()

    # 发送
    def send(self, event):
        print('send')
        # 判断当前是否是已连接的状态(我们会发现在很多操作执行的前提就是必须处于连接状态)
        if self.isConnected:
            # 获取输入框中输入的内容
            text = self.input_text.GetValue()
            # 判断输入框的内容是否为空(无法发送空消息)
            if text != '':
                # 给服务端发送 使用utf8编码后的消息
                self.client_socket.send(text.encode('utf8'))
                # 清空输入框(消息发送后自然要清空输入框咯)
                self.input_text.Clear()

    def update_ui(self, event):
        self.text.AppendText('')


def main():
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
