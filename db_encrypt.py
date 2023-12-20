# Encryption and Decryption

from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a cipher suite
cipher_suite = Fernet(key)

# Encrypt data
data = "some data to be encrypted"
cipher_text = cipher_suite.encrypt(data.encode())

# At this point, we can insert cipher_text into the database

# When retrieving, decrypt the data
plain_text = cipher_suite.decrypt(cipher_text).decode()
print(key)
