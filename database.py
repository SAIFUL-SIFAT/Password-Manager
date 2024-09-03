import json
from cryptography.fernet import Fernet
from encryption import Encryption

class Database:
    def __init__(self, file_name='password.json'):
        self.file_name = file_name
        self.encryption = Encryption()

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                if file.read().strip():  
                    file.seek(0) 
                    data = json.load(file)
                    return data
                else:
                    return {}
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
        
    def save_data(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def add_password(self, service, username, password):
        data = self.load_data() 
        encrypted_password = self.encryption.encrypt(password)
        data[service] = {'username': username, 'password': encrypted_password}
        self.save_data(data)

    def get_password(self, service):
        data = self.load_data()  
        if service in data:
            decrypted_password = self.encryption.decrypt(data[service]['password'])
            return data[service]['username'], decrypted_password
        else:
            return None, None
