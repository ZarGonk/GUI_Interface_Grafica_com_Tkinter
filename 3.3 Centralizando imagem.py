import tkinter as tk
from tkinter import ttk, PhotoImage

def center_image(event=None):
    """
    Centers the image inside the window by calculating
    the available width and height compared to the image size.
    """
    window_width = root.winfo_width()    # Current window width
    window_height = root.winfo_height()  # Current window height
    image_width = photo.width()          # Image width
    image_height = photo.height()        # Image height

    # Calculate center position
    pos_x = (window_width - image_width) // 2
    pos_y = (window_height - image_height) // 2

    # Place the image label at the calculated position
    lbl_photo.place(x=pos_x, y=pos_y)

# Create the main application window
root = tk.Tk()
root.geometry('300x200')   # Initial window size
root.title('Centering Image')

# Load an image (PhotoImage supports .png, .gif, .ppm)
photo = PhotoImage(file='assets/python.png')

# Create a Label widget to display the image
lbl_photo = ttk.Label(root, image=photo)

# Re-center the image automatically when the window is resized
root.bind("<Configure>", center_image)

# Center the image when the window first opens
center_image()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()
