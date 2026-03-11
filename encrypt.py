#takes a normal file, locks it using secret key and save itback in locked form(encrypted)
#So no on ecan read it
from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read() #Taking key into memory
    
fernet = Fernet(key) #Give key to the lock, Fernet know how to lock & unlock

with open("sample.txt", "rb") as file:
    data = file.read() #open file, read content
encrypted_data = fernet.encrypt(data) #function lock the data & encrypted_data = readable text

with open("sample.txt", "wb") as file: #open samea file again to replace content
    file.write(encrypted_data) #write locked data
    
print("File locked")