import os
# import tkinter as tk
# from tkinter import ttk, messagebox, scrolledtext

# STORAGE_FILE = "encrypted_passwords.txt"

# def password_strength(password):
#     score = 0
#     checks = []
#     if len(password) >= 8:
#         score += 1
#         checks.append("Length OK")
#     else:
#         checks.append("Length weak")
#     if any(c.isdigit() for c in password):
#         score += 1
#         checks.append("Digit OK")
#     else:
#         checks.append("No digit")
#     if any(c.isupper() for c in password):
#         score += 1
#         checks.append("Upper OK")
#     else:
#         checks.append("No uppercase")
#     if any(c in '!@#$%^&*?' for c in password):
#         score += 1
#         checks.append("Special OK")
#     else:
#         checks.append("No special")
#     strength = "Strong" if score >= 3 else "Medium" if score >= 2 else "Weak"
#     return strength, score, checks

# def caesar_encrypt(text, shift=3):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             base = 65 if char.isupper() else 97
#             result += chr((ord(char) - base + shift) % 26 + base)
#         else:
#             result += char
#     return result

# def save_encrypted(pwd, enc, strength):
#     with open(STORAGE_FILE, "a", encoding="utf-8") as f:
#         f.write(f"Original: {pwd} | Encrypted: {enc} | Strength: {strength}\n")

# def show_saved():
#     if os.path.exists(STORAGE_FILE):
#         with open(STORAGE_FILE, "r", encoding="utf-8") as f:
#             return f.read().strip()
#     return "No passwords saved yet."

# def encrypt_now():
#     pwd = entry_pwd.get().strip()
#     if not pwd:
#         messagebox.showwarning("Input Needed", "Please enter a password.")
#         return
#     strength, score, checks = password_strength(pwd)
#     result_box.delete("1.0", tk.END)
#     result_box.insert(tk.END, "Strength Check:\n")
#     for c in checks:
#         result_box.insert(tk.END, f"- {c}\n")
#     result_box.insert(tk.END, f"\nResult: {strength} ({score}/4)\n")
#     if strength == "Weak":
#         proceed = messagebox.askyesno("Weak Password", "The password is weak. Do you still want to encrypt it??")
#         if not proceed:
#             result_box.insert(tk.END, "\nPlease enter a stronger password.\n")
#             return
#     enc = caesar_encrypt(pwd)
#     save_encrypted(pwd, enc, strength)
#     result_box.insert(tk.END, f"\nEncrypted: {enc}\nSaved to {STORAGE_FILE}\n")

# def view_saved():
#     result_box.delete("1.0", tk.END)
#     result_box.insert(tk.END, "--- SAVED ---\n")
#     result_box.insert(tk.END, show_saved() + "\n")

# def clear_all():
#     entry_pwd.delete(0, tk.END)
#     result_box.delete("1.0", tk.END)

# print("Launching GUI...")

# try:
#     root = tk.Tk()
#     root.title("Hafiz Cyber-Crypto Tool")
#     root.geometry("620x480")
#     root.resizable(False, False)

#     style = ttk.Style()
#     style.theme_use("clam")
#     style.configure("TButton", padding=8)

#     main = ttk.Frame(root, padding=16)
#     main.pack(fill="both", expand=True)

#     label_title = ttk.Label(main, text="Hafiz Cyber-Crypto Tool", font=("Arial", 18, "bold"))
#     label_title.pack(pady=(0, 12))

#     frame_input = ttk.Frame(main)
#     frame_input.pack(fill="x", pady=6)

#     lbl = ttk.Label(frame_input, text="Enter Password:")
#     lbl.pack(side="left", padx=(0, 10))
#     entry_pwd = ttk.Entry(frame_input, width=40, show="*")
#     entry_pwd.pack(side="left", padx=(0, 10), fill="x", expand=True)

#     frame_buttons = ttk.Frame(main)
#     frame_buttons.pack(fill="x", pady=10)

#     btn_encrypt = ttk.Button(frame_buttons, text="Encrypt & Save", command=encrypt_now)
#     btn_encrypt.pack(side="left", padx=5)

#     btn_view = ttk.Button(frame_buttons, text="View Saved", command=view_saved)
#     btn_view.pack(side="left", padx=5)

#     btn_clear = ttk.Button(frame_buttons, text="Clear", command=clear_all)
#     btn_clear.pack(side="left", padx=5)

#     result_box = scrolledtext.ScrolledText(main, height=18, wrap=tk.WORD)
#     result_box.pack(fill="both", expand=True, pady=10)
#     result_box.insert(tk.END, "Enter a password, then click Encrypt & Save.\n")

#     print("GUI ready.")
#     root.mainloop()

# except Exception as e:
#     print("GUI error:", e) 

# import os >>>>>>>>>>>>>>>>>without app icon

# import tkinter as tk
# from tkinter import ttk, messagebox, scrolledtext

# STORAGE_FILE = "encrypted_passwords.txt"

