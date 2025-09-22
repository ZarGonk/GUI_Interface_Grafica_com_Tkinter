import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('CheckButton 2')
root.geometry('300x200')
root.resizable(True, True)  # Allow window resizing

# Variable to store the state of the checkbutton
check_var = tk.StringVar(value="Disable")  # initial state

# Function called when checkbox is clicked
def toggle():
    print("Current state:", check_var.get())

# Create CheckButton
checkbox = ttk.Checkbutton(
    root,
    text='Option to check',
    variable=check_var,       # connect to variable
    command=toggle,           # function called on click
    onvalue='Active',         # value when checked
    offvalue='Disable'        # value when unchecked
)
checkbox.grid(pady=20)

# Start the Tkinter event loop
root.mainloop()
