import sqlite3
import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

DB_NAME = "vault.db"
SALT_FILE = "salt.key"

# -------------------- DATABASE --------------------

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password BLOB NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# -------------------- SECURITY --------------------

def load_or_create_salt():
    if not os.path.exists(SALT_FILE):
        with open(SALT_FILE, "wb") as f:
            f.write(os.urandom(16))
    with open(SALT_FILE, "rb") as f:
        return f.read()

def generate_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000
    )
    return base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )

# -------------------- ENCRYPTION --------------------

def encrypt_password(fernet, password):
    return fernet.encrypt(password.encode())

def decrypt_password(fernet, encrypted_password):
    return fernet.decrypt(encrypted_password).decode()

# -------------------- PASSWORD OPERATIONS --------------------

def add_password(fernet):
    website = input("Website name: ")
    username = input("Username: ")
    password = input("Password: ")   # FIXED (input instead of getpass)

    if password.strip() == "":
        print("❌ Password cannot be empty")
        return

    encrypted = encrypt_password(fernet, password)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
        (website, username, encrypted)
    )
    conn.commit()
    conn.close()

    print("✅ Password saved securely")

def view_passwords(fernet):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT website, username, password FROM passwords")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("⚠️ No passwords stored")
        return

    print("\nStored Passwords:")
    print("-" * 40)

    for site, user, enc_pass in rows:
        try:
            password = decrypt_password(fernet, enc_pass)
            print(f"Website: {site}")
            print(f"Username: {user}")
            print(f"Password: {password}")
            print("-" * 40)
        except:
            print("❌ Wrong master password")
            return

# -------------------- MAIN --------------------

def main():
    create_database()

    master_password = input("Enter Master Password: ")   # FIXED
    if master_password.strip() == "":
        print("❌ Master password cannot be empty")
        return

    salt = load_or_create_salt()
    key = generate_key(master_password, salt)
    fernet = Fernet(key)

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_password(fernet)
        elif choice == "2":
            view_passwords(fernet)
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
