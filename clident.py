

import socket

# Create a socket for IPv6
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Set the timeout to 5 seconds
client_socket.settimeout(5)

# Connect to the server
s = ( ('2409:4063:4c92:7509:b3c4:fa6d:db6b:550f',  8000))

client_socket.connect(s)

