# 🔹 README.md for Your Project

````markdown
# Python Password Manager 🔐

A simple yet secure **Python-based password manager** that encrypts and stores your passwords safely in a SQLite database.  
This project demonstrates **encryption, security, and database handling** in a practical application.  

---

## 🚀 Features

- Secure **AES (Fernet) encryption** for all stored passwords  
- Master password authentication for access control  
- Passwords stored in **SQLite database** (`vault.db`)  
- User-friendly **terminal interface**  
- Works on **Windows, Linux, and macOS**  
- Prevents empty inputs and ensures secure password storage  

---

## 🛠️ Requirements

- Python 3.10+  
- `cryptography` library  
- `sqlite3` (comes pre-installed with Python)  

### Install dependencies:
```bash
pip install cryptography
````

---

## 📂 Installation

1. Clone the repository:

```bash
git clone https://github.com/Jiban0507/<YourRepoName>.git
```

2. Navigate to the project folder:

```bash
cd <YourRepoName>
```

3. Run the program:

```bash
python Password.py
```

---

## 📝 How to Use

1. **Enter a master password** (used to encrypt/decrypt your vault).

2. Select an option from the menu:

```
1. Add Password
2. View Passwords
3. Exit
```

3. **Add Password**:

   * Enter website, username, and password
   * Password will be **securely encrypted** and stored in `vault.db`

4. **View Passwords**:

   * Displays all stored credentials decrypted using the master password

5. **Exit**:

   * Close the program securely

---

## 🔧 Testing

* Tested on **VS Code Terminal** and **PowerShell**
* Compatible with Python 3.11, 3.12, 3.13
* Verified that passwords are stored encrypted in `vault.db`
* Empty inputs are blocked and user-friendly messages are displayed

---

## 🧰 Technologies Used

* Python 3.x
* SQLite for database
* `cryptography` library (Fernet AES encryption)
* Terminal-based user interface

---

## ⚠️ Notes

* **Do not delete `vault.db` or `salt.key`**; they are required to decrypt saved passwords
* Always remember your **master password**, otherwise stored passwords cannot be recovered

---

## 🌟 Future Enhancements

* Add **search by website** feature
* Implement **GUI version using Tkinter**
* Add **password strength checker**
* Add **master password change functionality**

---

## 👤 Author

**Name:** Jiban Maji


**GitHub:** [https://github.com/Jiban0507](https://github.com/Jiban0507)
