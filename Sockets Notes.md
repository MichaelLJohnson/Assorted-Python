# Socket Notes
### Darknut82
Most of this information is from around the web, and I do not own it. Maybe I'll cite sources later?

#### What is a "socket"
TBD. I have no clue? I think it is kinda like a port opening at a low level

#### Types of sockets
* INET - IPv4 Sockets (super common)

#### Types of Connections
* STREAM - TCP

#### How to actually use this module
``` python
# Import the socket module
import socket

# Make an IPv4 STREAM Socket (object)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Link it to a port
sock.connect( (url_string, port_num) )
```