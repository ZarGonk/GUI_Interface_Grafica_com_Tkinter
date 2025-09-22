import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title('Sizegrip Example 2')
root.geometry('300x200')
root.resizable(True, True)

# Set maximum and minimum window size
root.maxsize(600, 400)
root.minsize(150, 50)

# Create Sizegrip (allows resizing by dragging the corner)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=1, sticky='SE')

# Configure grid to make widgets expand properly
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
