import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import hashlib
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL

# Initialize global variable
key_hidden = False

# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Function to compute the hash of a message
def compute_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

# Function to toggle showing/hiding the key
def toggle_key_visibility():
    global key_hidden
    key_hidden = not key_hidden
    if key_hidden:
        key_entry.config(show='*')
    else:
        key_entry.config(show='')

# Function to encrypt a message
def encrypt_message():
    message = message_entry.get()  # Get the message from the input field
    if not message:
        messagebox.showerror("Error", "Please enter a message to encrypt.")
        return

    user_key = user_key_entry.get()
    if user_key:
        key = user_key.encode()
        try:
            fernet = Fernet(key)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid key: {str(e)}")
            return
    else:
        key = generate_key()
        fernet = Fernet(key)

    encrypted_message = fernet.encrypt(message.encode())  # Encrypt the message
    message_hash = compute_hash(message)  # Compute the hash of the original message

    # Clear and display the encryption key, encrypted message, and hash
    key_entry.delete(0, tk.END)
    encrypted_message_entry.delete(0, tk.END)
    message_hash_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())
    encrypted_message_entry.insert(0, encrypted_message.decode())
    message_hash_entry.insert(0, message_hash)

    # Hide the key initially
    toggle_key_visibility()

# Function to decrypt a message
def decrypt_message():
    encrypted_message = encrypted_message_entry.get()  # Get the encrypted message
    key = key_entry.get()  # Get the encryption key
    if not encrypted_message or not key:
        messagebox.showerror("Error", "Please enter both the key and the encrypted message.")
        return

    try:
        fernet = Fernet(key.encode())
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()  # Decrypt the message
        decrypted_message_entry.delete(0, tk.END)
        decrypted_message_entry.insert(0, decrypted_message)

        check_integrity()
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")
        integrity_status.set("Integrity Failed")

# Function to check message integrity
def check_integrity():
    decrypted_message = decrypted_message_entry.get()
    received_hash = compute_hash(decrypted_message)  # Compute the hash of the decrypted message
    original_hash = message_hash_entry.get()

    # Check message integrity
    if received_hash == original_hash:
        integrity_status.set("Integrity Successful")
    else:
        integrity_status.set("Integrity Failed")

# Create the main window
root = tk.Tk()
root.title("Cyber Threat Analysis - Encryption and Decryption")

# Load the background image and resize it
background_image = Image.open("C:/Users/aswal/OneDrive/Desktop/py/qw.jpeg")
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label with the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place the widgets (labels, input fields, buttons)
tk.Label(root, text="Message (Sender's End):", bg='white', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10)
message_entry = tk.Entry(root, width=60, font=('Arial', 11))
message_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="User Key (optional, 44 characters):", bg='white', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10)
user_key_entry = tk.Entry(root, width=60, font=('Arial', 11))
user_key_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Encrypt", command=encrypt_message, font=('Arial', 12)).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="Key:", bg='white', font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10)
key_entry = tk.Entry(root, width=60, show='*', font=('Arial', 11))  # Initially show key as asterisks
key_entry.grid(row=3, column=1, padx=10, pady=10)

toggle_button = tk.Button(root, text="Toggle Key Visibility", command=toggle_key_visibility, font=('Arial', 12))
toggle_button.grid(row=3, column=2, padx=10, pady=10)

tk.Label(root, text="Encrypted Message (Opponent's End):", bg='white', font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10)
encrypted_message_entry = tk.Entry(root, width=60, font=('Arial', 11))
encrypted_message_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Original Message Hash:", bg='white', font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10)
message_hash_entry = tk.Entry(root, width=60, font=('Arial', 11))
message_hash_entry.grid(row=5, column=1, padx=10, pady=10)

tk.Button(root, text="Decrypt", command=decrypt_message, font=('Arial', 12)).grid(row=6, column=0, columnspan=2, pady=10)

tk.Label(root, text="Decrypted Message (Receiver's End):", bg='white', font=('Arial', 12)).grid(row=7, column=0, padx=10, pady=10)
decrypted_message_entry = tk.Entry(root, width=60, font=('Arial', 11))
decrypted_message_entry.grid(row=7, column=1, padx=10, pady=10)

tk.Label(root, text="Integrity Status:", bg='white', font=('Arial', 12)).grid(row=8, column=0, padx=10, pady=10)
integrity_status = tk.StringVar()
tk.Label(root, textvariable=integrity_status, bg='white', font=('Arial', 12)).grid(row=8, column=1, padx=10, pady=10)

tk.Button(root, text="Check Integrity", command=check_integrity, font=('Arial', 12)).grid(row=9, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
