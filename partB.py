'''
Created on Mar 5, 2016

@authors: Austin Takechi, Cuong Su
This piece of code allows a person to chat between person A and B. Person A will input a message and that
message will be echoed back to them in upper case. It then switches turns and B will input a message. Again, the message
is echoed back in upper case and the turn switches. This goes on until one of the users inputs 'quit'.

Instructions/How-To-Run: You must open two instances of this program for it to work. In one instance, the person must be A.
In the other instance, the person must be B. Once both are confirmed, the program will begin alternating between the two.
The user must manually enter in responses.
'''

from socket import *
 
serverName = '*****'                                         #should be your own IP
 
yn = input("Are you A? (y/n) ")
if yn == 'y' or yn == 'yes':                                        #Distinguishes between A and B
    id = 1
    print("You are person A.")
else:
    id = -1
    print("You are person B.")
 
serverPort = 12000+id                                               #sets the port two ports apart
clientPort = 12000-id
 
turn = 1;                                                           #A will always input first
 
serverSocket = socket(AF_INET,SOCK_STREAM)                          #set up the server
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

if id == 1: 
    print('A has set up their server socket.')
else:
    print('B has set up their server socket.')
    
ready = False                                                       #waits until both A and B are chosen to start
while ready == False:
    ready = input('Press enter when both server/clients are ready.') == ''
 
clientSocket = socket(AF_INET,SOCK_STREAM)                          #set up the client
clientSocket.connect((serverName,clientPort))
 
if id == 1: 
    print('A has set up their client socket.')
else:
    print('B has set up their client socket.')
 
connectionSocket, addr = serverSocket.accept()
 
sentence = ''
while sentence != 'quit':
    if turn == id:                                                  #if turn == A
        sentence = input("Input lower case statement: ")
        clientSocket.send(sentence.encode('utf-8'))
        modifiedSentence = clientSocket.recv(1024)
        print ('From Server: ', modifiedSentence.decode('utf-8'))
        print("It is now the other person's turn.")
    else:                                                           #if turn == B                                                                
        print("Now waiting for input to come through network.")
        sentence = connectionSocket.recv(1024)
        modifiedSentence = sentence.upper()
        connectionSocket.send(modifiedSentence)
        sentence = sentence.decode('utf-8')
        print('From Client: ', sentence)        
    turn *= -1                                                      #changes turns
    
clientSocket.close()
serverSocket.close()
print('Program has ended.')