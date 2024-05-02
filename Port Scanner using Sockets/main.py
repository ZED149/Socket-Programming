

# importing some important libraries
from socket import *
import time
import threading

# starting time
starting_time = time.time()

# in this case, my localhost
target = gethostbyname(gethostname())

print(f"Started scanning at: {starting_time}")
open_ports: dict = {}


def scanner(port: int) -> None:
    """
    Scans a port using sockets.
    :param port: Port to scan
    :return: None
    """

    # initializing socket
    sock = socket(AF_INET, SOCK_STREAM)

    # connecting
    try:
        conn = sock.connect_ex((target, port))
        if conn == 0:
            open_ports[port] = "OPEN"
    except:
        pass

    # closing socket
    sock.close()


threads: [threading.Thread] = []

# scan ports from [1, 9999]
for i in range(1, 10000):
    # creating thread
    thread = threading.Thread(target=scanner, args=(i, ))
    threads.append(thread)

# starting threads
for t in threads:
    t.start()

# joining threads
for t in threads:
    t.join()


# calculating time
end_time = time.time()
print(f"[FINISHED] Time taken is: {end_time - starting_time}")
print("Open ports are:")
print(open_ports)
