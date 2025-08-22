import tkinter as tk
from tkinter import ttk

def Show_full_name():
    name = entry_name.get()
    last_name = entry_last_name.get()
    full_name = f'Full Name: {name} {last_name}'
    lbl_full_name.config(text=full_name)

# Main Window
root = tk.Tk()
root.title('Text Capture')
root.geometry('200x200')

# Create text 'Name'
lbl_name = ttk.Label(root, text='Name:')
lbl_name.pack()

# Create Entry for name
entry_name = ttk.Entry(root)
entry_name.pack()

# Create text 'Last Name'
lbl_last_name = ttk.Label(root, text='Last name:')
lbl_last_name.pack()

# Create Entry for last name
entry_last_name = ttk.Entry(root)
entry_last_name.pack()

# Button to show full name
show_button = ttk.Button(root, text='Show Name', command=Show_full_name)
show_button.pack()

# Label to display full name
lbl_full_name = ttk.Label(root, text='')
lbl_full_name.pack()

root.mainloop()
