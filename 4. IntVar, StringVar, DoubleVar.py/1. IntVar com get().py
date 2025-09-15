import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title('IntVar Example')
root.geometry('250x100')

# Creating an IntVar (special Tkinter variable that stores integers)
# It will stay synchronized with the Entry widget
var_number = tk.IntVar()

# Function called when the button is clicked
def show():
    # Gets the current value of the IntVar (what was typed in the Entry)
    # Updates the Label to display this value
    show_number['text'] = var_number.get()

# Entry linked to the IntVar through textvariable
# Anything typed in the Entry will automatically update var_number
entry_number = ttk.Entry(root, textvariable=var_number)
entry_number.grid(row=0, column=0, padx=10, pady=5)

# Button that calls the show() function when clicked
button = ttk.Button(root, text='Show Number', command=show)
button.grid(row=0, column=1, padx=5, pady=5)

# Label that will display the value of the IntVar after clicking the button
show_number = tk.Label(root, text='', foreground='Green')
show_number.grid()

# Start the Tkinter event loop
root.mainloop()