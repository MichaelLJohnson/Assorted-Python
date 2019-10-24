#!/bin/bash python3

"""
Socket Ex1.py

Creator: Darknut82
Date: 24 October 2019

Host: 127.0.0.1 (localhost)
Port: 8000
Description: Example Code on how to use the Module Socket. This goes right along with Socket Notes(.md) and is the first
attempt at writing a Python-based nc service. It opens a 1 connection socket, sends "Hello World" to the connection, and
receives the first line of text. Not Complete.

Changelog:
    24 Oct: Creation. Made base outline without testing. 
"""

# Import Socket Module (duh)
import socket


## Making a socket 

# Make a socket, this is on the server side.
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attach the socket to an IP and port. Since I am playing around, definitely do NOT use standard ports
hostname = '127.0.0.1' # Using localhost as the IP
port = 8000 # The most similar to 80 with being above 1000
serversock.connect( (hostname, port) )


## Start server-side connection

# okay... my socket is bound to localhost:8000, now wait for a connection
serversock.listen(1) 

# Connection time!
while True:
    # so make a new socket for the person who is connecting (from addr)
    (funBusiness_sock, addr) = serversock.accept()

    # Twofold if statement
    # (1) states that a connection is made and (2) no longer recieves a connection. See Note 1
    if addr is not None:
        print("Connection with:", addr)
        break


## Send a message

# Lets send a thing
message = "Hello World\n" # make sure to send a new line character, it would look silly without

# Two-part: (1) sends message (2) checks if an error occured. See Note 2
if funBusiness_sock.sendall(message) is None:
    print("Message Sent!")
else:
    print("Errors :(")
    raise RuntimeError("Message not sent successfully")


## Recieving Data:
# I want to see what nc sends back so lets do a thing.

# Set a buffer size (from Socket Docs)
buffer_size = 4096 #Uhh... Ill get to this TODO

# Keep recieving until someone decides to press enter 
while True:
    # Recieve the data (it will be a bytes object)
    byte_data = funBusiness_sock.recv(buffer_size)

    # Display the data TODO I am leaving it in bytes to see what type of data nc sends
    print("nc sent:", byte_data, sep = "\n")
    # TODO Change to a correct strings format

    # TODO break the infinite loop of recieve


# TODO: test bind v. connect
# TODO: make sure line 34 works
# TODO: make sure to explain (and verify) the outputs of all these methods

"""
Notes:
1. This is fine as line 17 (serversock.listen(1)) only allows 1 connection. However, this makes all lines after less 
robust. (aka not great for extendability)
2. This set-up is kinda cool (if it works). It will run the send command and also check if the output is correct! 
Coupled with some CLI feedback, this is a good way to check if you are on the right track.
"""