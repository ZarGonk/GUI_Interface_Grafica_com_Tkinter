import tkinter as tk

# Main Window
root = tk.Tk()
root.title('Compostamento da janela')
root.geometry('400x200+600+300')

# Sets whethet the window can be resized or not
root.resizable(True, True)

# Sets the minimum size for the window
root.minsize(350, 200)
# Sets the maximum size for the window
root.maxsize(1050, 600)

# Sets the transparency of the window: 0.0 (fully transparent) to 1.0 (fully opaque)
root.attributes('-alpha', 1.0)

root.mainloop()
