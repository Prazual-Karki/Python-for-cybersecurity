
# This script encrypts and decrypts a password using base64 encoding.
# It prompts the user to enter a password, encrypts it, and then gives the option
# to decrypt it back to the original password.
# This is a simple password encryption and decryption script
# It is intended for educational purposes only and should not be used for malicious purposes

import base64


# Function to encrypt a password using base64 encoding
# It takes a password as input, encodes it to bytes, and returns the encoded bytes
def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode("utf-8"))
    return encoded_bytes


# Function to decrypt a password using base64 decoding
# It takes an encoded password as input, decodes it from bytes, and returns the decoded bytes
def decrypt_pass(password):
    decoded_pass = base64.b64decode(password.decode("utf-8"))
    return decoded_pass
    
    

user_pass = input("Enter your password: ")
encrypted_password = encrypt_pass(user_pass)
print(f"your encrypted password is: {encrypted_password.decode("utf-8")}")
decrypt_choice = input("Do you wnat to decrypt it (y/n): ").lower()

# If the user chooses to decrypt, call the decrypt_pass function and print the original password
# If the user chooses not to decrypt, do nothing
if decrypt_choice == "y":
    decrypted_password = decrypt_pass(encrypted_password)
    print(f"your real password is: {decrypted_password.decode("utf-8")}")
    
else:
    pass
    

