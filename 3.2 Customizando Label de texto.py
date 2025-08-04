import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('Customizando Label de texto')
root.geometry('300x200')

# Create Label Text

message = ttk.Label(
    root,
    text='I am ZarGonk',
    font=('Times New Roman', 15),    
    foreground= 'Red',
    background= 'lightgray',
    anchor='center',
    borderwidth=5,
    relief='groove'
).pack()



root.mainloop()