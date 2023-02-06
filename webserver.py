#import socket module
import socket
import sys # In order to terminate the program


# Prepare a server socket
# Streaming socket in internet domain with TCP protocol
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind localhost to port 1024
serverSocket.bind(('', 80))
#queue as may as 5 conenct requests (max)
serverSocket.listen(5)
print("socket is listening")


while True:
    #Establish the connection
    print("Ready to serve... ")
    #accept outside connections
    connectionSocket, addr = serverSocket.accept()

    try:
        #max number of bits to recieve at once
        message = connectionSocket.recv(4096)
        filename = message.split() [1]
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)

        #Send one HTTP header line into socket
        request = b"HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(request)

        #send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(b"\r\n".encode())

        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()

