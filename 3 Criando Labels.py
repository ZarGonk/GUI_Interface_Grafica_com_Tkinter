import tkinter as tk

# Create the main application window
root = tk.Tk()
root.geometry('300x200')  # Set the window size
root.title('Displaying Image')

# Create a Label with text
message = tk.Label(
    root,
    text='Image below',                 # Text to be displayed
    font=('Times New Roman', 14),       # Font family and size
    fg='red'                            # Text color
)
message.pack()

# Load an image (must be a .png, .gif, or .ppm for PhotoImage)
photo = tk.PhotoImage(file='assets/python.png')

# Create a Label with both text and image
image_label = tk.Label(
    root,
    image=photo,                        # Image to display
    text='Python',                      # Text displayed together with the image
    compound=tk.TOP                     # Places text above the image
)
image_label.pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()