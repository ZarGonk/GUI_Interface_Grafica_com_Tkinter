import tkinter as tk

# Main Window
root = tk.Tk()
root.geometry('300x200')
root.title('test')

# Create Label
label = tk.Label(
    root,
    text = 'Hello World',
    font = ('Times Roman', 15),
    fg ='blue', # Color Letter
    bg= 'Black' # Color BackGround Letter
    
).pack()

root.mainloop()