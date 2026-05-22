import os

STORAGE_FILE = "encrypted_passwords.txt"  # Save file

def password_strength(password):
    score = 0
    checks = []
    if len(password) >= 8: score += 1; checks.append("Length OK")
    else: checks.append("Length weak")
    if any(c.isdigit() for c in password): score += 1; checks.append("Digit OK")
    else: checks.append("No digit")
    if any(c.isupper() for c in password): score += 1; checks.append("Upper OK")
    else: checks.append("No uppercase")
    if any(c in '!@#$%^&*?' for c in password): score += 1; checks.append("Special OK")
    else: checks.append("No special")
    strength = "Strong" if score >= 3 else "Medium" if score >= 2 else "Weak"
    return strength, score, checks

def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else: result += char
    return result

def save_encrypted(pwd, enc, strength):
    with open(STORAGE_FILE, 'a') as f:
        f.write(f"Original: {pwd} | Encrypted: {enc} | Strength: {strength}\n")
    print(f"  ✓ Saved to {STORAGE_FILE}")

def show_saved():
    if os.path.exists(STORAGE_FILE):
        print("\n--- SAVED PASSWORDS ---")
        with open(STORAGE_FILE, 'r') as f:
            print(f.read())
    else:
        print("No passwords saved yet.")

# MAIN TOOL
print("=== HAFIZ'S CYBER-CRYPTO TOOL ===\n")
while True:
    print("1. Add Password (Live Encrypt+Save)")
    print("2. View Saved")
    print("3. Exit")
    choice = input("Choose: ").strip()
    
    if choice == '1':
        pwd = input("Live Password: ")
        strength, score, checks = password_strength(pwd)
        print("\nStrength Check:")
        for c in checks: print(f"  - {c}")
        print(f"Result: **{strength}** ({score}/4)")
        
        if strength == "Weak":
            print("⚠️ Weak! Improve it.")
        
        enc = caesar_encrypt(pwd)
        print(f"Encrypted: **{enc}**")
        save_encrypted(pwd, enc, strength)
    
    elif choice == '2':
        show_saved()
    
    elif choice == '3':
        break
    print()