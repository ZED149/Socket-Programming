
# importing some important libraries
from socket import *
import threading




def main():
    print("[FORWADER] Listening...")
    # listening
    port = 10000
    ADDR = ("localhost", port)
    client = socket(AF_INET, SOCK_STREAM)
    client.bind(ADDR)
    client.listen(5)
    while True:
        client_socket, client_addr = client.accept()
        data = client_socket.recv(1024)
        message = data.decode()
        print(f"[MESSAGE] {message}")
        # connecting to TCP
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("salman-lenovo", 5050))
        client.send(message.encode("utf-8"))


main()
