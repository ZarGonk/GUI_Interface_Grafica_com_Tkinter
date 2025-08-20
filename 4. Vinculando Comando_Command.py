import tkinter as tk
from tkinter import ttk

# The widgets can respond to the events such as:
#  Mouse clicks
#  Key presses

root = tk.Tk()
root.title('Command/ Event')

# Function using the button
def button_click():
    print('Button Clicked')

# Create a Button
button = ttk.Button(root, text='Click Me',command= button_click).pack()

root.mainloop()