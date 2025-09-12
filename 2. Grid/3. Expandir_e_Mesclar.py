import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('Expand and Merge Cells')

# Create the widgets
lbl1 = ttk.Label(root, text='Widget 1', width=15, background='pink')
lbl2 = ttk.Label(root, text='Widget 2', width=30, background='purple')
lbl3 = ttk.Label(root, text='Widget 3', width=30, background='orange')

# Grid positioning
lbl1.grid(row=0, column=0)
lbl2.grid(row=0, column=1, columnspan=2)
lbl3.grid(row=1, column=0, rowspan=2, columnspan=3)

# Show the window
root.mainloop()