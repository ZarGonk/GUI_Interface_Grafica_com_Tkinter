import tkinter as tk
from tkinter import ttk, PhotoImage

def center_image(event=None):
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    image_width = photo.width()
    image_height = photo.height()

    pos_x = (window_width - image_width) // 2
    pos_y = (window_height - image_height) // 2

    lbl_photo.place(x=pos_x, y=pos_y)


# Main window
root = tk.Tk()
root.geometry('300x200')
root.title('Centering Image')

# Load Image
photo = PhotoImage(file='assets/python.png')

# Create Label and display image
lbl_photo = ttk.Label(root, image=photo)

# Center image when opening and resizing window
root.bind("<Configure>", center_image)

# Initial centering
center_image()

root.mainloop()
