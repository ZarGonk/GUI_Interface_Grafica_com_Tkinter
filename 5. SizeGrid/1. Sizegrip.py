import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title('Sizegrip Demo')
root.geometry('300x200')
root.resizable(True, False)  # Allow resizing in both directions

# Configure grid layout to allow expansion
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create the Sizegrip widget (used to resize the window)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=1, sticky='SE')  # Place at the bottom-right corner

# Start the Tkinter event loop
root.mainloop()