import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    gender = gender_var.get()

    if not username or not password or not email or not gender:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    messagebox.showinfo("Registration Successful",
                        f"Username: {username}\nPassword: {password}\nEmail: {email}\nGender: {gender}")

root = tk.Tk()
root.title("User Registration Form")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

gender_var = tk.StringVar(value="")

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=1, padx=10, pady=5, sticky="e")
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").grid(row=4, column=1, padx=10, pady=5, sticky="w")

register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=5, columnspan=2, pady=10)

root.mainloop()
