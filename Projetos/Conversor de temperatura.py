import tkinter as tk
from tkinter import ttk

def temperature():
    try:
        celsius= float(convert.get())

        # Temperature Conversion
        fahrenheit= (celsius * 1.8) + 32
        kelvin= celsius + 273.15

        text['text'] = f'{celsius}°C em {fahrenheit:.2f}°F\n{celsius}°C em {kelvin}K'
    except ValueError:
        text['text'] = f'Erro!'
        text['font'] = ('Arial', 16, 'bold')
        text['foreground'] = 'Red'
        text['background'] = 'lightblue'
        

# Main Window
root= tk.Tk()
root.title('Temperature converter')
root.geometry('300x200')
root.config(background='lightblue')

# Title Text Label
message= ttk.Label(root,
                    text='Temperature Converter',
                    font=('Hervetica bold', 16),
                    foreground='Black',
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
text= ttk.Label(root, text='',foreground='Green' ,background='lightblue')
text.pack(pady=10)

root.mainloop()