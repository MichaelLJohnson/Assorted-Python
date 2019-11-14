#!/bin/bash python3

"""
Socket Ex1.py

Creator: Darknut82
Date: 24 October 2019

Host: 127.0.0.1 (localhost)
Port: 8000
Description: Example Code on how to use the Module Socket. This goes right along with Socket Notes(.md) and is the first
attempt at writing a Python-based nc service. It opens a connection socket, sends "Hello World" to the connection, and
receives lines of text. Completed.

Changelog:
    24 Oct: Creation. Made base outline without testing. 
    30 Oct: Initial Testing. Didn't Work, until changed message string to a bytes string. Added a server message on successful startup.
        Finished Editing. 
"""

# Import Socket Module (duh)
import socket


## Making a socket 

# Make a socket, this is on the server side.
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attach the socket to an IP and port. Since I am playing around, definitely do NOT use standard ports
hostname = '127.0.0.1' # Using localhost as the IP
port = 8000 # The most similar to 80 with being above 1000
serversock.bind( (hostname, port) ) # I am not sure what .connect does, but it didn't work right.


## Start server-side connection

# okay... my socket is bound to localhost:8000, now listen for ONE connection
serversock.listen(1) 
print("[Alert] Now Listening on {}:{}".format(hostname, port))

# Connection time!
while True:
    # so make a new socket for the person who is connecting (from addr)
    (funBusiness_sock, addr) = serversock.accept()

    # Twofold if statement
    # (1) states that a connection is made and (2) no longer recieves a connection. See Note 1
    if addr is not None:
        print("[Alert] Connection with:", addr)
        break


## Send a message

# Lets send a thing. However, it requires a bytes object, not strings :(
message = bytes("[Server] Hello World!\n", 'utf-8') # make sure to send a new line character, it would look silly without

# Two-part: (1) sends message (2) checks if an error occured. See Note 2
if funBusiness_sock.sendall(message) is None:
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
    byte_data = funBusiness_sock.recv(buffer_size)

    # Display the data. Notice the b'{stuff}' format!
    print("[Client]", byte_data, sep = " ")

    # the byte data will be \0 (called the null byte) if there is a closed connection. Read that as stop.
    if byte_data is b'':
        print("[Alert] Recieved a 0")
        break


## End Statement to make sure we know it is done
print("[Alert] Done with no errors.")

"""
Notes:
1. This is fine as line 40 (serversock.listen(1)) only allows 1 connection. However, this makes all lines after less 
robust (aka not great for extendability). Eventually, the amount of connections made should be variable, and the code
to handle them should also be flexible to handle this. 
2. This set-up is kinda cool (if it works). It will run the send command and also check if the output is correct! 
Coupled with some CLI feedback, this is a good way to check if you are on the right track.
3. Some other notes: the [Thing] notation is to confirm where / who is saying what. Remember that this has three people:
the client (who connects), the host (on port 8000), and the fun business socket (where the host moves the client to). 
For the purposes of the example, and practically, the [Server] is any port from the host.
4. Arguably the most important reminder: this is made for the linux command line. Specifically, if trying to open this
on ANYTHING else, you need to take out the Shebang (line 1). Big Oof on my part to any non-linux people. 
"""