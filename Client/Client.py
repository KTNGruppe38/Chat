# -*- coding: utf-8 -*-
import socket
import json
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
        self.MessageReceiver.MessageReceiver(self,self.connection)
        
        self.host = host
        self.server_port = server_port

        self.run()



        # TODO: Finish init process with necessary code

    def run(self):
        # Initiate the connection to the server

        self.connection.connect((self.host, self.server_port))
        
        while True:

            data = raw_input('Skriv kommando: ')

            if data == 'msg':

                data2 = raw_input('Skriv inn melding: ')

                data3 = {'request':'msg', 'content': data2}
            
            elif data == 'login':
                
                brukernavn = raw_input('Skriv inn ditt brukernavn: ')
                
                data3 = {'request':'login', 'content': brukernavn}
                
            elif data == 'logout':
                
                data3 = {'request':'logout', 'content': None}
                
            elif data == 'help':
                
                data3 = {'request':'help', 'content': None}
                
            elif data == 'names':
                
                data3 = {'request':'names','content': None}
            
            else:
                print("Not a legal request.")


            

            self.send_payload(data3)

    def disconnect(self):
        # TODO: Handle disconnection
        self.connection.close()
        

    def receive_message(self, message):
        print message
     

    def send_payload(self, data):
        self.connection.send(json.dumps(data))


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
