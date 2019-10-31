# Socket Notes
### Darknut82

### References
[Sockets Documentation](https://docs.python.org/3/library/socket.html#socket-objects)  
[Sockets Tutorial](https://docs.python.org/3/howto/sockets.html) (It's where most of this has come from tbh)  
[TODO: for the CyberSEED_2019 Geography Remake](https://www.instructables.com/id/Netcat-in-Python/)  

### General
For reference when talking about the concept of sockets, I will leave it as **s**ockets. When refering to the Python module, I will use **S**ockets. My use of this module is going to heavily based and aimed towards creating a server to ask questions via a socket, then recieve and analyze the response from the user. Therefore, keep in mind that this is by no means comprehensive, and will only be expanded based off of the specific usage of the module. Also, most of this information is from around the web, and I do not own it. The examples build off of the Sockets Tutorial reference, but is coded by me. 

### Theory and Information

#### What is a "socket"
TBD. I have no clue? I think it is kinda like a port opening at a low level

#### Types of sockets
* INET - IPv4 Sockets (super common)

#### Types of Connections
* STREAM - TCP

#### How does sockets work?
A small bit of networking background first (I know, eww / oh please no). Consider connecting to a website from your browser. When connecting from a client (e.g. your computer), the client opens a port to connect to the server (website) on port 80 (standard http port number), then proceeds to forward you to a different port to communicate and do other "fun business".  

Sockets works a lot like this. The sockets made in Sockets can work as all three ports in the above example: the client who reaches out to the server, the server who is on a known port and forwards the client to the "fun business" port, and the "fun business"  port. 

### How to actually use this module
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
    # Accept connections and make a new socket to handle a new connection
    (cilentsocket, address) = sock.accept()

    # Create a new thread (kinda like having it do it's own thing off to the side)
    ct = client_thread(clientsocket)
    ct.run # Go play little-thread!
```

### Example 1: How to set up a "listener"
So we have some basics in sockets from the above, right? Now, how _exactly_ do we do this you might ask? Well, buckle up, cause there is a full, working (as of 30 October 2019) example. Some quick caveats to that...  
* The code is written for the linux command line. See note 4 in the example for more on this.  
* The code **only sets up a listener**. It will hang and look like it is doing nothing: this is good. It will only respond to something that connects to it, which I used netcat. Another method would be to setup another socket to act as the client. **The next example should have something in there for it.**  
* Code, as a rule of thumb, should be robust: flexible enough to handle the "stupid" user's inputs and run well if you change an important parameter. This includes putting things like the port and host into a variable instead of hardcoding it in. _If you choose to not heed this advice, expect pain in the next example._
* My comments, much like the voice and tone in this guide, is more or less my lighthearted thought process and is no means the way comment in final products.  
  
#### What is a "listener"?
With that stuff out of the way, we start with "What in the world is a 'listener'". To be circular, a listener listens to what is being sent to the port it is listening to. In more clear terms, the listener will accept what is being sent to the port it is listening on, and have it availible for the server-side to process as needed. This would be the first step to constructing a program to ask questions to an user over the wire: having something to (1) ask questions and (2) recieve the answer. 

#### Important Take-a-ways
First, look at and run through the code. Continue when you have.  
  
Now, I hope it makes sense all the way until line 46. If not, review the "How this module actually works" Section (or let me know that I write bad). I am going to break it down more-or-less line-by-line for important things. 
* Line 49: this exploits the output of the {socket object}.accept() method. This is saying as long as addr is not defined, which is set by the accept method, it will NEVER enter into the if statement. Therefore, if something goes wrong and the client is not given a new socket address, the program will not progress.
* Line 57: I cannot stress this enough, {socket object}.sendall({message}) requires {message} to be a bytes-like object.
* Line 60: This is also like line 48. I am exploiting the fact that the if statement will run the sendall method, then use the result of it to decide if something went wrong. 
* Line 82: This is a thing to know about Socket: if the other person's socket is closed, it will recieve the **null byte**. While not prominent in Python, other languages use it a lot, and it is used here. It is also represented as `0x0` in hex or `\0` in escape characters.  

### Methods
variables that need to be a certain class will be descriptive enough to understand.
  
| Method | Description | 
| :---:  | :----:      |
| socket_module.socket(socket_type, connection_type) | Sets up a socket with given parameters. Does not start or associate a port to the socket. |
| socket_object.connect(host_info) | Attaches a one-time socket (needs verification) to the given host and port. host_info is a tuple of the hostname and port, in that order. |
| socket_oject.bind(host_info) | Attaches a persistent socket (needs verification) to the given host and port. host_info is a tuple of the hostname and port, in that order. |
| socket_object.listen(max_num) | Sets the socket to listen for up to max_num connections. |
| socket_object.accept() | Accepts a new connection from a client. Returns a new socket and the address of the client |

### TODO
* A CTF Socket Class (for the project of a nc CTF) would be cool
* .encode() and .decode()
* .shutdown() and .close()