# def password_strength(password):
#     score = 0
#     checks = []
#     if len(password) >= 8:
#         score += 1
#         checks.append("Length OK")
#     else:
#         checks.append("Length weak")
#     if any(c.isdigit() for c in password):
#         score += 1
#         checks.append("Digit OK")
#     else:
#         checks.append("No digit")
#     if any(c.isupper() for c in password):
#         score += 1
#         checks.append("Uppercase OK")
#     else:
#         checks.append("No uppercase")
#     if any(c in "!@#$%^&*?+-_=" for c in password):
#         score += 1
#         checks.append("Special character OK")
#     else:
#         checks.append("No special character")
#     strength = "Strong" if score >= 3 else "Medium" if score >= 2 else "Weak"
#     return strength, score, checks

# def caesar_encrypt(text, shift=3):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             base = 65 if char.isupper() else 97
#             result += chr((ord(char) - base + shift) % 26 + base)
#         else:
#             result += char
#     return result

# def save_encrypted(pwd, enc, strength):
#     with open(STORAGE_FILE, "a", encoding="utf-8") as f:
#         f.write(f"Original: {pwd} | Encrypted: {enc} | Strength: {strength}\n")

# def show_saved():
#     if os.path.exists(STORAGE_FILE):
#         with open(STORAGE_FILE, "r", encoding="utf-8") as f:
#             return f.read().strip()
#     return "No passwords saved yet."

# def update_meter(score):
#     meter.delete("all")
#     width = 320
#     filled = int((score / 4) * width)
#     meter.create_rectangle(0, 0, width, 20, fill="#1f2937", outline="")
#     color = "#ef4444" if score <= 1 else "#f59e0b" if score == 2 else "#22c55e"
#     meter.create_rectangle(0, 0, filled, 20, fill=color, outline="")
#     meter.create_text(width // 2, 10, text=f"{score}/4", fill="white", font=("Arial", 10, "bold"))

# def set_status(msg, color="#cbd5e1"):
#     status_var.set(msg)
#     status_label.configure(fg=color)

# def encrypt_now():
#     pwd = entry_pwd.get().strip()
#     if not pwd:
#         messagebox.showwarning("Input Required", "Please enter a password.")
#         return
#     strength, score, checks = password_strength(pwd)
#     update_meter(score)
#     result_box.delete("1.0", tk.END)
#     result_box.insert(tk.END, "Strength Check:\n")
#     for c in checks:
#         result_box.insert(tk.END, f"- {c}\n")
#     result_box.insert(tk.END, f"\nResult: {strength} ({score}/4)\n")
#     if strength == "Weak":
#         proceed = messagebox.askyesno("Weak Password", "The password is weak. Do you still want to encrypt it?")
#         if not proceed:
#             set_status("Encryption cancelled because the password is weak.", "#f59e0b")
#             result_box.insert(tk.END, "\nPlease enter a stronger password.\n")
#             return
#     enc = caesar_encrypt(pwd)
#     save_encrypted(pwd, enc, strength)
#     result_box.insert(tk.END, f"\nEncrypted: {enc}\nSaved to {STORAGE_FILE}\n")
#     set_status(f"Password encrypted successfully. Strength: {strength}", "#22c55e")
#     messagebox.showinfo("Success", "Password encrypted and saved successfully.")

# def view_saved():
#     result_box.delete("1.0", tk.END)
#     result_box.insert(tk.END, "--- SAVED ---\n")
#     result_box.insert(tk.END, show_saved() + "\n")
#     set_status("Saved records loaded.", "#60a5fa")

# def clear_all():
#     entry_pwd.delete(0, tk.END)
#     result_box.delete("1.0", tk.END)
#     meter.delete("all")
#     update_meter(0)
#     set_status("Ready for a new password.", "#cbd5e1")

# def toggle_theme():
#     global dark_mode
#     dark_mode = not dark_mode
#     if dark_mode:
#         root.configure(bg="#020617")
#         main.configure(style="Dark.TFrame")
#         card.configure(style="DarkCard.TFrame")
#         title_label.configure(bg="#020617", fg="#e2e8f0")
#         subtitle_label.configure(bg="#020617", fg="#94a3b8")
#         pwd_label.configure(bg="#0f172a", fg="#e2e8f0")
#         meter_label.configure(bg="#0f172a", fg="#cbd5e1")
#         info_label.configure(bg="#0f172a", fg="#cbd5e1")
#         status_label.configure(bg="#0f172a", fg="#cbd5e1")
#         footer_label.configure(bg="#020617", fg="#64748b")
#         style.configure("TLabel", background="#020617", foreground="#e2e8f0")
#         style.configure("Dark.TFrame", background="#020617")
#         style.configure("DarkCard.TFrame", background="#0f172a")
#     else:
#         root.configure(bg="#e2e8f0")
#         main.configure(style="Light.TFrame")
#         card.configure(style="LightCard.TFrame")
#         title_label.configure(bg="#e2e8f0", fg="#0f172a")
#         subtitle_label.configure(bg="#e2e8f0", fg="#334155")
#         pwd_label.configure(bg="#f8fafc", fg="#0f172a")
#         meter_label.configure(bg="#f8fafc", fg="#334155")
#         info_label.configure(bg="#f8fafc", fg="#475569")
#         status_label.configure(bg="#f8fafc", fg="#475569")
#         footer_label.configure(bg="#e2e8f0", fg="#64748b")
#         style.configure("TLabel", background="#e2e8f0", foreground="#0f172a")
#         style.configure("Light.TFrame", background="#e2e8f0")
#         style.configure("LightCard.TFrame", background="#f8fafc")

