'''Criar um app que peça a temperatura em Celsius e retorne a temperatura em Fahrenheit  e Kelvin'''

import tkinter as tk
from tkinter import ttk

# Function to convert Celsius to Fahrenheit and Kelvin
def temperature():
    try:
        celsius = float(convert.get())

        # Temperature Conversion
        fahrenheit = (celsius * 1.8) + 32
        kelvin = celsius + 273.15

        # Display conversion result
        text.config(
            text = f'{celsius}°C = {fahrenheit:.2f}°F\n{celsius}°C = {kelvin:.2f}K',
            font=('Arial', 12, 'bold'),
            fg='Green',
            bg='Lightblue'
        )

    except ValueError:
        # Error message for invalid input
        text.config(
            text = 'Error! Please enter a valid number',
            font = ('Arial', 12, 'bold'),
            fg = 'Red',
            bg = 'Lightblue'
        )
        

# --- Main Window ---
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x200')
root.config(background='lightblue')

# Title label
message = tk.Label(
    root,
    text='Temperature Converter',
    font=('Helvetica', 16, 'bold'),
    fg='Black',
    background='lightblue'
)
message.pack(pady=4)

# Instruction label
text_celsius = tk.Label(
    root,
    text='Enter temperature in Celsius:',
    font=('Times New Roman', 12),
    bg='lightblue',
    fg='Green'
)
text_celsius.pack(pady=6)

# Entry field for user input
convert = ttk.Entry(root, foreground='blue')
convert.focus()
convert.pack()

# Button to execute conversion
button_temperature = ttk.Button(root, text='Convert', command=temperature)
button_temperature.pack(pady=4)

# Label to display result
text = tk.Label(root, text='', foreground='Green', background='lightblue')
text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()