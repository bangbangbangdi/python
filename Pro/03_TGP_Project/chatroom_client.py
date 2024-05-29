# -------------------- 聊天室-客户端 --------------------
import wx
from socket import *
import threading
from faker import Faker


class Client(wx.Frame):
    def __init__(self):
        self.name = Faker('zh_CN').name()
        self.isConnected = False
        self.client_socket = None

        wx.Frame.__init__(self, None, title=self.name + "Chatroom Client", size=(450, 660), pos=(100, 50))
        self.pl = wx.Panel(self)

        self.conn_btn = wx.Button(self.pl, label='join chatroom', pos=(10, 10), size=(200, 40))
        self.dis_conn_btn = wx.Button(self.pl, label='quit chatroom', pos=(220, 10), size=(200, 40))
        self.clear_btn = wx.Button(self.pl, label='clear', pos=(10, 580), size=(200, 40))
        self.send_btn = wx.Button(self.pl, label='send', pos=(220, 580), size=(200, 40))
        self.text = wx.TextCtrl(self.pl, size=(400, 400), pos=(10, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.input_text = wx.TextCtrl(self.pl, size=(400, 100), pos=(10, 470), style=wx.TE_MULTILINE)

    def connect(self, event):
        print('connect')
        if not self.isConnected:
            self.isConnected = True
            self.client_socket = socket()
            self.client_socket.connect(('127.0.0.1', 8999))
            # 发送用户名
            self.client_socket.send(self.name.encode('utf8'))

    def recv_data(self):
        print('recv_data')
        while self.isConnected:
            text = self.client_socket.recv(1024).decode('utf8')
            print(text)
            self.text.AppendText(text + '\n')

    def dis_connect(self, event):
        print('dis_conn')
        self.client_socket.send('disconnect'.encode('utf8'))
        self.isConnected = False

    def clear(self, event):
        print('clear')
        self.input_text.Clear()

    def send(self, event):
        print('send')
        if self.isConnected:
            text = self.input_text.GetValue()
            if text != '':
                self.client_socket.send(text.encode('utf8'))
                self.input_text.Clear()


def main():
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
