import tkinter as tk

def abrir_janela():
    root2 = tk.Tk()
    root2.mainloop()

root = tk.Tk()
root.geometry('300x200')
root.title('Hello, World!')

message = tk.Label(root, text='Hello World')
message.pack()

button = tk.Button(root, text='Click', command=abrir_janela)
button.pack()

root.mainloop()