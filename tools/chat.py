import socket

def start_server():
  
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    h = "127.0.0.1"
    p = 5001

    try:
        b1.bind((h, p))
        b1.listen(1)
        print(f"[*] Chat Server started on {h}:{p}. Waiting for client...")

        conn, addr = b1.accept()
        print(f"[*] Connection from {addr[0]}")

        while True:
            data = conn.recv(1024)
            if not data:
                print("[*] Client disconnected.")
                break

            msg = data.decode()
            print("Client:", msg)

           
            reply = input("You (Server): ")
            conn.send(reply.encode())
            
            if reply.lower() == 'exit':
                break

        conn.close()
    except Exception as e:
        print("Server Error:", e)
    finally:
        b1.close()
        print("[*] Server closed. Returning to Menu...")

