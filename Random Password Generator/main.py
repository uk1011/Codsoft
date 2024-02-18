import random
import tkinter as tk
from tkinter import ttk
import pyperclip 
from ttkbootstrap import Style  

def generate_password():
    password_length = length.get()
    generated_password = "".join(random.sample(characters, int(password_length)))
    password.set(generated_password)

def copy_password():
    pyperclip.copy(password.get())

def reset_form():
    username.set("")
    length.set("")
    password.set("")


style = Style(theme='minty') 
root = style.master

root.title("Random Password Generator")
root.geometry("380x420") 
root.iconbitmap("password.ico")

# define set of character to use for generating random password
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*_-=+"
characters = alphabets + numbers + special_characters


# label for the app name
label = ttk.Label(master=root, text="Random Password Generator", font="Arial 16 bold")
label.grid(row=0, column=0, columnspan=2, pady=10)

# user details (label and entry)
username_label = ttk.Label(root, text="Username:", font="Arial 12")
username_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
username = tk.StringVar()
username_entry = ttk.Entry(root, textvariable=username, font="Arial 12")
username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# password length label and entry field
length_label = ttk.Label(root, text="Password Length:", font="Arial 12")
length_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
length = tk.StringVar()
password_length_entry = ttk.Entry(root, textvariable=length, font="Arial 12")
password_length_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# password generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# label to show text generated password
output_label = ttk.Label(root, text="Generated Password", font="Arial 12")
output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# display the random generated password using label
password = tk.StringVar()
password_label = ttk.Label(root, textvariable=password, font="Arial 12")
password_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# button used to generate another password 
generate_another_button = ttk.Button(root, text="Generate Another Password", command=generate_password)
generate_another_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# copy password button
copy_button = ttk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# reset form button
reset_button = ttk.Button(root, text="Reset Form", command=reset_form)
reset_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# run
root.mainloop()
