import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #IP and TCP
client.connect(('localhost', 1002)) #1002 is port number

file = open('image.jpg', "rb") #readbinary

image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)


file.close()
client.close()