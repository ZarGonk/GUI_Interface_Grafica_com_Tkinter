"""
App that receives 2 numbers and shows the greatest one.
"""

import tkinter as tk
from tkinter import ttk

def show_result():
    """Compare the two numbers and show the greatest one."""
    value_1 = spin_value_1.get()
    value_2 = spin_value_2.get()

    if value_1 > value_2:
        text_result.config(text=f'{value_1} > {value_2}')
    elif value_2 > value_1:
        text_result.config(text=f'{value_1} < {value_2}')
    else:
        text_result.config(text=f'Values are equal: {value_1} = {value_2}')


# --- Main Window ---
root = tk.Tk()
root.title('Greatest Number')
root.geometry('300x200')
root.resizable(True, True)

# Instruction Label
text_label = ttk.Label(
    root,
    text='Choose the values and I will show the greatest one:'
)
text_label.grid(row=0, column=0, pady=5)

# Variables to store spinbox values
spin_value_1 = tk.IntVar()
spin_value_2 = tk.IntVar()

# Frame for Spinboxes
frame = tk.Frame(root)
frame.grid(row=1, column=0, sticky='W', padx=15, pady=2)

# Spinboxes
spin_box_1 = ttk.Spinbox(frame, from_=0, to=100, textvariable=spin_value_1, wrap=True, width=5)
spin_box_2 = ttk.Spinbox(frame, from_=0, to=100, textvariable=spin_value_2, wrap=True, width=5)

spin_box_1.grid(row=1, column=0, sticky='W', padx=5, pady=2)
spin_box_2.grid(row=1, column=1, sticky='W', padx=5, pady=2)

# Button to check result
button = ttk.Button(root, text='Check', command=show_result)
button.grid(row=2, column=0, pady=5)

# Result Label
text_result = ttk.Label(root, text='', wraplength=300, justify='center')
text_result.grid(row=3, column=0, pady=10)

# Start the Tkinter event loop
root.mainloop()