#python中的服务器端的程序,其用来测试的客户端程序为：tcpClient1.py
#coding:utf-8

import socket
import threading
def tcplink(sock,addr):
	print('Accept new connection from %s:%s...'%addr)
	sock.send(b'welcome')
	while True:
		date=sock.recv(1024)
		if not date or date.decode('utf-8')=='exit':
			break 
		print(date.decode('utf-8'))	
	
	sock.close()
	print('Connection from %s:%s'%addr)
#第一步：创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#第二步：绑定监听的地址和端口,方法bind()只接收一个tuple
s.bind(('127.0.0.1',9999))
#第三步：调用listen（）方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(10)
#第四步：服务器程序通过一个永久循环来接收来自客户端，accept()会等待并返回一个客户端的连接
while True:
	sock,addr=s.accept()
	#创建一个新线程来处理TCP链接
	threading.Thread(target=tcplink,args=(sock,addr)).start()
	
