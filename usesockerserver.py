'''
How to use socket
'''
#!/usr/bin/python3
#coding: utf-8

import socket, sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()
    print("addr {}".format(addr))

    msg = 'hello {}'.format(addr)
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

