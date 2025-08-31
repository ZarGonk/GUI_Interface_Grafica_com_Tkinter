import tkinter as tk
from tkinter import ttk

def virgula_by_point(string):
    number = string.replace(',', '.')
    return float(number)

def double():
    try:
        number = value.get()
        if not number.strip():
            text['text'] = 'Enter any number'
            text['foreground'] = 'Red'
            return
        
        number = virgula_by_point(number)
        result = number * 2
        
        text['text'] = f'Double the {number} is the {result}' 
        text['foreground'] = 'Green'

    except ValueError:
        text['text'] = f'Valor Invalido! Somento Numeros São Permitidos'
        text['foreground'] = 'Red'

# Main Window
root = tk.Tk()
root.title('Doubling Value')
root.geometry('300x200')
root.resizable(False, False)

# Title text label
message = ttk.Label(
    root, 
    text='Doubling Numbers', 
    font=('Century', 15), 
    foreground='Red')
message.pack(pady=4)

# Text Label
text_number = ttk.Label(
    root,
    text='Enter a Number:',
    font=('Century', 11),
    foreground='Black')
text_number.pack(pady=4)

# Entry Value
value = ttk.Entry(
    root,
    font=('arial',11),
    foreground='Blue')
value.focus()
value.pack(pady=4)

# Bottun Number
button_number = ttk.Button(
    root,
    text='Double the number',
    command=double)
button_number.pack()

# End Result
text = ttk.Label(root, text='')
text.pack(pady=6)

root.mainloop()