# server.py 
import socket
import time
import sys

# getting local machine ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
host = s.getsockname()[0]

# create a socket object
serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = socket.gethostbyname(socket.getfqdn())                          

# get port number from command line
port = sys.argv[1]

# bind to the port
serversocket.bind((host, int(port)))
print("Socket bound to " + host + " at port " + port + ".")

# queue up to 5 requests
serversocket.listen(5)
print("Listening...")

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
