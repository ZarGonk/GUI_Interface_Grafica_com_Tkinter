# Importar as bibliotecas 
import tkinter as tk
from tkinter import ttk
from random import randint

# Criar uma função para contar os clicks
color = ''
count = 0
def click():
    global count
    count +=1
    message['text'] = f'You Clicked {count} times'
    if count % 10 == 0:
        global color
        color = color_hex_random()
        root.config(bg=color)
    return message['text'] 

# Criar uma função para decrementar os click
def decrement():
    global count
    count -= 1
    message['text'] = f'You Clicked {count} times'
    
    return message['text']

# Criar uma função para resetar o contador
def reset():
    global count 
    count = 0
    message['text'] = 0
    return message['text']

# Gerador de cor aleatoria 
def color_hex_random():
    return '#{:06x}'.format(randint(0, 0xFFFFFF))

# Cria uma janela
root = tk.Tk()
root.title('Button Click')
root.config(background='lightblue')
root.geometry('280x150')

#Crial um label de instrução
instruction = tk.Label(
    root,
    text='Click Counter',
    font=('Times New Roman', 15, 'italic'),
    bg='lightblue'
)
instruction.pack(pady=10)

# Alinhar os bottons
frame = tk.Frame(root, bg='lightblue')
frame.pack(pady=15)


# Criar um Button para clicar e contar a quantia de click
button_click = ttk.Button(
    frame,
    text='Count',
    command=click)
button_click.pack(side= 'left', padx=5)

button_decrement = ttk.Button(
    frame,
    text='Decrement',
    command=decrement
)
button_decrement.pack(side='left', padx=5)


# Criar um Button para resetar a contagem
button_reset = ttk.Button(
    frame,
    text='Reset',
    command=reset
)
button_reset.pack(side='left', padx=5)

# Criar um Label para exibir o numero de clicks
message = tk.Label(
    root,
    text='0',
    font=('Arial',12, 'bold'),
    fg='Red',
    bg='lightblue'
)
message.pack()

root.mainloop()