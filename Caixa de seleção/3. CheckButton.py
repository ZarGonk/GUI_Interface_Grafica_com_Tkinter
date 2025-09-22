import tkinter as tk
from tkinter import ttk

def show_option():
    result = []
    if var1.get():
        result.append('Option 1')
    if var2.get():
        result.append('Option 2')
    
    # Update label with result
    text_label.config(text=', '.join(result) if result else 'No option selected')


# Main Window
root = tk.Tk()
root.title('CheckButton Example')
root.geometry('300x200')
root.resizable(True, True) 

# Instruction label
lbl = ttk.Label(root, text='Check the options:')
lbl.grid(row=0, column=0, columnspan=2, pady=5)

# Variables
var1 = tk.BooleanVar(value=False)
var2 = tk.BooleanVar(value=False)

# Checkbuttons
checkbox1 = ttk.Checkbutton(root, text='Option 1', variable=var1)
checkbox1.grid(row=1, column=0, sticky="w", padx=10)

checkbox2 = ttk.Checkbutton(root, text='Option 2', variable=var2)
checkbox2.grid(row=2, column=0, sticky="w", padx=10)

# Confirm button
button_check = ttk.Button(root, text='Confirm', command=show_option)
button_check.grid(row=3, column=0, pady=10)

# Result label
text_label = tk.Label(root, text='', fg="blue")
text_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()
