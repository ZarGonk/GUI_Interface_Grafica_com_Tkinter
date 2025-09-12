import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title('Enter Data')

# Create a Label widget
label = ttk.Label(root, text='Entry:')  # Text displayed next to the entry field
label.pack()

# Create an Entry widget (input field)
entry = ttk.Entry(root)  # Field where the user can type text
entry.pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()