import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the window size
root.geometry('300x200')

# Set the window title
root.title('Displaying Message')

# Create a Label widget (text element)
message = tk.Label(
    root,
    text='Hello, World!',          # Text to be displayed
    font=('Times New Roman', 15)   # Font family and size
)

# Add the Label to the window
message.pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()
