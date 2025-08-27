import tkinter as tk
from tkinter import ttk

def validation_age():
    try:
        year = int(input('Digite Idade: '))
        if year > 18:
            print('Maior de Idade')
        else:
            print('menor de idade')
    
    except ValueError:
        print('Dado informado Invalido')


# Main Window
root = tk.Tk()
root.title('Age Validation')

try:
    photo = tk.PhotoImage(file='Projetos/assets/age-icon-2.png')
    root.iconphoto(False, photo)
except tk.TclError:
    print('Icon file not found')

# Create Text Label
message = ttk.Label(root, text='Age Validation', font=('Times New Roman', 15), foreground='red')
message.pack(pady=4)

# Button
age_button = ttk.Button(root, text='Verificar', command=validation_age)
age_button.pack(pady=10)




root.mainloop()