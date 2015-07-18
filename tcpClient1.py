#为tcpServer服务器端写一个测试的客户端程序
#coding:utf-8
import socket
#第一步：创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#第二步：建立连接
s.connect(('127.0.0.1',9999))
#第三步：发送数据
s.send(b'hello World!')
#第三步：接收数据
date=s.recv(1024)
print(date.decode('utf-8'))

