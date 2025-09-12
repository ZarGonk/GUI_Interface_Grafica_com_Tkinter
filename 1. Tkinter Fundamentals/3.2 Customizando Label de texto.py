import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title('Customizing Text Label')
root.geometry('300x200')

# Create a Label widget with custom styling
message = ttk.Label(
    root,
    text='I am ZarGonk',                 # Text to display
    font=('Times New Roman', 15),        # Font family and size
    foreground='red',                    # Text color
    background='lightgray',              # Background color
    anchor='center',                     # Align text inside the widget
    borderwidth=2,                       # Thickness of the border
    relief='groove'                      # Border style (groove, ridge, sunken, raised, solid, flat)
).pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()