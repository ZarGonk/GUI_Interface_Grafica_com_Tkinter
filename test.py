import tkinter as tk
from tkinter import ttk

# Cria a janela principal
janela = tk.Tk()
janela.title("Exemplo de StringVar com Entry e Label")
janela.geometry("400x200")

# 1. Cria o StringVar
texto_digitado_var = tk.StringVar()
texto_digitado_var.set("Digite algo aqui...") # Define um valor inicial

# 2. Cria e associa os widgets
ttk.Label(janela, text="Escreva seu nome:").pack(pady=5)

# O Entry atualiza o StringVar
entrada_nome = ttk.Entry(janela, textvariable=texto_digitado_var, width=40)
entrada_nome.pack(pady=5)

ttk.Label(janela, text="O que você está digitando:").pack(pady=10)

# O Label lê o StringVar e se atualiza automaticamente
label_espelho = ttk.Label(janela, textvariable=texto_digitado_var, font=("Helvetica", 12))
label_espelho.pack(pady=5)

janela.mainloop()