

# importing some important libraries
from socket import *
import threading

PORT = 10000
SERVER = gethostbyname(gethostname())
BUFFER_SIZE = 1024
ADDR = (SERVER, PORT)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(ADDR)


def connect():
    client = socket(AF_INET, SOCK_STREAM)
    try:
        client.connect((SERVER, 5050))
    except ConnectionRefusedError:
        return
    print(f"[CONNECTED] Connected to {SERVER}")
    # send(client)


print("UDP Server Started and listening...")
while True:
    connect()

    bytesAddressPair = udp_socket.recvfrom(BUFFER_SIZE)
    message = bytesAddressPair[0]
    if message.decode() == "exit":
        print("Exiting....")
        exit(1)

    addr = bytesAddressPair[1]
    clientMsg = f"Message from client: {message.decode()}"
    print(clientMsg)

    udp_socket.sendto(clientMsg.encode(), addr)
