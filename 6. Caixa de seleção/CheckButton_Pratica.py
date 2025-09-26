import tkinter as tk
from tkinter import ttk

def confirm_order():
    ingredients_list = []
    if ingredients['cheese'].get(): ingredients_list.append('Cheese')
    if ingredients['calabrese'].get(): ingredients_list.append('Calabrese')
    if ingredients['olive'].get(): ingredients_list.append('Olive')
    if ingredients['cucumber'].get(): ingredients_list.append('Cucumber')
    if ingredients['mayonnaise'].get(): ingredients_list.append('Mayonnaise')
    if ingredients['tomato'].get(): ingredients_list.append('Tomato')
    if ingredients['onion'].get(): ingredients_list.append('Onion')
    if ingredients['mushroom'].get(): ingredients_list.append('Mushroom')
    
    # Show selected ingredients or a message if none were selected
    text_menu.config(text=', '.join(ingredients_list) if ingredients_list else 'No ingredient selected')


color_window = "#AEE1FF"

# Main Window
root = tk.Tk()
root.title('CheckButton 1')
root.geometry('250x220')
root.resizable(True, True) 
root.config(bg=color_window)

# Center window
window_width = 250
window_height = 220
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Title text
text_title = tk.Label(root, text='Which ingredients do you want?', 
                      bg=color_window, font=('arial', 10, 'bold'))
text_title.grid(row=0, column=0, columnspan=2, sticky='WE', pady=5)

# Dictionary with all ingredients as BooleanVar (unchecked = False)
ingredients = {
    name: tk.BooleanVar(value=False)
    for name in [
        'cheese', 'calabrese', 'olive', 'cucumber', 
        'mayonnaise', 'tomato', 'onion', 'mushroom'
    ]
}

# Frame to group the checkbuttons
frame = tk.Frame(root, bg='white', bd=2, relief='solid')
frame.grid(row=1, column=0)

# Checkbuttons
checkbox1 = ttk.Checkbutton(frame, text='Cheese', variable=ingredients['cheese'])
checkbox2 = ttk.Checkbutton(frame, text='Calabrese', variable=ingredients['calabrese'])
checkbox3 = ttk.Checkbutton(frame, text='Olive', variable=ingredients['olive'])
checkbox4 = ttk.Checkbutton(frame, text='Cucumber', variable=ingredients['cucumber'])
checkbox5 = ttk.Checkbutton(frame, text='Mayonnaise', variable=ingredients['mayonnaise'])
checkbox6 = ttk.Checkbutton(frame, text='Tomato', variable=ingredients['tomato'])
checkbox7 = ttk.Checkbutton(frame, text='Onion', variable=ingredients['onion'])
checkbox8 = ttk.Checkbutton(frame, text='Mushroom', variable=ingredients['mushroom'])

# Grid organization for checkbuttons
checkbox1.grid(row=1, column=0, sticky='W', padx=5, pady=2)
checkbox2.grid(row=2, column=0, sticky='W', padx=5, pady=2)
checkbox3.grid(row=3, column=0, sticky='W', padx=5, pady=2)
checkbox4.grid(row=4, column=0, sticky='W', padx=5, pady=2)

checkbox5.grid(row=1, column=1, sticky='W', padx=5, pady=2)
checkbox6.grid(row=2, column=1, sticky='W', padx=5, pady=2)
checkbox7.grid(row=3, column=1, sticky='W', padx=5, pady=2)
checkbox8.grid(row=4, column=1, sticky='W', padx=5, pady=2)

# Confirm button
button = ttk.Button(root, text='Confirm order', command=confirm_order)
button.grid(row=2, column=0, columnspan=2, pady=5)

# Configure layout weights
root.rowconfigure(2, weight=0)
root.columnconfigure(0, weight=1)

# Label that displays the result
text_menu = tk.Label(root, text='', bg=color_window, wraplength=230, justify='center')
text_menu.grid(row=3, column=0, columnspan=2, rowspan=2, pady=10, sticky="WE")

# Sizegrip for resizing
sizegrid = ttk.Sizegrip(root)
sizegrid.grid(row=30, column=0, sticky='SE')

root.rowconfigure(30, weight=1)

# Start the Tkinter event loop
root.mainloop()