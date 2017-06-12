'''
Created on Mar 5, 2016

@authors: Austin Takechi, Cuong Su
This piece of code works with the TCPclient code in order to print an upper case version of text.
This code allows the user to communicate with the client by receiving the text sent by the user and
converting it from lower case to upper case.
'''

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)                                  #there can only be one connection pending on the socket
print ("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()          #allows the socket through to the address
sentence = ''
while sentence != 'quit':
    sentence = connectionSocket.recv(1024)              #receive the message sent by the client
    capitalizedSentence = sentence.upper()              #changes the message to uppercase
    connectionSocket.send(capitalizedSentence)          #sends the message back to the client
    sentence = sentence.decode('utf-8')    
connectionSocket.close()                                #closes the socket when user inputs 'quit'
print("The server has been terminated.") 