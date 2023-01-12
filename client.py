

import socket

# Create a socket for IPv6
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Set the timeout to 5 seconds
client_socket.settimeout(5)

# Connect to the server
s = ( ('localhost',  8000))

client_socket.connect(s)

