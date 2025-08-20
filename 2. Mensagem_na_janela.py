import tkinter as tk

root = tk.Tk() # Create Window

root.geometry('300x200') # Sets a size for the screen

root.title('Mostrando Mensagem') # Give the app a title

# Create Widget (Text)
message = tk.Label(
    root, 
    text='Hello, World!', # Message to be displayed
    font = ('times new roman', 15)) # Font type and font size
message.pack() # Adds the Label to the window

root.mainloop() # Keep the window open