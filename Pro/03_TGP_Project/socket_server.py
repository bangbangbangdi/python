# -------------------- socket-服务器 --------------------
import socket

# 创建socket对象
sock = socket.socket()
# 绑定ip和端口号
sock.bind(('0.0.0.0', 8995))
# 设置监听,这里的5指的是socket的最大排队个数,了解即可(详情参考:https://blog.51cto.com/u_3078781/3288071)
sock.listen(5)
# 等待客户端连接
conn, addr = sock.accept()

# 打印连接信息
print(conn, addr)
while True:
    # 接收客户端的请求内容,最大数据量为1024个字节
    accept_data = conn.recv(1024)
    # 对数据解码
    decoded_data = accept_data.decode('utf-8')
    # 打印解码后的内容
    print('received data:', decoded_data)

    # 设置给客户端响应的内容
    send_data = 'received!'
    # 对响应内容进行编码
    encoded_data = send_data.encode('utf-8')
    # 给客户端返回响应内容
    conn.send(encoded_data)
