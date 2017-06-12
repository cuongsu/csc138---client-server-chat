'''
Created on Mar 5, 2016

@authors: Austin Takechi, Cuong Su
This piece of code works with the TCPserver code in order to print an upper case version of text.
The text is sent to the server in the UDPserver code and then the server returns it after converting
it to uppercase. As long as the user does not type 'quit', the code will keep allowing the user to input text.
When the user quits, the server closes automatically.
'''

from socket import *
serverName = '*****'                                     #serverName must be one's own IP
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))                  #connects the socket to the IP and port
sentence = ''
while sentence != 'quit': 
    sentence = input("Input lowercase sentence: ")
    clientSocket.send(sentence.encode('utf-8'))                 #sends message to the server
    modifiedSentence = clientSocket.recv(1024)                  #receives the modified message from the server
    print ("From Server: ", modifiedSentence.decode('utf-8'))   #prints the modified message from the server
clientSocket.close()                                            #closes the socket when user inputs 'quit'
print("The link to the server has been terminated.")