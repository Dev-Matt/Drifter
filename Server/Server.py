
import socket
import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(16)#.strip()
        current_thread = threading.current_thread()
        response = "{}:    {}".format(current_thread.name, self.data)
        self.request.sendall(self.data.upper())

        print (self.client_address[0]
              + ' sent: ' + self.data.decode('utf-8')
              )


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

    '''def client(ip, port, message):
        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Socket.connect((ip,port))
        try:
            Socket.sendall(message)
            response
        finally:
            Socket.close()'''

    def server_shutdown(self,):
        self.shutdown()
        self.server_close()

if __name__ == '__main__':
    server_address = ('localhost', 10000,)
    print ('Listening on: ' + str(server_address))

    Server = ThreadedTCPServer(server_address, ThreadedTCPRequestHandler,)
    server_thread = threading.Thread(target=Server.serve_forever)
    #erver_thread.daemon = True
    server_thread.start()
