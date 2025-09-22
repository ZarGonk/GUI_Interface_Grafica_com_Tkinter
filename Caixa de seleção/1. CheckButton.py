import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('CheckButton 1')
root.geometry('300x200')
root.resizable(True, True)  # Allow window resizing

# Struct de check button
checkbox = ttk.Checkbutton(root, text='Option the check', 
                           command='Activate a function', variable='normally a BooleanVar', 
                           onvalue='Active', offvalue='Disable').grid()

# Start the Tkinter event loop
root.mainloop()