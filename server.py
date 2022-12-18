import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #IP and TCP
server.bind(('localhost', 1002)) #1002 is port number
server.listen(2) #starts a loop after which you accept incoming connections

client_socket, client_address = server.accept() #accepts incoming client

file = open('server_image.jpg', "wb") #write binary data to new image
image_chunk = client_socket.recv(2048) #receiving only 2048 bytes at once


while image_chunk:              #loop runs to keep accepting chunks of images
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)


file.close()
client_socket.close()