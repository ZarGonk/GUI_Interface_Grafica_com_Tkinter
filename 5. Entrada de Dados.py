import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('Enter Dados')

# Label text
text = ttk.Label(root,text='Entry:').pack()

# create widget constructor:Entry
entry = ttk.Entry(root).pack()

root.mainloop()