import tkinter as tk
from tkinter import ttk

def charge_window_color():
    window_color = selected.get()
    for widget in (root, frame, text_label):
        widget.config(bg=window_color)
        
    style = ttk.Style()
    style.configure('Custom.TButton',background=window_color)
    style.configure('Custom.TRadiobutton', background=window_color)


# Main Window
root = tk.Tk()
root.title('CheckButton 1')
root.geometry('300x200')
root.resizable(True, True) 

selected = tk.StringVar(value='')

text_label = tk.Label(root, text='Choose the color of the window', font=('arial', 12, 'bold'))
text_label.grid(row=0, column=0, padx=5, pady=2)

colors = (('Red', '#FF0000'), ('Blue', '#0000FF'), ('Green', '#00FF00'))

frame = tk.Frame(root)
frame.grid(row=1, column=0, sticky='W')

for color in colors:
    r = ttk.Radiobutton(frame, text=color[0], value=color[1], variable=selected, style='Custom.TRadiobutton')
    r.grid(padx=10, pady=2, sticky='W')

button = ttk.Button(root, text='Confirm Color', command=charge_window_color, style='Custom.TButton')
button.grid(row=2, column=0)

# Start the Tkinter event loop
root.mainloop()