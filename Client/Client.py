
import socket
import sys

'''  This is a simple TCP client built using
 the python standard library modules .socket and .sys.

 It accepts strings passed as arguements when executing client.py
 in the commandline.

'''

server_address = (162.247.231.201, 10000,)
data = ''.join(sys.argv[1:]) # joins a list of string argumemnts from the command line
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a new socket  with IP4 set for TCP

try:
    Socket.create_connection(server_address) #Creates a new connection to the server_address
    Socket.sendall (data.encode('utf-8') + '\n'.encode('utf-8')) #encodes data to byte string and sends to server_address

    received = Socket.recv(16) # recieves reply from server

finally:
    Socket.close() #closes socket

print('Sent: ' + data)
print('Received: ' + received.decode('utf-8'))
