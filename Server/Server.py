# -*- coding: utf-8 -*-
import SocketServer
import json

class ClientHandler(SocketServer.BaseRequestHandler):
    
    usernames = []
    
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        

        # Loop that listens for messages from the client
        print "Wating input from user..."
        while True:
            received_string = self.connection.recv(1024)
            if received_string:
                payload = json.loads(received_string)
                request = payload.get('request')
                if request == 'login':
                    self.login(payload)
                elif request == 'logout':
                    self.logout(payload)
                elif request == 'msg':
                    self.msg(payload)
                elif request == 'names':
                    self.names(payload)
                elif request == 'help':
                    self.help(payload)
                else:
                    self.error(payload)
            else:
                break

    def login(self,payload):

                username = data2['content']
                self.usernames.append(username)

    def logout(self,payload):

    def msg(self,payload):

    def names(self,payload):

    def help(self,payload):

    def error(self,payload):

    def send_payload(self,payload):
        payload = 


            

            # TODO: Add handling of received payload from client


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
