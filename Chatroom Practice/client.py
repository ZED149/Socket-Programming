

# importing some important libraries
from socket import *
import threading

# initializing client socket
client = socket(AF_INET, SOCK_STREAM)

host = "salman-lenovo"
port = 9999
FORMAT = "utf-8"
alias = "Salman.ZED"
# connecting
client.connect((host, port))


# client receive
def client_receive() -> None:
    """
    Receives message from other clients through the server.
    :return: None
    """
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "alias?\n":
                client.send(alias.encode(FORMAT))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break


# send_client
def send_client():
    while True:
        message = f"{alias}: {input("")}"
        client.send(message.encode(FORMAT))


# starting threads
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
send_thread = threading.Thread(target=send_client)
send_thread.start()
