#!/bin/bash python3

"""
Socket_Ex2.py

Creator: Darknut82
Date: 14 November 2019 

Host: 127.0.0.1 (localhost)
Port: 8000
Description: Example Code on how to use the Module Socket. This goes right along with Socket Notes(.md) and is the 
second attempt at writing a Python-based nc service. 

It creates a (super)class that will be able to open a socket and send messages. 

Changelog:
    15 Nov: Creation
    19 Nov: Begin Creation of the Client Socket
"""

# First things first, lets make an instance of the class. This ensures you aren't studpid like me and try to run a class
# without any run-able code. it will be at the bottom of the file


class socketCommunicator():
    """
    A Superclass to start a socket server. 

    In Development

    """

    # This is the constructor. Note it takes the port and host. All we SHOULD have to do is make our Ex1 code in here. 
    # And I mean literal ctrl-c, ctrl-v  when I say make the code here, with a few edits.
    def __init__(self, host, port):



        # Now I have to run through this, line by line, that it works. 
        # Make a server socket
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # TODO Comment
        self.hostname = host 
        self.port = port 

        # Bind the Socket to the host and port.
        self.serversock.bind( (self.hostname, port) ) 

        ### Yes, I have more code. But no, I am not including it. Thats because I want to test the code for SETUP only.
        ### Any further, it would start listening.

    def listen(self, num_connections):      
        ## Start server-side connection

        # osocket is bound to localhost:8000, now listen for ONE connection
        self.serversock.listen(num_connections) 
        print("[Alert] Now Listening on {}:{}".format(self.hostname, self.port))

        # Setup Connection Loop. Made for only one connection right now.
        while True:
            # make a new socket for a person who is connecting (from addr)
            (self.funBusiness_sock, addr) = self.serversock.accept()

            # If connected, break out of statement. 
            if addr is not None:
                print("[Alert] Connection with:", addr)

                # Run the meaty part of the code
                self.run()

                break

    # Now we need an way to run some code. Using the old code from the example
    def run(self):
        ## Send message

        # Lets send a thing. However, it requires a bytes object, not strings :(
        message = bytes("[Server] Hello World!\n", 'utf-8') # make sure to send a new line character, it would look silly without

        # Two-part: (1) sends message (2) checks if an error occured. See Note 2
        if self.funBusiness_sock.sendall(message) is None:
            print("[Alert] Message Sent!")
        else:
            print("[Error] Errors :(")
            raise RuntimeError("Message not sent successfully")


        ## Recieving Data:
        # I want to see what nc sends back so lets do a thing.

        # Set a buffer size (from Socket Docs)
        buffer_size = 4096 #This should (requires more testing) set the upper limit on how much you can recieve

        # Keep recieving until someone decides to leave
        while True:
            # Recieve the data (it will be a bytes object). This also holds the code until something is recieved. 
            byte_data = self.funBusiness_sock.recv(buffer_size)

            # Display the data. Notice the b'{stuff}' format!
            print("[Client]", byte_data, sep = " ")

            # the byte data will be \0 (called the null byte) if there is a closed connection. Read that as stop.
            if byte_data is b'':
                print("[Alert] Recieved a 0")
                break


        ## End Statement to make sure we know it is done
        print("[Alert] Done with no errors.")
    

import socket
mySock = socketCommunicator("127.0.0.1", 8000)
mySock.listen(1)