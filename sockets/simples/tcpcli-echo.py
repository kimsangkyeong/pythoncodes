import socket

HOST = '127.0.0.1'
PORT = 30020

sockcli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockcli.connect((HOST, PORT))

sockcli.sendall('hello socket world!')

data = sockcli.recv(1024)
#print('Received',repr(data.decode()))
print('Received',data)

sockcli.close()
