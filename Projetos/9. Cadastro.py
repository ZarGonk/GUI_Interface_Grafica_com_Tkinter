import tkinter as tk
from tkinter import ttk

def registration():
    valid_fields = 0

    if name.get().strip():
        valid_fields += 1

    if email.get().strip() and '@' in email.get():
        valid_fields += 1

    if select_radio.get() in ['M', 'F', 'O']:
        valid_fields += 1

    if valid_fields == 3:
        label_confirmation['text'] = 'Registration confirmed!'
        name.set('')
        email.set('')
        select_radio.set('')
        check_var.set(False)
    else:
        label_confirmation['text'] = 'Please fill in all required fields *'

    

# Main Window
root = tk.Tk()
root.title('')
#root.geometry('300x200')
root.resizable(True, True) 

title = ttk.Label(root, text='App de cadastro', font=('Arial', 16, 'bold'))
title.grid(row=0, column=0, padx=5, pady=2)

# Variable name, E-mail
name  = tk.StringVar()
email = tk.StringVar()
select_radio = tk.StringVar()
check_var = tk.BooleanVar(value=False)


# Frame the Name and Email
frame_0 = ttk.Frame(root)
frame_0.grid(row=1, column=0, sticky='W')

# Name Field
label_0 = ttk.Label(frame_0, text='* Name: ')
label_0.grid(row=1, column=0, padx=5, pady=2, sticky='W')

entry_0 = ttk.Entry(frame_0, textvariable=name)
entry_0.grid(row=1, column=1, pady=2 , sticky='W')

# E-mail Field 
label_1 = ttk.Label(frame_0, text='* E-mail: ')
label_1.grid(row=2, column=0, padx=5, pady=2, sticky='W')

entry_1 = ttk.Entry(frame_0, textvariable=email)
entry_1.grid(row=2, column=1, pady=2, sticky='W')

# Radio sex
label_2 = ttk.Label(root, text='* What is your gender: ')
label_2.grid(row=2, column=0, padx=5, pady=2, sticky='W')

# Sexual orientation
genres = (
    ('Male', 'M'),
    ('Female', 'F'),
    ('Others', 'O')
)

# Frame to hold the radiobuttons
frame_1 = ttk.Frame(root)
frame_1.grid(row=3, column=0, sticky='W')

for index, gender in enumerate(genres):
    radio = ttk.Radiobutton(frame_1, text=gender[0], value=gender[1], variable=select_radio)
    radio.grid(row=0, column= index, padx=5, sticky='W')

# Check
check = ttk.Checkbutton(root, text='I wish to receive an email.', variable=check_var)
check.grid(row=4, column=0, padx=5,pady=10, sticky='W')


# End

button = ttk.Button(root, text='confirm', command=registration)
button.grid(row=5, column=0)

label_confirmation = ttk.Label(root, text='')
label_confirmation.grid(row=6, column=0)

# Start the Tkinter event loop
root.mainloop()