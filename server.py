import socket
from security import verify_totp, decrypt_payload
from logger import write_log

HOST = '127.0.0.1'
PORT = 5000

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print("Server started and awaiting authentication requests...")

    while True:
        client_sock, addr = server.accept()
        username = "Unknown" 
        
        try:
            encrypted_data = client_sock.recv(1024)
            if not encrypted_data:
                continue