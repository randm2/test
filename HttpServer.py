'''
Created on Oct 16, 2013

@author: marc
'''
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
serverName = gethostname()
print(gethostname())
#Prepare a sever socket
#Fill in start
serverSocket.bind((serverName,serverPort))
serverSocket.listen(0)
print ('The server is ready to receive')
#Fill in end
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
            #Fill in start #Fill in end
            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send(b'HTTP/1.0 200 OK\r\n')
            connectionSocket.send(b'Content-Type: text/html\r\n\r\n')
            #Fill in end
            #Send the content of the requested file to the client
            for i in range (0, len(outputdata)):
                connectionSocket.send(bytes(outputdata[i], 'ASCII'))
            connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(b'404 Not Found')
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end 
serverSocket.close() 