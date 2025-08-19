import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')

# Using the widget builder when creating the widget
ttk.Label(root, text='Hi, there').pack(ipadx=10, ipady=20)

# Using a dictionary index after creating the widget
label2 = ttk.Label(root)
label2['text'] = 'Hi, there'
label2.pack(ipadx=10, ipady=30)

# Using the config() method with keyword arguments
label3 = ttk.Label(root)
label3.config(text='Hi, there')
label3.pack(ipadx=10, ipady=40)

root.mainloop()