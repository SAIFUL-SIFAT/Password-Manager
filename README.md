# Password Manager

This is a simple password manager built using Python. It allows users to securely store and retrieve passwords for different services. The project uses encryption to protect stored passwords and features a graphical user interface (GUI) built with Tkinter.

## Features

- **Add Password:** Store a username and password for a service.
- **Retrieve Password:** Retrieve the stored username and password for a service.
- **Encryption:** All passwords are securely encrypted before being stored.
- **Graphical User Interface (GUI):** Simple and user-friendly interface using Tkinter.

## Project Structure

The project consists of the following files:

- `main.py`: Entry point for the application. Initializes and runs the GUI.
- `database.py`: Handles storing, retrieving, and managing encrypted password data.
- `encryption.py`: Handles encryption and decryption of passwords using the `cryptography` library.
- `user_interface.py`: Contains the code for the graphical user interface.

## Installation

### Prerequisites

- Python 3.x
- Pip package manager

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SAIFUL-SIFAT/Password-Manager.git
    cd password-manager
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python main.py
    ```

## Usage

- **Adding a Password:**
  - Click the "Add Password" button.
  - Enter the service name, username, and password.
  - Click "Save" to store the encrypted password.

- **Retrieving a Password:**
  - Click the "Retrieve Password" button.
  - Enter the service name.
  - The username and decrypted password will be displayed in a popup window.

## Technical Details

### Encryption

Passwords are encrypted using the `cryptography` library. The encryption key is stored securely, and the passwords are decrypted only when retrieved.

### Graphical User Interface

The GUI is built using Tkinter, a standard Python interface to the Tk GUI toolkit.




## Acknowledgments

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI toolkit
- [Cryptography](https://cryptography.io/en/latest/) - Python library used for encryption
