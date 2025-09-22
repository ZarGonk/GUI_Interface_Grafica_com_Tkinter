import tkinter as tk
from tkinter import messagebox

# Função que coleta os ingredientes selecionados
def confirmar_pedido():
    ingredientes = []
    if queijo.get(): ingredientes.append("Queijo")
    if calabresa.get(): ingredientes.append("Calabresa")
    if tomate.get(): ingredientes.append("Tomate")
    if cebola.get(): ingredientes.append("Cebola")
    if azeitona.get(): ingredientes.append("Azeitona")
    
    pedido = ", ".join(ingredientes) if ingredientes else "Nenhum ingrediente selecionado"
    messagebox.showinfo("Pedido Confirmado", f"Você escolheu: {pedido}")

# Janela principal
root = tk.Tk()
root.title("Monte sua Pizza")

# Variáveis de controle dos Checkbuttons
queijo = tk.BooleanVar()
calabresa = tk.BooleanVar()
tomate = tk.BooleanVar()
cebola = tk.BooleanVar()
azeitona = tk.BooleanVar()

# Checkbuttons
tk.Checkbutton(root, text="Queijo", variable=queijo).pack()
tk.Checkbutton(root, text="Calabresa", variable=calabresa).pack()
tk.Checkbutton(root, text="Tomate", variable=tomate).pack()
tk.Checkbutton(root, text="Cebola", variable=cebola).pack()
tk.Checkbutton(root, text="Azeitona", variable=azeitona).pack()

# Botão de confirmação
tk.Button(root, text="Confirmar Pedido", command=confirmar_pedido).pack(pady=10)

root.mainloop()
