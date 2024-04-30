import socket

# 创建socket对象
sk = socket.socket()
# 连接服务器
sk.connect(("127.0.0.1",8995))

while True:
    send_data = input('请输入你要发送的内容：')
    # 发送数据到服务器
    sk.send(send_data.encode('utf8'))
    # 等待服务器的响应
    accept_data = sk.recv(1024)
    # 打印服务器的响应
    print('接收到服务器的响应：',accept_data.decode('utf8'))

