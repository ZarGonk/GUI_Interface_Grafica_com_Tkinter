import tkinter as tk
from tkinter import ttk

def register():
    """Validate fields and display confirmation or error messages."""
    
    # Check if the name field is empty
    if not name.get().strip():
        label_confirmation.config(text='Name is required!', foreground='red')
        return

    # Validate email (must contain '@' and '.')
    if not email.get().strip() or '@' not in email.get() or '.' not in email.get():
        label_confirmation.config(text='Invalid or missing email!', foreground='red')
        return
    
    # Validate gender selection
    if selected_gender.get() not in ['M', 'F', 'O']:
        label_confirmation.config(text='Please select your gender!', foreground='red')
        return

    # If all validations pass, confirm registration
    label_confirmation.config(text='Registration confirmed!', foreground='green')
    
    # Clear all fields
    name.set('')
    email.set('')
    selected_gender.set('')
    newsletter_var.set(False)


# --- Main Window ---
root = tk.Tk()
root.title('Registration App')
root.geometry('280x235')
root.resizable(True, True)

# App title label
title = ttk.Label(root, text='Registration App', font=('Arial', 16, 'bold'))
title.grid(row=0, column=0, padx=10, pady=10)

# --- Variables ---
name = tk.StringVar()
email = tk.StringVar()
selected_gender = tk.StringVar()
newsletter_var = tk.BooleanVar(value=False)

# --- Frame for Name and Email fields ---
frame_user = ttk.Frame(root)
frame_user.grid(row=1, column=0, sticky='W', padx=10, pady=5)

# --- Name Field ---
label_name = ttk.Label(frame_user, text='* Name:')
label_name.grid(row=1, column=0, padx=5, pady=2, sticky='W')

entry_name = ttk.Entry(frame_user, textvariable=name, width=30)
entry_name.grid(row=1, column=1, pady=2, sticky='W')

# --- Email Field ---
label_email = ttk.Label(frame_user, text='* Email:')
label_email.grid(row=2, column=0, padx=5, pady=2, sticky='W')

entry_email = ttk.Entry(frame_user, textvariable=email, width=30)
entry_email.grid(row=2, column=1, pady=2, sticky='W')

# --- Gender Selection ---
label_gender = ttk.Label(root, text='* What is your gender:')
label_gender.grid(row=2, column=0, padx=15, pady=5, sticky='W')

# Frame to organize the gender radio buttons
frame_gender = ttk.Frame(root)
frame_gender.grid(row=3, column=0, sticky='W', padx=10, pady=5)

# Define gender options
genders = (('Male', 'M'), ('Female', 'F'), ('Other', 'O'))

# Create a radio button for each gender option
for index, gender in enumerate(genders):
    radio = ttk.Radiobutton(frame_gender, text=gender[0], value=gender[1], variable=selected_gender)
    radio.grid(row=0, column=index, padx=5, sticky='W')

# --- Newsletter Checkbox ---
check_newsletter = ttk.Checkbutton(root, text='I wish to receive emails.', variable=newsletter_var)
check_newsletter.grid(row=4, column=0, padx=15, pady=5, sticky='W')

# --- Confirmation Button ---
button_confirm = ttk.Button(root, text='Confirm', command=register)
button_confirm.grid(row=5, column=0)

# --- Label for displaying messages (confirmation or error) ---
label_confirmation = ttk.Label(root, text='')
label_confirmation.grid(row=6, column=0)

# --- Start Tkinter main loop ---
root.mainloop()