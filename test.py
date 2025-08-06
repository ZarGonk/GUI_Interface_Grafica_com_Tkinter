import tkinter as tk
from tkinter import ttk

def color(event):
    root.config(background='black')

def new_color(event):
    root.config(background='red')


# Main Window
root = tk.Tk()
root.title('Test')


btn = ttk.Button(root, text='Color')
btn.bind('<KeyPress-B>', color)
btn.bind('<KeyPress-R>',new_color, add='+')
btn.pack(expand=True)

root.mainloop()