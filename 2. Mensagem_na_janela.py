import tkinter as tk

root = tk.Tk() # Cria a janela

root.geometry('300x200') # Define um tamanho para a tela 

root.title('Mostrando Mensagem') # Da um titulo para o app

# Cria um Widget
message = tk.Label(
    root, 
    text='Hello, World!', # Mensagem a ser mostrada
    font = ('times new roman', 15)) # Fonte e tamanho
message.pack() # Adiciona o Label à janela

root.mainloop() # Mantem a janela aberta