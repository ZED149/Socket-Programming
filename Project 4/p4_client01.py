#
# CSCI351 Project 4
#
import socket
import threading

def receive_messages(sock):
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

def send_messages(sock):
	while True:
		message = input('')
		try:
			sock.send(message.encode('utf-8'))
			if message.lower() == 'exit':
				break
		except:
			print("An error occurred. Disconnecting...")
			sock.close()
			break

def main(server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((server_ip, server_port))
        print("Connected to server")
        # Start the thread for receiving messages
        threading.Thread(target=receive_messages, args=(sock,)).start()
        send_messages(sock)
        
    except Exception as e:
        print(f"Failed to connect to server: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    SERVER_IP = "localhost"  
    SERVER_PORT = 10000  
    main(SERVER_IP, SERVER_PORT)
