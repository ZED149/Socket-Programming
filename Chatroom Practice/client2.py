
# importing some important libraries
from socket import *
import threading

alias = "RT.Awais"

# initializing socket
s = socket(AF_INET, SOCK_STREAM)

# connecting
s.connect(("salman-lenovo", 9999))

def client_receive():
    while True:
        try:
            msg = s.recv(1024).decode("utf-8")
            if msg == "alias?\n":
                s.send(alias.encode("utf-8"))
            else:
                print(msg)
        except:
                print("Error!")
                s.close()
                break


def send():
    while True:
        msg = f"{alias}: {input("")}"
        s.send(msg.encode("utf-8"))


rt = threading.Thread(target=client_receive)
rt.start()
st = threading.Thread(target=send)
st.start()
