import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('IntVar')
root.geometry('250x100')

# Criando um IntVar (caixinha especial que guarda números inteiros)
# Ele vai ficar sincronizado com o Entry
var_number = tk.IntVar()

# Função chamada pelo botão
def show():
    # Pega o valor atual do IntVar (o que foi digitado no Entry)
    # Mostra esse valor dentro do Label
    show_number['text'] = var_number.get()

# Entry conectado ao IntVar através do textvariable
# Tudo que for digitado no Entry vai atualizar automaticamente o var_number
entry_number = ttk.Entry(root, textvariable=var_number)
entry_number.grid(row=0, column=0, padx=10, pady=5)

# Botão que, quando clicado, chama a função show()
button = ttk.Button(root, text='Show Number', command=show)
button.grid(row=0, column=1, padx=5, pady=5)

# Label que vai exibir o valor do IntVar depois que o botão for clicado
show_number = tk.Label(root, text='', foreground='Green')
show_number.grid()

root.mainloop()
