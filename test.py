import tkinter as tk

root = tk.Tk()
root.title('Janela')

root.geometry('300x200+50+50')
# root.resizable(False, True)

# Define tamanho minimo da janela
root.minsize(300, 200)
# Define tamanho maximo da janela
root.maxsize(600, 400)

# Defini nivel de transparencia
root.attributes('-alpha', 1)

# Alteração de icon da janela

root.iconbitmap('assets/pythontutorial-1-150x150.ico')


root.mainloop()