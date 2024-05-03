

# importing some important libraries
from socket import *
import threading
import time
import sys
import trace

# initializing client socket
client = socket(AF_INET, SOCK_STREAM)

host = "salman-lenovo"
port = 9999
FORMAT = "utf-8"
alias = "Salman"
password = "zed123"
# connecting
client.connect((host, port))
stop_thread = False


# client receive
def client_receive() -> None:
    """
    Receives message from other clients through the server.
    :return: None
    """
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "[SERVER] Client disconnected.\n":
                stop_thread = True
                print("Closing Connection: ")
                continue

            if message == "alias?\n":
                client.send(alias.encode(FORMAT))
                message = client.recv(1024).decode(FORMAT)
                if message == "[SERVER] Password: \n":
                    client.send(password.encode(FORMAT))
                    message = client.recv(1024).decode(FORMAT)
                    if message == "[SERVER] Connection Failed!\n":
                        client.close()
                        print("Connection was refused. Wrong password.")
                        stop_thread = True
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break


# send_client
def send_client():

    while True:
        time.sleep(0.0001)
        if not receive_thread.is_alive():
            break
        if stop_thread:
            client.close()
            break
        message = f"{alias}: {input("")}"
        if message[len(alias) + 2:].startswith("/"):
            if alias == "admin":
                if message[len(alias) + 2].startswith("/kick"):
                    client.send(f"[KICK] {message[len(alias) + 2 + 6:]}".encode(FORMAT))
                elif message[len(alias) + 2].startswith("/ban"):
                    client.send(f"[BAN] {message[len(alias) + 2 + 5:]}".encode(FORMAT))
            else:
                print("Commands can only be executed by an admin!")
        try:
            client.send(message.encode(FORMAT))
        except:
            print(f"{alias}: you are now disconnected.")


# starting threads
threads = []
receive_thread = threading.Thread(target=client_receive)
send_thread = threading.Thread(target=send_client)
threads.append(send_thread)
threads.append(receive_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
