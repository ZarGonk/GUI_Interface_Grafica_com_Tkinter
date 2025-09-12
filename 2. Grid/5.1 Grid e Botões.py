import tkinter as tk
from tkinter import ttk, messagebox

def show_message(text):
    messagebox.showinfo('Button Clicked', text)

# Main Window
root = tk.Tk()
root.title('Expand and Merge Cells')
root.configure(background='lavender')

# Creating the buttons
button1 = ttk.Button(root, text='Button 1', command=lambda: show_message('Button 1'))
button2 = ttk.Button(root, text='Button 2', command=lambda: show_message('Button 2'))
button3 = ttk.Button(root, text='Button 3', command=lambda: show_message('Button 3'))
button4 = ttk.Button(root, text='Button 4', command=lambda: show_message('Button 4'))
button5 = ttk.Button(root, text='Button 5', command=lambda: show_message('Button 5'))

# Grid positioning
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=1, column=1, padx=10)

# Spacer row (empty label to create spacing)
ttk.Label(root, text='', background='lavender').grid(row=2, sticky='we')

button4.grid(row=3, column=0, columnspan=2, pady=5)
button5.grid(row=5, column=0, columnspan=2, sticky='we')

# Show the window
root.mainloop()