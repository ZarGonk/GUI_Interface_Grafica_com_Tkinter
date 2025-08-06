import tkinter as tk
from tkinter import ttk, PhotoImage

def centralizar_imagem(event):
    largura_janela = root.winfo_width()
    altura_janela = root.winfo_height()
    largura_imagem = photo.width()
    altura_imagem = photo.height()

    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2

    lbl_photo.place(x=posicao_x, y=posicao_y)

# main window
root = tk.Tk()
root.geometry('300x200')
root.title('Centralizando Imagem')

#Load Photo
photo= PhotoImage(file='assets/python.png')

# Create Label and display photo
lbl_photo= ttk.Label(root, image= photo)

# Centralizar imagem ao redimensionar janela
root.bind("<Configure>", centralizar_imagem)

# Inserir o label na janela
centralizar_imagem()


root.mainloop()