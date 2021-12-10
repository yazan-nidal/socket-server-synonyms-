# the python version : Python 3.9.1 

 #[some code here ]
from _thread import *
import threading # use for multi-threaded
import os.path # use for check file exist
from socket import * # imports everything from 'socket'
import socket
import sys

class ServeClient(threading.Thread):
 def __init__(self, conn, addrs): #def __init__(self, conn, (ip, port)):
  threading.Thread.__init__(self)

  #self.ip = ip
  #self.port = port

   #[add code here ]
  self.conn = conn
  self.addrs = addrs

 def run (self) :
   #stop this client connection
  def stop() :
   self.running = False
   self.conn.close()

  while True:
    #[ add code here ]
    # receive word
   data = self.conn.recv(1024)
   cmd = data.decode()
   print ('The received word from Client',self.addrs,': ',cmd)   

   if cmd == '@':
     #[add code here ]
    cmd = '@'
    self.conn.send(cmd.encode())
    break

   if cmd in engDict: #if engDict.has_key(cmd):
     #[add code here ]
    cmd = engDict[cmd]
    print ('The Response word from server: ',cmd,'\n')
    self.conn.send(cmd.encode())

   else:
     #[add code here ]
    cmd = '<this word does not have a synonym>'
    print ('The Response word from server: ',cmd,'\n')
    self.conn.send(cmd.encode())

   #[add code here ]
  stop()
  print ('The Client',self.addrs,': has Stopped \a \n')
  exit()
 
 #[add code here ]
 # check file exist
file = 'C:/Users/yazan/Desktop/dictionary.txt'
if not os.path.isfile(file):
    print ('\nfile is not exist\a\n')
    exit()

engDict = {} # empty dictionary object
with open(file) as f: # open the file 
 for line in f: 
   tok = line.split()
   engDict[tok[0]] = tok[1]
#print(engDict)

serverName = socket.gethostname() 
serverPort = 12345
 #[add code here]
serverSocket = socket.socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 #[add code here ]
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('\nServer ready to recieve \n') # print 'Server ready to recieve '

threads = []
while True:
 #[ add code here ]
 connectionSocket, addr = serverSocket.accept() # persistent connection
 newThread = ServeClient(connectionSocket, addr)
  #[ add code here ]
 newThread.start()
 
for t in threads:
 t.join()

#def close_():
    ##serverSocket.shutdown(socket.SHUT_RDWR)
    #serverSocket.close()

#close_()
#print ("\n\nserver closed\a\n")
#sys.exit(0) 