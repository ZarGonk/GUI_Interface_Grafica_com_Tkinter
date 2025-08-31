import tkinter as tk
from tkinter import ttk

def temperature():
    try:
        celsius= float(convert.get())

        # Temperature Conversion
        fahrenheit= (celsius * 1.8) + 32
        kelvin= celsius + 273.15

        text.config(text = f'{celsius}°C em {fahrenheit:.2f}°F\n{celsius}°C em {kelvin:.2f}K',
                    font=('Arial', 12, 'bold'),
                    fg='Green',
                    bg='Lightblue')

    except ValueError:
        text.config(
        text = f'Erro! Insira um número válido',
        font = ('Arial', 12, 'bold'),
        fg = 'Red',
        bg = 'lightblue')
        

# Main Window
root= tk.Tk()
root.title('Temperature converter')
root.geometry('300x200')
root.config(background='lightblue')

# Title Text Label
message= tk.Label(root,
                    text='Temperature Converter',
                    font=('Hervetica', 16, 'bold'),
                    fg='Black',
                    background='lightblue')
message.pack(pady=4)

# Text Label
text_celsius = tk.Label(root,
                        text='Set the temperature to Celsius:',
                        font=('Times New Roman', 12),
                        bg='lightblue',
                        fg='Green')
text_celsius.pack(pady=6)


# Entry for function "temperature"
convert= ttk.Entry(root, foreground='blue')
convert.focus()
convert.pack()

# Button execute function "temperature"
button_temperature= ttk.Button(root, text='Convert', command=temperature)
button_temperature.pack(pady=4)

# Text label result
text= tk.Label(root, text='',foreground='Green' ,background='lightblue')
text.pack(pady=10)

root.mainloop()