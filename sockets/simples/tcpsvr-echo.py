import socket

#HOST = '127.0.0.1'
HOST = '' # anywhere
PORT = 30020

socksvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socksvr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socksvr.bind((HOST,PORT))

socksvr.listen(5)

sockcli, addrcli = socksvr.accept()

print('Connected by',addrcli)

while True:
    data = sockcli.recv(1024)

    if not data:
        break

    print('Received from', addrcli, data)
#    print('Received from', addrcli, data.decode())

    sockcli.sendall(data)

sockcli.close()
socksvr.close()