# print("Launching GUI...")
# root = tk.Tk()
# root.title("GhostEncrypt ZeroTrace")
# root.geometry("860x620")
# root.minsize(860, 620)
# root.configure(bg="#020617")
# root.option_add("*Font", "Arial 10")
# root.after(100, lambda: (root.deiconify(), root.lift(), root.focus_force(), root.attributes("-topmost", True), root.after(200, lambda: root.attributes("-topmost", False))))

# style = ttk.Style()
# style.theme_use("clam")
# style.configure("TButton", padding=10, font=("Arial", 10, "bold"))
# style.configure("Accent.TButton", background="#2563eb", foreground="white")
# style.map("Accent.TButton", background=[("active", "#1d4ed8")])
# style.configure("Danger.TButton", background="#dc2626", foreground="white")
# style.map("Danger.TButton", background=[("active", "#b91c1c")])
# style.configure("Dark.TFrame", background="#020617")
# style.configure("Light.TFrame", background="#e2e8f0")
# style.configure("DarkCard.TFrame", background="#0f172a")
# style.configure("LightCard.TFrame", background="#f8fafc")

# main = ttk.Frame(root, style="Dark.TFrame", padding=16)
# main.pack(fill="both", expand=True)

# top = ttk.Frame(main, style="Dark.TFrame")
# top.pack(fill="x", pady=(0, 12))

# title_block = ttk.Frame(top, style="Dark.TFrame")
# title_block.pack(side="left", fill="x", expand=True)

# title_label = tk.Label(title_block, text="GhostEncrypt ZeroTrace", font=("Arial", 22, "bold"), bg="#020617", fg="#e2e8f0")
# title_label.pack(anchor="w")
# subtitle_label = tk.Label(title_block, text="Modern password encryption dashboard with live analysis", font=("Arial", 10), bg="#020617", fg="#94a3b8")
# subtitle_label.pack(anchor="w", pady=(2, 0))

# theme_btn = ttk.Button(top, text="Toggle Theme", command=toggle_theme)
# theme_btn.pack(side="right")

# card = ttk.Frame(main, style="DarkCard.TFrame", padding=18)
# card.pack(fill="both", expand=True)

# pwd_label = tk.Label(card, text="Enter Password", font=("Arial", 11, "bold"), bg="#0f172a", fg="#e2e8f0")
# pwd_label.pack(anchor="w")

# entry_pwd = ttk.Entry(card, show="*", font=("Arial", 12))
# entry_pwd.pack(fill="x", pady=(8, 12))

# meter_label = tk.Label(card, text="Strength Meter", font=("Arial", 10, "bold"), bg="#0f172a", fg="#cbd5e1")
# meter_label.pack(anchor="w")
# meter = tk.Canvas(card, width=320, height=20, highlightthickness=0, bg="#0f172a")
# meter.pack(anchor="w", pady=(6, 12))

# buttons = ttk.Frame(card, style="DarkCard.TFrame")
# buttons.pack(fill="x", pady=(2, 12))

# btn_encrypt = ttk.Button(buttons, text="Encrypt & Save", style="Accent.TButton", command=encrypt_now)
# btn_encrypt.pack(side="left", padx=(0, 8))

# btn_view = ttk.Button(buttons, text="View Saved", command=view_saved)
# btn_view.pack(side="left", padx=8)

# btn_clear = ttk.Button(buttons, text="Clear", style="Danger.TButton", command=clear_all)
# btn_clear.pack(side="left", padx=8)

# info_label = tk.Label(card, text="Tip: Use 8+ characters, uppercase letters, digits, and special symbols.", font=("Arial", 9), bg="#0f172a", fg="#cbd5e1")
# info_label.pack(anchor="w", pady=(0, 8))

# status_var = tk.StringVar(value="Ready. Enter a password to begin.")
# status_label = tk.Label(card, textvariable=status_var, font=("Arial", 10, "italic"), bg="#0f172a", fg="#cbd5e1")
# status_label.pack(anchor="w", pady=(0, 8))

# result_box = scrolledtext.ScrolledText(card, height=18, wrap=tk.WORD, font=("Courier New", 11), bg="#020617", fg="#e2e8f0", insertbackground="white", relief="flat")
# result_box.pack(fill="both", expand=True)
# result_box.insert(tk.END, "Enter a password, then click Encrypt & Save.\n")

# footer = ttk.Frame(main, style="Dark.TFrame")
# footer.pack(fill="x", pady=(10, 0))
# footer_label = tk.Label(footer, text="Project mode: GUI + encryption + local save", font=("Arial", 9), bg="#020617", fg="#64748b")
# footer_label.pack(anchor="e")

# update_meter(0)
# print("GUI ready.")
# root.mainloop()