import tkinter as tk
from tkinter import ttk

def temperature():
    celsius = convert.get()

    fahrenheit = (celsius * 1.8) + 32

    kelvin = celsius + 273.15
    text_fahrenheit['text'] = f'{celsius}°C em {fahrenheit}°F'
    text_kelvin['text']     = f'{celsius}°C em {kelvin}K'


# Main Window
root = tk.Tk()
root.title('Temperature converter')
root.config(background='lightblue')

# Title Text Label
message = ttk.Label(root,
                    text='Temperature Converter',
                    font=('Hervetica bold', 16),
                    foreground='Black',
                    background='lightblue')
message.pack()





root.mainloop()