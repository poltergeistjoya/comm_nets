# This script is running the process which is a webserver

import socket

HOST = '127.0.0.1' #localhost
PORT = 8000

#create socket on internet domain with TCP
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(1)

print('Server running on port ', PORT)

while True:
    #connect to client, get client address
    connection, client = socket.accept()

    #listen for requests
    request = connection.recv(4096).decode('utf-8')
    print(request)
    request_pieces = request.split("\n")
    main_req = request_pieces[0]
    main_pieces = main_req.split(" ")
    req_file = main_pieces[1]

    if req_file == "/":
        req_file = 'index.html'
    else:
        req_file = (main_pieces[1]).lstrip("/") 
    
    print(req_file)

    try: 
        #open file to read in byte format
        file = open(req_file, 'rb')
        response = file.read()
        file.close()

        #success header
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'

    except:
        #404 not found
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')

    print(header)
    final_response = header.encode('utf-8')
    final_response += response
    connection.send(final_response)
    connection.close()