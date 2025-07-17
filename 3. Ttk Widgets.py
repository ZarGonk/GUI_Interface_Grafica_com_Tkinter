import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')

button = tk.Label(root,text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()


root.mainloop()