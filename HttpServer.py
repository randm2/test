'''
Created on Oct 16, 2013

@author: marc

modified from Kurr/Rosse
Python 3.3
'''
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
serverName = gethostname()
print(gethostname())
#Prepare a sever socket

serverSocket.bind((serverName,serverPort))
serverSocket.listen(0)
print ('The server is ready to receive')

while True:
#Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connected')
    try:
            message = connectionSocket.recv(80)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            
            #Send one HTTP header line into socket
            
            connectionSocket.send(b'HTTP/1.0 200 OK\r\n')
            connectionSocket.send(b'Content-Type: text/html\r\n\r\n')
           
            #Send the content of the requested file to the client
            for i in range (0, len(outputdata)):
                connectionSocket.send(bytes(outputdata[i], 'ASCII'))
            connectionSocket.close()
    except IOError:
        #Send response message for file not found
        
        connectionSocket.send(b'404 Not Found')
        
        
        connectionSocket.close()

serverSocket.close() 