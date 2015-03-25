# -*- coding: utf-8 -*-
import socket
import sys, json, time
from MessageReceiver import MessageReceiver

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """
        
        self.host = host
        self.server_port = server_port

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.run()

    def run(self):

        self.connection.connect((self.host, self.server_port))
        message_receiver=MessageReceiver(self,self.connection)
        message_receiver.start()
        
        while True:
            message = raw_input('Enter command \n')
            self.send_payload(message)
            if message == 'logout':
                time.sleep(1)
                break
        self.disconnect()

    def disconnect(self):

        self.connection.close()
        raise SystemExit
        

    def receive_message(self, message):
        payload = json.loads(message)
        print "%s: %s <%s> %s" % (payload.get('timestamp'), payload.get('response'), payload.get('sender'), payload.get('content'))

     

    def send_payload(self, data):
        s = data.split(' ', 1)
        payload = {'request': s[0], 'content': s[1] if len(s) > 1 else None}
        self.connection.send(json.dumps(payload))


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
