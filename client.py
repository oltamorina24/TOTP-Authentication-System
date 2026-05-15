import socket
import time
from security import generate_totp, encrypt_payload

HOST = '127.0.0.1'
PORT = 5000
def run_client():
    print("Welcome to TOTP Authentication System.")
    
    while True:
        print("\n" + "-"*30)
        username = input("Enter your username: ")
        
        if username.lower() == 'exit':
            break
        try:
            real_otp = generate_totp(username)
            print(f"(Your 2FA device shows: {real_otp})")
            
            otp_input = input("Enter your TOTP: ")
            payload = f"{username};{otp_input}"
            encrypted_message = encrypt_payload(payload)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(encrypted_message)
                
                response = s.recv(1024).decode()
                print(response)

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    run_client()