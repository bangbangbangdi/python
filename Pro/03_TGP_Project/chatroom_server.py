# -------------------- 聊天室-服务端 --------------------
import wx
from socket import *
import threading
from concurrent.futures import ThreadPoolExecutor


class Server(wx.Frame):
    def __init__(self):
        # 定义Server对象有哪些属性
        # 服务器的启动状态
        self.isOn = False
        # 创建socket对象
        self.server_socket = socket()
        # 给刚刚创建出来的socket绑定ip和端口号 (注意这里并没有定义新的属性, 定义新属性要是这种格式 self.xxx = ? )
        self.server_socket.bind(('0.0.0.0', 8999))
        # 给socket设置监听 (了解:这里的5表示最大的排队数量)
        self.server_socket.listen(5)
        # 保存所有的客户端
        self.client_thread_dict = {}
        # 创建线程池
        self.pool = ThreadPoolExecutor(max_workers=10)

        # 界面布局 调用父类__init__方法设置窗口名,位置,大小
        wx.Frame.__init__(self, None, title="Chatroom Server", pos=(0, 50), size=(450, 600))
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        # 启动服务器按钮
        self.start_btn = wx.Button(self.pl, pos=(10, 10), size=(200, 40), label='start_server')
        # 保存聊天记录按钮
        self.save_btn = wx.Button(self.pl, pos=(220, 10), size=(200, 40), label='save_chat_history')
        # 聊天内容文本框
        self.text = wx.TextCtrl(self.pl, pos=(10, 60), size=(400, 400), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # 给按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.start_server, self.start_btn)
        self.Bind(wx.EVT_BUTTON, self.save_text, self.save_btn)

    def start_server(self, event):
        if not self.isOn:
            self.isOn = True
            main_thread = threading.Thread(target=self.main_thread_fun)
            main_thread.daemon = True
            main_thread.start()

    def main_thread_fun(self):
        while self.isOn:
            client_socket, client_addr = self.server_socket.accept()
            print(client_addr)
            accept_data = client_socket.recv(1024)
            client_name = accept_data.decode('utf8')
            print(client_name)
            # 创建与客户端保持通信的线程
            client_thread = ClientThread(client_socket, client_name, self)
            self.client_thread_dict[client_name] = client_thread
            self.pool.submit(client_thread.run)
            self.send(f'[server msg] welcome {client_name}')

    def send(self, text):
        self.text.AppendText(text + '\n')
        for client in self.client_thread_dict.values():
            if client.isOn:
                encode = text.encode('utf8')
                client.client_socket.send(encode)

    def save_text(self, event):
        print('save text')
        record = self.text.GetValue()
        with open('record.log', 'a+', encoding='utf-8') as f:
            f.write(record)


class ClientThread(threading.Thread):
    def __init__(self, socket, name, server):
        threading.Thread.__init__(self)
        self.client_socket = socket
        self.client_name = name
        self.server = server
        self.isOn = True

    def run(self):
        while self.isOn:
            text = self.client_socket.recv(1024).decode('utf8')
            if text == 'disconnect':
                self.isOn = False
                self.server.send(f'[server msg] {self.client_name} quiet')
            else:
                self.server.send(f'[{self.client_name}]{text}')
        self.client_socket.close()


def main():
    # 创建应用程序对象
    app = wx.App()
    # 创建服务器窗口
    server = Server()
    # 显示服务器窗口
    server.Show()
    # 循环显示
    app.MainLoop()


if __name__ == '__main__':
    main()
