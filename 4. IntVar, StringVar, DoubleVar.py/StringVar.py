import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title('StringVar Example')

# ----- Create the StringVar -----
# StringVar is a special Tkinter variable that stores text
string_var = tk.StringVar()

# ----- Create an Entry linked to the StringVar -----
entry = ttk.Entry(root, textvariable=string_var)
entry.grid(row=0, column=0, padx=10, pady=5)  

# ----- Create a Label linked to the same StringVar -----
label = ttk.Label(root, textvariable=string_var)
label.grid(row=1, column=0, padx=10, pady=5) 

# Start the Tkinter event loop
root.mainloop()