import tkinter as tk
from tkinter import ttk

def clear():
    string_var.set('')

def atualizar_maiusculo(*args):
    text_upper.set(string_var.get().upper())

root = tk.Tk()
root.title('StringVar Example')

string_var = tk.StringVar()
text_upper = tk.StringVar()

# Sempre que string_var mudar, atualizar_maiusculo é chamado
string_var.trace("w", atualizar_maiusculo)

entry = ttk.Entry(root, textvariable=string_var)
entry.grid(row=0, column=0, padx=10, pady=5)  

# Espelho normal
label = ttk.Label(root, textvariable=string_var)
label.grid(row=1, column=0, padx=10, pady=5) 

# Espelho em maiúsculo
label_upper = ttk.Label(root, textvariable=text_upper)
label_upper.grid(row=2, column=0, padx=10, pady=5) 

# Botão de limpar
button = ttk.Button(root, text='Clear', command=clear)
button.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
