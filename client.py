# the python version : Python 3.9.1

from socket import * # imports everything from 'socket'
import sys

serverName = '127.0.0.1' # localhost
serverPort = 12345

try:
 # persistent connection 
 clientSocket = socket(AF_INET, SOCK_STREAM)
 clientSocket.connect((serverName, serverPort)) 

 while True:

   word = input('Input a word:') # word = raw_input('Input a word:')
   clientSocket.send(word.encode())
   response = clientSocket.recv(1024)
   response = response.decode()

   if response == '@':
    break	

   print (word , '==>' , response)

except :
 print ('\nThe Server is Not Running\a\n')
 exit()
        
clientSocket.close()
exit()