import random
import string
import tkinter as tk

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    password = generate_password()
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create GUI components
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

include_digits_var = tk.IntVar()
include_digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=include_digits_var)
include_digits_checkbox.pack()

include_special_chars_var = tk.IntVar()
include_special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=include_special_chars_var)
include_special_chars_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

# Start the GUI event loop
root.mainloop()
