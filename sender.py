'''Send the image'''

from tkinter import *
from tkinter import filedialog
import socket

ip = input("IP address: ")
pn = int(input("Port number: "))
serverSocket = socket.socket()
serverSocket.bind((ip,pn))
data = filedialog.askopenfile(initialdir="/")
path = str(data.name)
image = open(path,"rb")
serverSocket.listen(1)
clientConnected = 0
clientConnected,clientAddress = serverSocket.accept()
if clientConnected != 0:
    for i in image:
        clientConnected.send(i)
