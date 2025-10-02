import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Criar um estilo personalizado
style = ttk.Style()
style.theme_use("clam")  # "clam" permite mais personalização

# Configurar o estilo com cores específicas
style.configure("Custom.TButton",
                background="lightblue",
                foreground="black",
                borderwidth=1,
                focusthickness=3,
                focuscolor='none')

style.map("Custom.TButton",
          background=[("active", "blue"), ("pressed", "green")],
          foreground=[("active", "white"), ("pressed", "black")])


# Aplicar o estilo ao botão
btn = ttk.Button(root, text="Clique aqui", style="Custom.TButton")
btn.pack(padx=20, pady=20)


root.mainloop()
