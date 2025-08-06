import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.geometry('300x200')

# --- Different ways of creating and configuring a Label widget ---

# 1) Directly passing options (arguments) when creating the widget
ttk.Label(root, text='Hi, there').pack(ipadx=10, ipady=20)

# 2) Using dictionary-style indexing to set options after creation
label2 = ttk.Label(root)
label2['text'] = 'Hi, there'     # Configure text like a dictionary key
label2.pack(ipadx=10, ipady=30)

# 3) Using the config() (or configure()) method with keyword arguments
label3 = ttk.Label(root)
label3.config(text='Hi, there')  # Equivalent to label3['text']
label3.pack(ipadx=10, ipady=40)

# Start the Tkinter event loop (keeps the window open)
root.mainloop()
