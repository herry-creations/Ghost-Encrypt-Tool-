Ghost-Encrypt-Tool 💀

GhostEncrypt is a Python based GUI tool for encrypting and decrypting sensitive text and passwords to help protect private data

GhostEncrypt 

GhostEncrypt is a Python-based GUI application designed to encrypt and decrypt sensitive text such as passwords and private information. It helps users protect confidential data by converting plain input into an encrypted format that can be restored only with the correct key or password.

Features

- Simple and user-friendly graphical interface.
- Encrypts sensitive text into a secure format.
- Decrypts encrypted text back to its original form.
- Lightweight and easy to run locally.
- Custom application icon support.
- Suitable for academic demonstration and basic privacy use cases.

Purpose

The purpose of GhostEncrypt is to provide a simple desktop-based encryption utility for protecting sensitive data. It demonstrates how encryption can be used to secure passwords or private text from unauthorized access.

How It Works

1. The user enters a password or text into the application.
2. The application processes the input through the encryption logic.
3. The output is transformed into encrypted text.
4. When needed, the same data can be decrypted using the correct key or password.

Installation

1. Clone the repository.
2. Install the required dependencies.
3. Run the application using Python.

```bash
python gui_tool.py
```

Build Executable

To generate a standalone `.exe` file, use PyInstaller:

```bash
pyinstaller --clean --noconfirm --onefile --icon=ghost.ico --name="GhostEncryptZeroTrace" gui_tool.py
```

Usage

- Open the application.
- Enter the text or password you want to encrypt.
- Click Encrypt or Decrypt.
- Copy or save the output.

Security Note

This project is intended for educational and basic privacy purposes. For production-grade security, stronger cryptographic practices and proper key management should be used.

## License

This project is licensed under the MIT License.
