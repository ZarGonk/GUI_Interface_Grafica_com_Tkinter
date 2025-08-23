import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.geometry('300x200')        # Set the window size
root.title('Entry Widget Demo') # Set the window title

# --- Name Entry Field ---
text_name = ttk.Label(root, text='Name:')  # Label for the name field
text_name.pack(pady=2)

name_entry = ttk.Entry(root)   # Entry widget where the user types their name
name_entry.pack(pady=5)

name_entry.focus()  # Automatically gives keyboard focus to this field on startup

# --- Email Entry Field ---
text_email = ttk.Label(root, text='Email:')  # Label for the email field
text_email.pack(pady=2)

email_entry = ttk.Entry(root)  # Entry widget where the user types their email
email_entry.pack(pady=5)

# Start the Tkinter event loop (keeps the window open)
root.mainloop()
