

# importing some important libraries
import socket
import threading

# from here
port = 5050
server_ip = "192.168.0.192"
HEADER = 1024
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients_id: dict = {}


def broadcast(message, sender_id):
    for id, client in clients_id.items():
        if id != sender_id:
            try:
                client.send(message)
            except:
                del clients_id[id]


def handler(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    # Prompting new client for an identifier
    conn.send(b'Enter your ID:')
    id = conn.recv(1024).decode().strip()
    clients_id[id] = conn  # Adding the client with its ID

    connected = True
    while connected:
        # msg_length = conn.recv(HEADER).decode("utf-8")
        # if not msg_length:
        #     break
        # msg_length = int(msg_length)

        msg = conn.recv(1024).decode("utf-8")
        if msg == "exit":
            connected = False
        # broadcast(msg, addr[1])
        print(f"[{id}] sent: {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        print("[WAITING] Waiting for connection...")
        client_conn, client_addr = server.accept()
        thread = threading.Thread(target=handler, args=(client_conn, client_addr))
        print(f"[CONNECTED] Client connected {client_addr}")
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


# from here
print("Server is Starting...")
start()
