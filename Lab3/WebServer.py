#coding: utf-8
from socket import *
import sys

#Define connection (socket) parameters
#Address + Port no
#Server would be running on the same host as Client
# change this port number if required
serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', serverPort))

serverSocket.listen(10)
#The serverSocket then goes in the listen state to listen for client connection requests. 

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
        if ('html' in request_file):
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        elif ('png' in request_file):
            response = 'HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n'
        connectionSocket.sendall(response.encode())
        connectionSocket.sendall(file_content)
        connectionSocket.close()

    except Exception:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        file_content = '<h1><center>404 Not Found</center></h1>'
        connectionSocket.sendall(response.encode())
        connectionSocket.sendall(file_content.encode())
        connectionSocket.close()


