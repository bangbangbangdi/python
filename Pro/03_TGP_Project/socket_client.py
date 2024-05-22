# -------------------- socket-客户端 --------------------
import socket

# 创建socket对象
sock = socket.socket()
# 连接服务器 (了解即可:localhost多数情况下都对应着127.0.0.1; 后面的8995是端口号)
sock.connect(('localhost', 8995))
# sock.connect(("127.0.0.1",8995))

while True:
    send_data = input("Enter to send message: ")

    # 对输入的内容 是使用指定字符集编码(这里指定的字符集是utf8)
    encoded = send_data.encode('utf8')
    # 发送数据到服务器(编码后)
    sock.send(encoded)
    # 等待服务器的响应,此处的1024是指要接收的最大数据量(单位是字节)
    accept_data = sock.recv(1024)
    # 对接收到的服务器响应进行解码
    decoded_data = accept_data.decode('utf8')
    # 打印服务器的响应
    print('Received message: ', decoded_data)
