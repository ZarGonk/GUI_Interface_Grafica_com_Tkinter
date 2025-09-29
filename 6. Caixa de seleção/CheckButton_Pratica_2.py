import tkinter as tk
from tkinter import ttk

# Function to show selected days
def show_days():
    days = []
    if sunday.get():   days.append('Sunday')
    if monday.get():   days.append('Monday')
    if tuesday.get():  days.append('Tuesday')
    if wednesday.get():days.append('Wednesday')
    if thursday.get(): days.append('Thursday')
    if friday.get():   days.append('Friday')
    if saturday.get(): days.append('Saturday')

    # Show selected days or message if none
    text_result.config(text=', '.join(days) if days else 'No day selected')
    return days
 
# Function to clear all checkboxes
def disable():
    sunday.set(value=False)
    monday.set(value=False)
    tuesday.set(value=False)
    wednesday.set(value=False)
    thursday.set(value=False)
    friday.set(value=False)
    saturday.set(value=False)

    text_result.config(text='')


def save():
    date = show_days()
    with open('Save Date.txt', 'w', encoding='utf-8') as file:
            day = ', '.join(date)
            file.write(day)

    text_result.config(text='Days successfully saved!')

# --- Main Window ---
root = tk.Tk()
root.title('CheckButton 2')
root.resizable(True, True) 

# BooleanVars for each checkbox
sunday    = tk.BooleanVar(value=False)
monday    = tk.BooleanVar(value=False)
tuesday   = tk.BooleanVar(value=False)
wednesday = tk.BooleanVar(value=False)
thursday  = tk.BooleanVar(value=False)
friday    = tk.BooleanVar(value=False)
saturday  = tk.BooleanVar(value=False)

# Frame for checkboxes
frame_check = tk.Frame(root)
frame_check.grid(row=0, column=0, sticky='N')

# Checkbuttons
checkbox1 = ttk.Checkbutton(frame_check, text='Sunday', variable=sunday)
checkbox2 = ttk.Checkbutton(frame_check, text='Monday', variable=monday)
checkbox3 = ttk.Checkbutton(frame_check, text='Tuesday', variable=tuesday)
checkbox4 = ttk.Checkbutton(frame_check, text='Wednesday', variable=wednesday)
checkbox5 = ttk.Checkbutton(frame_check, text='Thursday', variable=thursday)
checkbox6 = ttk.Checkbutton(frame_check, text='Friday', variable=friday)
checkbox7 = ttk.Checkbutton(frame_check, text='Saturday', variable=saturday)

# Organize checkbuttons in grid
checkbox1.grid(row=0, column=0, padx=5, pady=2, sticky="W")
checkbox2.grid(row=1, column=0, padx=5, pady=2, sticky='W')
checkbox3.grid(row=2, column=0, padx=5, pady=2, sticky='W')
checkbox4.grid(row=0, column=1, padx=5, pady=2, sticky='W')
checkbox5.grid(row=1, column=1, padx=5, pady=2, sticky='W')
checkbox6.grid(row=2, column=1, padx=5, pady=2, sticky='W')
checkbox7.grid(row=3, column=1, padx=5, pady=2, sticky='W')

# Frame for buttons
frame_button = tk.Frame(root)
frame_button.grid(row=0, column=1)

# Confirm and Clear buttons
button_confirm = ttk.Button(frame_button, text='Confirm Availability', command=show_days)
button_confirm.grid(row=0, column=0, padx=10, pady=5, sticky='WN')

button_clear = ttk.Button(frame_button, text='Clear Selection', command=disable)
button_clear.grid(row=1, column=0, padx=10, pady=5, sticky="WN")

button_save = ttk.Button(frame_button, text='Save', command=save)
button_save.grid(row=2, column=0, padx=10, pady=5, sticky='WN')

# Label that displays the result
text_result = tk.Label(root, text='', foreground='blue', wraplength='170', justify='center')
text_result.grid(row=2, column=0, sticky='N')

# Sizegrip for resizing
sizegrid = ttk.Sizegrip(root)
sizegrid.grid(row=10, column=5, sticky='SE')

# Configure layout
root.rowconfigure(10, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
