#import socket module
import socket
import sys # In order to terminate the program


# Prepare a server socket

# Streaming socket in internet domain with TCP protocol
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.connect(("www.example.com", 80))

#create HTTP request, conv to bytes, and send 
request = b"GET / HTTP/1.1\r\nHost:www.example.com\r\nConnection: close\r\n\r\n"
serverSocket.send(request)
sent = 0

while sent < len(request):
    sent = sent + serverSocket.send(request[sent:])

response = b""
while True:
    chunk = serverSocket.recv(4096)

    #0 bytes returned when server terminates connection
    if len(chunk) == 0:
        break
    response = response + chunk


#decode bytes
print(response.decode())

serverSocket.close()

