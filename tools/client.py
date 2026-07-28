import socket

def start_client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 5001))

    while True:
        msg = input("You (Client): ")  
        c.send(msg.encode())

        if msg.lower() == "exit":
            break

        data = c.recv(2222).decode()
        print("Server:", data)

    c.close()

start_client()