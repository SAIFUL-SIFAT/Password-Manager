from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key_file='encryption.key'):
        self.key_file = key_file
        self.cipher = self.load_or_generate_key()

    def load_or_generate_key(self):
        try:
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        return Fernet(key)

    def encrypt(self, plaintext):
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        try:
            return self.cipher.decrypt(ciphertext.encode()).decode()
        except Exception as e:
            print(f"Decryption failed: {e}")
            return None
