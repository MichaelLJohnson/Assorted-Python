#!/bin/bash python3

"""
Socket_Ex2.py

Creator: Darknut82
Date: 14 November 2019 

Host: 127.0.0.1 (localhost)
Port: 8000
Description: Example Code on how to use the Module Socket. This goes right along with Socket Notes(.md) and is the 
second attempt at writing a Python-based nc service. Any double hash / comment delimiters are explicitly for the
tutorial. Any single hash / comment delimiter are final-style comments

It creates a (super)class that will be able to open a socket and send messages. 

Changelog:
    15 Nov: Creation
    19 Nov: Begin Creation of the Client Socket
    17 Dec: Cleaned up code and comments, implemented new commenting formatting.
"""

## First things first, lets make an instance of the class. This ensures you aren't stupid like me and try to run a class
## without any run-able code. It is at the bottom of the file.


class socketCommunicator():
    """
    A Superclass to start a socket server. 

    In Development

    """

    ## This is the constructor. Note it takes the port and host. All we SHOULD have to do is make our Ex1 code in here. 
    ## And I mean literal "ctrl-c, ctrl-v" when I say make the code here, with a few edits.
    def __init__(self, host, port):
        """ Initializes a socket on host:port """
        ## Notice the above line is in a multiline comment. This is for a linter, the thing that pops up how to use the
        ## module when you're typing. Helpful if you use them, and a good way to decribe what the method does. 

        ## Now I have to run through this, line by line, that it works. 
        # Make a server socket
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Store host and port in the object
        self.hostname = host 
        self.port = port 

        # Bind the Socket to the host and port.
        self.serversock.bind( (self.hostname, self.port) ) 

        ## Yes, I have more code. But no, I am not including it. Thats because I want to test the code for SETUP only.
        ## Any further, it would start listening.

    def listen(self, num_connections): 
        """ Sets the socket up as a listener with the specified number of connections. """     
        ## Now that we have a socket already bound, we continue from that point. 

        # socket is bound to self.hostname:self.port, now listen for num_connections amounts.
        ## While I am trying to increase the robust-ness of this code by allowing a more than one connection, this will
        ## be tested later.
        self.serversock.listen(num_connections) 
        print("[Server Alert] Now Listening on {}:{}".format(self.hostname, self.port))

        # Setup Connection Loop. Made for only one connection right now.
        while True:
            # make a new socket for a person who is connecting (from addr)
            (self.funBusiness_sock, addr) = self.serversock.accept()

            # If connected, break out of statement. 
            if addr is not None:
                print("[Server Alert] Connection with:", addr)

                # Run the meaty part of the code
                self.run()

                break

    ## At this point I would expect two questions: What makes this only for one connection and what is the self.run() 
    ## method? Well, the self.run() method I am using to make a modifiable method for the payload. As for the one 
    ## connection restriction, that is because the break out portion is only looking for the first assignment of addr.
    ## Basically, even if you allow for multiple connections, the code will stop after the first. 

    def run(self):
        """ Base method for payload, Overwrite in subclasses. Sends Client a welcome message and recieves client input. 
        Client input is printed on server. """
        
        ## This is our payload section. I have changed it to do as the description says, so this can be used as a test 
        ## in the future. 

        # Send the welcome message
        message = bytes("[Server -> Client] Connected to Server\n", 'utf-8') 

        # Send Message
        if self.funBusiness_sock.sendall(message) is None:
            print("[Server Alert] Message Sent")
        else:
            print("[Server Error] Errors :(")
            raise RuntimeError("Message not sent successfully")

        # Set a buffer size (from Socket Docs)
        buffer_size = 4096 

        # Revieve from Client Loop
        while True:
            # Wait until data is received
            byte_data = self.funBusiness_sock.recv(buffer_size)

            # Check if the connection has been closed
            if byte_data is b'':
                print("[Server Alert] Connection Closed.")
                break

            # Display the data.
            print("[Client -> Server]", byte_data, sep = " ")

            ## Note that the close condition is before displaying the data. This is for ease of use.
    
## All of the "Actually Run" stuff. 
import socket
mySock = socketCommunicator("127.0.0.1", 8000)
mySock.listen(1)