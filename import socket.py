import socket


# Create an IPv6 socket
s= socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to a local address
s.bind(('localhost', 8000))


# listen for incoming connections

s.listen(10)
print("waiting------------------- ")
c, addr= s.accept()
print("connected wqith {addr}")



# wait for a connection
done= False
while not done:
  #  print( c, addr)
    m=(c.recv(10244).decode('utf-8'))
    if m== 'stop':
        done= True
    else:

        print(m)
    c.send(input("message:").encode('utf-8'))