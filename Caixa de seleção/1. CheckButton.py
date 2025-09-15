import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('CheckButton Example')
root.geometry('300x200')
root.resizable(True, True)  # Allow window resizing

# IntVar to store the state of the checkbox
check_var = tk.IntVar(value=0)

# Function to show the checkbox state
def show_state():
    state = check_var.get()
    if state == 1:
        label.config(text='Checkbox is checked')
    else:
        label.config(text='Checkbox is unchecked')

# Create the Checkbutton linked to check_var
check = ttk.Checkbutton(root, text='Accept Terms', variable=check_var, command=show_state)
check.grid(row=0, column=0, sticky='W')

# Label to display the state of the checkbox
label = ttk.Label(root, text='Waiting for action...')
label.grid(row=1, column=0)

# Grid layout configuration for resizing
root.rowconfigure(2, weight=1)
root.columnconfigure(1, weight=1)

# Create the Sizegrip (for resizing the window)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=2, column=1, sticky='SE')

# Start the Tkinter event loop
root.mainloop()