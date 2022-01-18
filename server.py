#!/usr/bin/python3 


import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


localhost = 'local.host'
host = socket.gethostname()
port = 4242

#Host and port and can be used in place of IP
serversocket.bind((host,port))


serversocket.listen(3)

#Start connection to se
while True:
    clientsocket, address = serversocket.accept()

    print("received connection from " %  str(address))

    message = 'Connected to Neo .... Welcome to the matrix + "\r\n" Why do you join us) ' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()

