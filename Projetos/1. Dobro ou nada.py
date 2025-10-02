'''Criar um campo para digitar um número e um botão que mostre o dobro.'''

import tkinter as tk
from tkinter import ttk

# Function to replace commas with dots and convert to float
def comma_to_point(string):
    number = string.replace(',', '.')
    return float(number)

# Function to calculate the double
def double():
    try:
        number = value.get()
        if not number.strip():
            text['text'] = 'Enter a number'
            text['foreground'] = 'Red'
            return
        
        number = comma_to_point(number)
        result = number * 2
        
        text['text'] = f'Double of {number} is {result}' 
        text['foreground'] = 'Green'

    except ValueError:
        text['text'] = 'Invalid value! Only numbers are allowed'
        text['foreground'] = 'Red'

# --- Main Window ---
root = tk.Tk()
root.title('Doubling Value')
root.geometry('300x200')
root.resizable(False, False)

# Title label
message = ttk.Label(
    root, 
    text='Doubling Numbers', 
    font=('Century', 15), 
    foreground='Red'
)
message.pack(pady=4)

# Instruction label
text_number = ttk.Label(
    root,
    text='Enter a number:',
    font=('Century', 11),
    foreground='Black'
)
text_number.pack(pady=4)

# Entry field
value = ttk.Entry(
    root,
    font=('Arial', 11),
    foreground='Blue'
)
value.focus()
value.pack(pady=4)

# Button to calculate double
button_number = ttk.Button(
    root,
    text='Double the number',
    command=double
)
button_number.pack()

# Label to show result
text = ttk.Label(root, text='')
text.pack(pady=6)

# Start the Tkinter event loop
root.mainloop()