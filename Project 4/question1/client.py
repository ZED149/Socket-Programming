
import socket

HEADER = 1024
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "exit"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


def send(sock):
    id = input("Enter your id: ")
    sock.send(id.encode(FORMAT))
    while True:
        try:
            msg = input("Enter the message: ")
            sock.send(msg.encode("utf-8"))
        except:
            sock.close()
            break


def receive(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                print("Disconnected from server")
                break
        except:
            print("An error occurred. Disconnecting...")
            sock.close()
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Connected to {SERVER}")
    send(client)


# from here
main()
