# -*- coding: utf-8 -*-
import SocketServer
import json, time

class ClientHandler(SocketServer.BaseRequestHandler):
    
    messages = []
    clients = {}
    deads = []
    
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
            received_string = self.connection.recv(1024).strip()
            if received_string:
                payload = json.loads(received_string)
                print payload
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
        username = payload.get('content')
        while username in self.clients.values():
            username += '_'
        self.clients[self.connection] =  username
        self.send_payload('server', 'info', 'Successfully logged in as %s' % username)
        msg_string = '\n'
        if self.messages:
            for payload in self.messages:
                msg_string += "%s: <%s> %s %s\n" % (payload.get('timestamp'), payload.get('sender'), payload.get('response'), payload.get('content'))
            self.send_payload('server', 'info', msg_string)

    def logged_in(self):
        if not self.connection in self.clients:
            self.send_payload('server', 'error', 'Not logged in. Type help for info.')
            return False
        else:
            return True

    def logout(self,payload):

        if self.logged_in():
            self.send_payload('server', 'info', 'Successfully logged out')
            del self.clients[self.connection]

    def msg(self,payload):

        if self.logged_in():
            username = self.clients[self.connection]
            msg = payload.get('content')
            self.send_payload(username+'\033[0m', 'message', msg)

    def names(self,payload):

        if self.logged_in():
            names = self.clients.values()
            self.send_payload('server', 'info', '\033[0m, '.join(names)+'\033[0m')

    def help(self,payload):

        help_string = '\nlogin <username> - log in with the given username\nlogout - log out\nmsg <message> - send message\nnames - list users in chat\nhelp - view help text'
        self.send_payload('server', 'info', help_string)

    def error(self,payload):

        self.send_payload('server', 'error', 'You did somethin wrong: %s' % payload.get('request'))

    def send_payload(self,sender, response, content):
        payload = {'timestamp'  : time.strftime('%Y-%m-%d %H:%M:%S'),
                    'sender'    : sender,
                    'response'  : response,
                    'content'   : content
        }
        if response == 'message':
            self.messages.append(payload)
            self.broadcast(json.dumps(payload))
        else:
            self.connection.sendall(json.dumps(payload))

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.sendall(message)
            except:
                self.deads.append(client)
        for dead_conn in self.deads:
             del self.clients[dead_conn]


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
