
from cryptography.fernet import Fernet

# below is the message I am going to encrypt
message = "No one expects the spanish inquisition"

# now to make a key using fernet to encrypt and decrypt the message

key = Fernet.generate_key()

fernet = Fernet(key)

# now to encrypt the message. The string needs to be encoded before it can be encrypted.
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# to decode the message, I use the same Fernet instance of the key
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string ", decMessage)
