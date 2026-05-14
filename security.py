import pyotp
from cryptography.fernet import Fernet
from users import users

ENCRYPTION_KEY = b'7P6p-X9_z8A-v1L9T6Xz_m_L8_Y9Xz-v1L9T6Xz_m_0='
cipher_suite = Fernet(ENCRYPTION_KEY)

def generate_totp(username):
    if username not in users:
        raise Exception("User does not exist in the system!")
  secret = users[username]
  totp = pyotp.TOTP(secret)
  
    return totp.now()



def verify_totp(username, code):
   if username not in users:
        return False
    
     secret = users[username]
     totp = pyotp.TOTP(secret)
     return totp.verify(code, valid_window=1)

  def encrypt_payload(message):
    return cipher_suite.encrypt(message.encode())

  def decrypt_payload(encrypted_message):
    return cipher_suite.decrypt(encrypted_message).decode()
