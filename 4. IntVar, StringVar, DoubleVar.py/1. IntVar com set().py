import tkinter as tk

root = tk.Tk()
root.title("Exemplo 1 - IntVar Básico")

numero = tk.IntVar()   # cria a caixinha de número

# define um valor inicial
numero.set(10)

def mostrar():
    print("O valor atual é:", numero.get())

btn = tk.Button(root, text="Mostrar valor", command=mostrar)
btn.pack(pady=10)

root.mainloop()
