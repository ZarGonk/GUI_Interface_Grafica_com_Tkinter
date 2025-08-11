import tkinter as tk

# Main Window
root = tk.Tk()
root.geometry('300x200') # Sets a size for the screen

root.title('Mostrando Imagem')

# Create Label Text
message = tk.Label(
    root,
    text='Image below',
    font= ('Times New Roman', 14),
    fg='red'
)
message.pack()

# Create Label Photo
photo = tk.PhotoImage(file='assets/python.png')
image_label = tk.Label(
    root, 
    image=photo,
    text='Python',
    compound=tk.TOP
)
image_label.pack()

root.mainloop()