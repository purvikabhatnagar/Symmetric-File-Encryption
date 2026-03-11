#Fernet = ready-made strong lock
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("secret.key", "wb") as key_file: #wb = write in binary 
    key_file.write(key) #write(key) = put the key inside the file
    print("Key created")
     