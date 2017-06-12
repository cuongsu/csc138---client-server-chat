'''
Created on Mar 5, 2016

@authors: Austin Takechi, Cuong Su
This piece of code works with the UDPclient code in order to print an upper case version of text.
This code allows the user to communicate with the client by receiving the text sent by the user and
converting it from lower case to upper case.
'''

from socket import *                            
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
message = ''.encode('utf-8')
while message.decode('utf-8') != 'quit':                        #as long as the received message is not 'quit', the chunk of code will run
    message, clientAddress = serverSocket.recvfrom(2048)        #receives the lower case message from the client
    modifiedMessage = message.upper()                           #changes the received message to upper case
    serverSocket.sendto(modifiedMessage, clientAddress)         #sends the modified text back to the client
serverSocket.close()                                            #closes the server
print("The server has been terminated.")                        #prints after user has entered 'quit'