#coding: utf-8
from socket import *
import sys

serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(10)
print("The server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    response = ''
    try:
        request = connectionSocket.recv(1024)
        request = request.decode()
        print(request)
        request_file = request.split()[1].replace('/', '')
        file = open(request_file, 'rb')
        file_content = file.read()
        response = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.sendall(response.encode())
        connectionSocket.sendall(file_content)
        connectionSocket.close()

    except Exception:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        file_content = '<h1><center>404 Not Found</center></h1>'
        connectionSocket.sendall(response.encode())
        connectionSocket.sendall(file_content.encode())
        connectionSocket.close()


