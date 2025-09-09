import tkinter as tk

root = tk.Tk()
root.title("Exemplo 2 - Alterando valores")

contador = tk.IntVar(value=0)  # começa em 0

def aumentar():
    contador.set(contador.get() + 1)

def diminuir():
    contador.set(contador.get() - 1)

label = tk.Label(root, textvariable=contador, font=("Arial", 20))
label.pack(pady=10)

btn1 = tk.Button(root, text="Aumentar", command=aumentar)
btn1.pack(side="left", padx=10)

btn2 = tk.Button(root, text="Diminuir", command=diminuir)
btn2.pack(side="right", padx=10)

root.mainloop()
