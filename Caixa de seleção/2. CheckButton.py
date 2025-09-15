import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Example - Multiple Checkbuttons")

# Variables for each option
option1 = tk.BooleanVar()
option2 = tk.BooleanVar()
option3 = tk.BooleanVar()

# Function to display selected choices
def show_choices():
    choices = []
    if option1.get():
        choices.append("Python")
    if option2.get():
        choices.append("C++")
    if option3.get():
        choices.append("SQL")
    
    if choices:
        label.config(text="You chose: " + ", ".join(choices))
    else:
        label.config(text="No option selected")

# Create multiple checkbuttons
check1 = ttk.Checkbutton(root, text="Python", variable=option1, command=show_choices)
check1.pack(anchor="w", padx=10, pady=2)

check2 = ttk.Checkbutton(root, text="C++", variable=option2, command=show_choices)
check2.pack(anchor="w", padx=10, pady=2)

check3 = ttk.Checkbutton(root, text="SQL", variable=option3, command=show_choices)
check3.pack(anchor="w", padx=10, pady=2)

# Label to display the result
label = ttk.Label(root, text="Choose your favorite programming languages")
label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()