#coding:utf-8
#TCP编程的客户端程序
#编写客户端程序与其它语言（例如java）的思路差不多。如下
#第一步：创建一个socket
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#第二步：建立连接，参数是一个tuple，以访问新浪为例
s.connect(('www.sina.com.cn',80))
#第三步：发送数据
s.send(b'GET / HTTP/1.1\r\n Host:www.sina.com.cn\r\nConnection:close\n\r\n')
#第四步：接收数据
buffer=[]
while True:
	d=s.recv(1024)  #recv(max)方法，表示每次只能读取max个字节
	if d:
		buffer.append(d)
	else:
		break
date=b''.join(buffer)

#第五步：关闭连接
#由于接收到的数据包括http头和网页本身，因此将其分开
header,html=date.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
	f.write(html)