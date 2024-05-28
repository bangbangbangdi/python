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
