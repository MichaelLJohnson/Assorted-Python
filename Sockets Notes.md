# Socket Notes
### Darknut82
Most of this information is from around the web, and I do not own it. Maybe I'll cite sources later?  
For reference when talking about the concept of sockets, I will leave it as **s**ockets. When refering to the Python module, I will use **S**ockets.

#### What is a "socket"
TBD. I have no clue? I think it is kinda like a port opening at a low level

#### Types of sockets
* INET - IPv4 Sockets (super common)

#### Types of Connections
* STREAM - TCP

#### How does sockets work?
A small bit of networking background first (I know, eww / oh please no). Consider connecting to a website from your browser. When connecting from a client (e.g. your computer), the client opens a port to connect to the server (website) on port 80 (standard http port number), then proceeds to forward you to a different port to communicate and do other fun business.  

Sockets works a lot like this. The sockets made in Sockets can work as all three ports in the above example: the client who reaches out to the server, the server who is on a known port and forwards the client to another port, and the other port to do the fun business. 

#### How to actually use this module
``` python
# Import the Socket module
import socket

# Make an IPv4 STREAM socket (object)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# CLIENT SIDE
# Requests the data from the url (typical website get request) and is destroyed
sock.connect( (url_string, port_num) )

# SERVER SIDE
# Binds the host and port number to the socket object
sock.bind( (host_string, port_num) )
# Its worth noting that if host_string is 'localhost' or '127.0.0.1' it is only accessible on your system

# Listen and allow up to max_num people to connect (usually max_num = 5)
sock.listen(max_num)

# Run the server (while true is so it just keeps going)
while True:
    # Accept connections
    (cilentsocket, address) = sock.accept()
```