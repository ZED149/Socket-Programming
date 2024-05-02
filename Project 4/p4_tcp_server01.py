#
# CSCI351 Project 4
#
from socket import *
import threading 
import sys

PORT = 10000  
clients = {}

def broadcast_message(message, sender_id):
    for id, client in clients.items():
        if id != sender_id:
            try:
                client.send(message)
            except:
                # Removing the client if it's no longer connected
                del clients[id]

def handler(clientsock, addr):
    # Prompting new client for an identifier
    clientsock.send(b'Enter your ID:')
    id = clientsock.recv(1024).decode().strip()
    clients[id] = clientsock  # Adding the client with its ID
    
    while True:
        try:
            data = clientsock.recv(1024)
            if not data: 
                break
            sys.stderr.write(f'{id} sent "{data.decode()}"\n')
            
            # Broadcasting received message to other clients, including sender's ID
            message = f"{id}: {data.decode()}".encode()
            broadcast_message(message, id)
            if "exit" == data.decode().strip().lower():
                break
        except ConnectionResetError:
            break  

    # Removing the client on disconnect
    del clients[id]
    clientsock.close()
    sys.stderr.write(f"Closed connection with {id}\n")

def start_server():
    server_address = ('localhost', PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(server_address)
    sys.stderr.write('Server starting up\n')

    serversock.listen(5)  # Listening for up to 5 clients
    while True:
        sys.stderr.write('Waiting for connection...\n')
        clientsock, client_address = serversock.accept()
        sys.stderr.write(f'Client connected: {client_address}\n')
        x = threading.Thread(target=handler, args=(clientsock, client_address,))
        x.start()

start_server()
