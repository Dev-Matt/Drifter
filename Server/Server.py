'''import socket
import sys

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ('Starting on port %s port %s' % server_address, file=sys.stderr)


try:
    Socket.bind(server_address)
except socket.error as msg:
    print('Bind Failed. : ' + str(msg[0]) + ' : ' + msg[1])
    sys.exit()


Socket.listen(10)

while True:
    print ('connection pending...', file=sys.stderr)
    connection, client_address = Socket.accept()

try:
    print (client_address + ' connected', file=sys.stderr)


finally:
    Socket.close()'''


import socketserver

server_address = ('localhost', 10000,)


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(16)#.strip()
        print (self.client_address[0]
              + ' sent: ' + self.data.decode('utf-8')
              )
        self.request.sendall(self.data.upper())

if __name__ == '__main__':
    print ('Listening on: ' + str(server_address))
    server_address = ('localhost', 10000,)

Server = socketserver.TCPServer(server_address, TCPHandler,)

Server.serve_forever()
