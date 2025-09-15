import tkinter as tk
from tkinter import ttk

# Function to clear the Entry
def clear():
    string_var.set('')

# Function to update the uppercase mirror
def update_uppercase(*args):
    text_upper.set(string_var.get().upper())

# Main Window
root = tk.Tk()
root.title('StringVar Example')

# Create a StringVar to store user input
string_var = tk.StringVar()
# Create another StringVar to store uppercase text
text_upper = tk.StringVar()

# Whenever string_var changes, call update_uppercase
string_var.trace("w", update_uppercase)

# Entry linked to string_var
entry = ttk.Entry(root, textvariable=string_var)
entry.grid(row=0, column=0, padx=10, pady=5)  

# Normal mirror label (shows input as typed)
label = ttk.Label(root, textvariable=string_var)
label.grid(row=1, column=0, padx=10, pady=5) 

# Uppercase mirror label
label_upper = ttk.Label(root, textvariable=text_upper)
label_upper.grid(row=2, column=0, padx=10, pady=5) 

# Button to clear the Entry
button = ttk.Button(root, text='Clear', command=clear)
button.grid(row=0, column=1, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
