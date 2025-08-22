import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.geometry('300x200')
root.title('Entry Widget Demo')

# Entry Name FOCUS
text_name = ttk.Label(root, text='Name:').pack(pady=2)
name_entry = ttk.Entry(root)
name_entry.pack(pady=5)
name_entry.focus()

# Entry Email
text_email = ttk.Label(root, text='Email:').pack(pady=2)
email_entry = ttk.Entry(root)
email_entry.pack(pady=5)

root.mainloop()
