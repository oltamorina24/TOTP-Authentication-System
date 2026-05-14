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