'''
Created on Mar 5, 2016

@authors: Austin Takechi, Cuong Su
This piece of code works with the UDPserver code in order to print an upper case version of text.
The text is sent to the server in the UDPserver code and then the server returns it after converting
it to uppercase. As long as the user does not type 'quit', the code will keep allowing the user to input text.
When the user quits, the server closes automatically.
'''

from socket import *
serverName = '*****'                     #must have your own IP address for this
serverPort = 12000                              
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = ''                                    #empty message in order for the user to type in anything they want to be changed
while message != 'quit':                        #while the message isn't 'quit', keep allowing user to input text to be changed
    message = input('Input lower case sentence: ')
    clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))   #send the message to the server to be changed to upper case
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)            #receive the upper case message from the server
    print(modifiedMessage.decode('utf-8'))                                 #prints the received upper case message
clientSocket.close()                            #allow the server to close automatically after the user types in 'quit'
print ("The link to the server has been terminated.") 