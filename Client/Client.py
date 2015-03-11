# -*- coding: utf-8 -*-
import socket
import json

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
        
        self.host = host
        self.server_port = server_port

        self.run()



        # TODO: Finish init process with necessary code

    def run(self):
        # Initiate the connection to the server
        
        data = raw_input('Skriv kommando: ')



        if data == 'msg':

            data2 = raw_input('Skriv inn melding: ')

            data3 = {'request:':'msg', 'content': data2}

        self.connection.connect((self.host, self.server_port))

        self.send_payload(data3)
    

    def disconnect(self):
        # TODO: Handle disconnection
        self.connection.close()
        pass

    def receive_message(self, message):
        result = json.loads(self.connection.recv(1024))
        print result
        pass

    def send_payload(self, data):
        self.connection.send(json.dumps(data))
        pass


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
