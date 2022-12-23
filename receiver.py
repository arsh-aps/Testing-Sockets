'''Receives the image'''
#192.168.2.13

import socket
clientSocket = socket.socket()
q = input("Enter IP address of sender: ")
p = int(input("Enter the port number: "))
s = "pythonimage123.png"
print(s)
condition = True
clientSocket.connect((q,p))
f = open(s,"wb")
while condition:
    image = clientSocket.recv(1024)
    if str(image) == "b''":
        condition = False
    f.write(image)