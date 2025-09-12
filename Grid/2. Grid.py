import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('Columnspan')

# Create the widgets
lbl1 = ttk.Label(root, text='Grid 1', width=20, background='Red')
lbl2 = ttk.Label(root, text='Grid 2', width=20, background='Blue')
lbl3 = ttk.Label(root, text='Grid 3', width=40, background='Green')

# Grid positioning
lbl1.grid(row=0, column=0)
lbl2.grid(row=0, column=1)
# Columnspan -> Uses 2 grid spaces instead of 1
lbl3.grid(row=1, column=0, columnspan=2)

# Show the window
root.mainloop()