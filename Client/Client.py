'''import socket
import sys


Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ('connecting to %s port %s' % server_address, file=sys.stderr)

Socket = socket.socket(sockets.AF_INET, socket.SOCK_STREAM)
Socket.connect(server_address)
Socket.sendall('Connected')
data = Socket.recv(16)
Socket.close()


try:
    message = 'Lorem Ipusm dolor sit amet.'
    print ( 'sending "%s"' % message)
    Socket.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = Socket.recv(16)
        amount_received += len(data)
        print ('recieved "%s"' % data, file=sys.stderr)

finally:
    print('closing socket', file=sys.stderr)
    Socket.close()'''


import socket
import sys

server_address = ('localhost', 10000,)
data = ''.join(sys.argv[1:])
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    Socket.connect(server_address)
    Socket.sendall (data.encode('utf-8') + '\n'.encode('utf-8'))

    received = Socket.recv(16)

finally:
    Socket.close()

print('Sent: ' + data)
print('Received: ' + received.decode('utf-8'))
