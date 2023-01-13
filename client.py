

import socket

# Create a socket for IPv6
client= socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Set the timeout to 5 seconds
client.settimeout(5)

# Connect to the server
s = ( ('2409:4050:2e9e:73c4:a29:475:d343:e8c6',  8000))


client.connect(s)

done= False
while not done:
client.send(input("message:").encode('utf-8'))
    m=(client.recv(10244).decode('utf-8'))
    if m== 'stop':
        done= True
    else:

        print(m)
