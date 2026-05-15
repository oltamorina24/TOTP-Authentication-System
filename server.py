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
            decrypted_data = decrypt_payload(encrypted_data)
            username, otp = decrypted_data.split(";")
            
            print(f"\nReceived authentication request for user: {username}")
            print(f"TOTP provided: {otp}")
            if verify_totp(username, otp):
                print(f"Authentication successful for user: {username}")
                response = "Authentication successful. You now have access to the system."
                write_log(username, "SUCCESS") 
            else:
                print(f"Authentication failed for user: {username}")
                response = "Authentication failed. Invalid or expired code."
                write_log(username, "FAILED") 
            client_sock.send(response.encode())
            
        except Exception as e:
            print(f"Error processing request for {username}: {e}")
        finally:
            client_sock.close()
            print(f"Connection closed for {username}. Waiting for next request...")
            print("-" * 40)

if __name__ == "__main__":
    start_server()