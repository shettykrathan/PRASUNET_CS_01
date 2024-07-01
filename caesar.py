'Task 1: Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm.'
'Allow users to input a message and a shift value to perform encryption and decryption.'

message = input("Enter the message: ").upper()
key = int(input("Enter the encryption key: "))

def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            encrypted += chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        else:
            encrypted += char
    return encrypted
encryption = encrypt(message, key)
print("Encrypted text is:", encryption)

def decrypt(encrypted, key):
    decrypted = ""
    for char in encrypted:
        if char.isalpha():
            decrypted += chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        else:
            decrypted += char
    return decrypted
decryption = decrypt(encryption, key)
print("Decrypted message is:", decryption)
