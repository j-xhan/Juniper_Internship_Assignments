# client.py  
import socket
import sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get server machine ip and port
host = sys.argv[1]

port = sys.argv[2]

# connection to hostname on the port.
s.connect((host, int(port)))
print("Connected to " + host + " at port " + port + ".")

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
