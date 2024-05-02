

# importing some important libraries
from socket import *
import threading

# initializing our socket object
server = socket(AF_INET, SOCK_STREAM)

# host
host = "salman-lenovo"
# port
port = 9999

# binding
server.bind((host, port))

# listening
server.listen()

# clients list
clients = []
# aliases list
aliases = []
# Format
FORMAT = "utf-8"


# broadcast
def broadcast(message) -> None:
    """
    Broadcasts message to all the clients.
    :param message: Message to broadcast.
    :return: None
    """

    # clients list is the list of client sockets
    for client in clients:
        client.send(message.encode(FORMAT))


# handle_client
def handle_client(client) -> None:
    """
    Handles client connection.
    :param client: Client socket connection.
    :return: None
    """

    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            alias = aliases[index]
            aliases.remove(alias)
            # closing connection to the client socket
            client.close()
            broadcast(f"{alias} has disconnected from the chatroom.")
            break


# receive
def receive():
    """
    Receives connection from client.
    :return:
    """

    while True:
        print("Server is Listening...")
        client, address = server.accept()
        print(f"Client with {address} connected.")
        clients.append(client)

        # asking for alias
        client.send(f"alias?\n".encode(FORMAT))

        alias = client.recv(1024).decode(FORMAT)
        aliases.append(alias)
        print(f"The alias of the client {address} is {alias}")
        broadcast(f"{alias} has connected to the chatroom.")
        client.send(f"{alias} you are now connected.".encode(FORMAT))

        # creating thread
        thread = threading.Thread(target=handle_client, args=(client, ))
        thread.start()


receive()
