import tkinter as tk
from tkinter import simpledialog, messagebox
from database import Database

class UserInterface:
    def __init__(self):
        self.database = Database()

    def run(self):
        root = tk.Tk()
        root.geometry("400x250") 
        root.title("Password Manager")
    
        root.eval('tk::PlaceWindow . center')
        
        root.configure(bg='#f0f0f0')  

        button_style = {'font': ('Arial', 12), 'bg': '#4CAF50', 'fg': 'white', 'bd': 0, 'padx': 10, 'pady': 10}
        
        tk.Button(root, text="Add Password", command=self.add_password, **button_style).pack(pady=20)
        tk.Button(root, text="Retrieve Password", command=self.retrieve_password, **button_style).pack()

        root.mainloop()

    def add_password(self):
        service = simpledialog.askstring("Service", "Enter the service name:")
        username = simpledialog.askstring("Username", "Enter the username:")
        password = simpledialog.askstring("Password", "Enter the password:")
        self.database.add_password(service, username, password)
        messagebox.showinfo("Success", f"Password for {service} added successfully.")

    def retrieve_password(self):
        service = simpledialog.askstring("Service", "Enter the service name:")
        username, password = self.database.get_password(service)
        if username and password:
            messagebox.showinfo("Password", f"Username: {username}\nPassword: {password}")
        elif username and password is None:
            messagebox.showwarning("Error", f"Decryption failed for {service}. The data may be corrupted or the key may be incorrect.")
        else:
            messagebox.showwarning("Error", f"No password found for {service}.")


if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
