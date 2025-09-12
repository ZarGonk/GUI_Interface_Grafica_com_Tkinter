import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title('Expand and Merge Cells')

# Define a minimum size for the row
root.grid_rowconfigure(1, minsize=80)

# Create the Widgets
lbl1 = ttk.Label(root, text='Widget 1', width=15, background='pink')
lbl2 = ttk.Label(root, text='Widget 2', width=30, background='purple')
lbl3 = ttk.Label(root, text='Widget 3', width=30, background='orange')

# Grid positioning
lbl1.grid(row=0, column=0)
lbl2.grid(row=0, column=1, columnspan=2)

# Rowspan = uses 2 or more rows
# Columnspan = uses 2 or more columns
# Sticky = attaches the widget to the window borders 
#          (using compass directions: 'n, e, s and/or w')
lbl3.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='ewns')

# Show the window
root.mainloop()
