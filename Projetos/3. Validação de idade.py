'''Criar um app que peça a idade e diga se a pessoa é maior ou menor de idade.'''

import tkinter as tk
from tkinter import ttk

# Function to validate age
def validation_age():
    try:
        year = int(entry.get())
        if year < 0:
            text['text'] = 'Invalid Age'
        elif year >= 18:  # Legal age is 18 or older
            text['text'] = 'Legal Age'
        else:
            text['text'] = 'Minor Age'
    
    except ValueError:
        text['text'] = 'Please enter valid data!'


# --- Main Window ---
root = tk.Tk()
root.title('Age Validation')
root.geometry('300x180')
root.resizable(width=False, height=False)

# Window Icon
try:
    photo = tk.PhotoImage(file='Projetos/assets/age-icon-2.png')
    root.iconphoto(False, photo)
except tk.TclError:
    print('Icon file not found')

# Title label
message = ttk.Label(
    root, 
    text='Age Validation', 
    font=('Times New Roman', 15), 
    foreground='red'
)
message.pack(padx=4)

# Label for entry
text_age = ttk.Label(root, text='Enter the age:')
text_age.pack(pady=4, padx=2)

# Entry field
entry = ttk.Entry(root)
entry.focus()
entry.pack(pady=4, padx=100)

# Button to check age
age_button = ttk.Button(root, text='Check', command=validation_age)
age_button.pack(pady=10)

# Result label
text = ttk.Label(root, text='')
text.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()