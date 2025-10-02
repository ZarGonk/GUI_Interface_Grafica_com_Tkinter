import tkinter as tk
from tkinter import ttk

# Background color
color = '#D4D2D2'

# --- Main Window ---
root = tk.Tk()
root.title('Login')
root.geometry('240x100')
root.config(background=color)

# Configure grid layout (3 rows x 2 columns)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# --- Username ---
username = tk.Label(
    root,
    text='Username:',
    font=('Helvetica', 10),
    bg=color
)
username.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)

entry_name = ttk.Entry(root)
entry_name.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)

# --- Password ---
password = tk.Label(
    root,
    text='Password:',
    font=('Helvetica', 10),
    bg=color
)
password.grid(row=1, column=0, sticky=tk.EW, padx=5, pady=5)

entry_password = ttk.Entry(root, show='*')
entry_password.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)

# --- Login Button ---
button_login = ttk.Button(root, text='Login')
button_login.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()