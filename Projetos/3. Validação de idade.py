import tkinter as tk
from tkinter import ttk

def validation_age():
    try:
        year = int(entry.get())
        if year < 0:
            text['text'] = 'Invalid Age'
        elif year > 18:
            text['text'] = f'Legal Age'
        else:
            text['text'] = f'Minor Age'
    
    except ValueError:
        text['text'] = f'Please enter valid data!'


# Main Window
root = tk.Tk()
root.title('Age Validation')
root.geometry('300x180')
root.resizable(width=False, height=False)

# Icon
try:
    photo = tk.PhotoImage(file='Projetos/assets/age-icon-2.png')
    root.iconphoto(False, photo)
except tk.TclError:
    print('Icon file not found')

# Title Label
message = ttk.Label(root, text='Age Validation', font=('Times New Roman', 15), foreground='red')
message.pack(padx=4)

# Entry
text_age = ttk.Label(root, text='Enter the age:')
text_age.pack(pady=4, padx=2)
entry = ttk.Entry(root)
entry.focus()
entry.pack(pady=4, padx=100)

# Button
age_button = ttk.Button(root, text='Check', command=validation_age)
age_button.pack(pady=10)

# Result Label
text = ttk.Label(root, text='')
text.pack(pady=5)

root.mainloop()