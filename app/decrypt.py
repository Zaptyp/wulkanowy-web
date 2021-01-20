import json
from cryptography.fernet import Fernet

def decrypt_cookies(s, key):
    s = bytes(s, 'utf-8')
    key = Fernet(key)
    s = key.decrypt(s)
    s = json.loads(s.decode('utf-8'))
    return s