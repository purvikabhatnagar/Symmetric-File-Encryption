#Unlock and org text comes back
from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

with open("sample.txt", "rb") as file:
    encrypted_data = file.read()

decrypted = fernet.decrypt(encrypted_data)

with open("sample.txt", "wb") as file:
    file.write(decrypted)

print("File decrypted")