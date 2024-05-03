

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
PASSWORD = "zed123"


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
            index = clients.index(client)
            alias = aliases[index]
            if message == f"{alias}: quit":
                client.send("[SERVER] Client disconnected.\n".encode(FORMAT))
                raise Exception
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            alias = aliases[index]
            aliases.remove(alias)
            client.close()
            print(f"[SERVER] {alias} is now disconnected.")
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
        # checking for password
        if alias == "admin":
            # we need to prompt client(admin) for password
            client.send("[SERVER] Password: \n".encode(FORMAT))
            password = client.recv(1024).decode(FORMAT)
            if password != PASSWORD:
                client.send("[SERVER] Connection Failed!\n".encode(FORMAT))
                client.close()
                continue

        aliases.append(alias)
        print(f"The alias of the client {address} is {alias}")
        broadcast(f"{alias} has connected to the chatroom.")
        client.send(f"{alias} you are now connected.".encode(FORMAT))

        # creating thread
        thread = threading.Thread(target=handle_client, args=(client, ))
        thread.start()


receive()
