
import socket
import threading

HEADER = 1024
PORT = 10000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "exit"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


def send(sock):
    # id = input("Enter your id: ")
    # sock.send(id.encode(FORMAT))
    while True:
        try:
            msg = input("Enter the message: ")
            sock.send(msg.encode("utf-8"))
            if msg == "exit":
                sock.close()
                print("Exiting Client...")
                exit(0)
        except:
            sock.close()
            break


def receive(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == "exit":
                print("Exiting...")
                sock.close()
                exit(0)
        except:
            print("An error occurred. Disconnecting...")
            sock.close()
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 10000))
    print(f"[CONNECTED] Connected to {SERVER}")
    send(client)


# from here
main()
