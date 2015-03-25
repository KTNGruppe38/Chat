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
        self.connection.connect((self.host, self.server_port))
        self.message_receiver=MessageReceiver(self,self.connection)
        self.message_receiver.start()
        
        self.host = host
        self.server_port = server_port

        self.run()

    def run(self):
        
        while True:

            data = raw_input('Skriv kommando: ')

            if data == 'msg':

                data2 = raw_input('Skriv inn melding: ')

                data3 = {'request':'msg', 'content': data2}
            
            elif data == 'login':
                
                username = raw_input('Write in your username: ')
                
                data3 = {'request':'login', 'content': username}
                
            elif data == 'logout':
                
                data3 = {'request':'logout', 'content': None}
                
            elif data == 'help':
                
                data3 = {'request':'help', 'content': None}
                
            elif data == 'names':
                
                data3 = {'request':'names','content': None}
            
            else:
                print("Not a legal request.")
                data3=0


            

            self.send_payload(data3)

    def disconnect(self):

        self.connection.close()
        

    def receive_message(self, message):
        decode_message= json.loads(message)
        
        message = decode_message.get('content') 
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
