import tkinter as tk
from tkinter import ttk

def calculate_power():
    try:
        first_number = int(entry_number1.get())
        second_number = int(entry_number2.get())
        result = first_number ** second_number
        lbl_result.config(text=f'Result: {result}')
    except ValueError:
        lbl_result.config(text='Error: Please enter valid numbers')


# Main Window
root = tk.Tk()
root.title('Power Calculator')
root.geometry('300x200')  # Optional fixed size

# First number
lbl_first_number = ttk.Label(root, text='First number:')
lbl_first_number.pack(pady=4)
entry_number1 = ttk.Entry(root)
entry_number1.focus()
entry_number1.pack(pady=2)

# Second number
lbl_second_number = ttk.Label(root, text='Second number:')
lbl_second_number.pack(pady=4)
entry_number2 = ttk.Entry(root)
entry_number2.pack(pady=2)

# Button
calculate_button = ttk.Button(root, text='Calculate', command=calculate_power)
calculate_button.pack(pady=4)

# Result label
lbl_result = ttk.Label(root, text='', font=('Arial', 12, 'bold'))
lbl_result.pack(pady=8)

root.mainloop()