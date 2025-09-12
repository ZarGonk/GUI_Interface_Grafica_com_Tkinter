import tkinter as tk
from tkinter import ttk

# Function to capture input and display the full name
def show_full_name():
    name = entry_name.get()          # Get text from the "Name" Entry
    last_name = entry_last_name.get() # Get text from the "Last Name" Entry
    full_name = f'Full Name: {name} {last_name}'
    lbl_full_name.config(text=full_name)  # Update the Label with the full name

# Create the main application window
root = tk.Tk()
root.title('Text Capture')
root.geometry('200x200')

# --- Name field ---
lbl_name = ttk.Label(root, text='Name:')
lbl_name.pack()

entry_name = ttk.Entry(root)
entry_name.pack()

# --- Last Name field ---
lbl_last_name = ttk.Label(root, text='Last Name:')
lbl_last_name.pack()

entry_last_name = ttk.Entry(root)
entry_last_name.pack()

# --- Button to display the full name ---
show_button = ttk.Button(root, text='Show Name', command=show_full_name)
show_button.pack()

# --- Label to display the result ---
lbl_full_name = ttk.Label(root, text='')
lbl_full_name.pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()