# -*- coding: utf-8 -*-
from threading import Thread

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        Thread.__init__(self)
        # Flag to run thread as a deamon
        self.daemon = True
        self.client = client
        self.connection = connection
        super(MessageReceiver, self).__init__()



    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            received_string = self.connection.recv(1024)
            if received_string:
                self.client.receive_message(received_string)

            
        pass
