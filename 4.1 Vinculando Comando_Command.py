import tkinter as tk
from tkinter import ttk

# --- Widgets can respond to events such as ---
# Mouse clicks
# Key presses

# Create the main application window
root = tk.Tk()
root.title('Command / Event')

# Function to be called when the button is clicked
def button_click():
    print('Button Clicked')  # Prints a message to the console

# Create a Button widget and link it to the function via the 'command' option
button = ttk.Button(
    root,
    text='Click Me',
    command=button_click   # Function executed when the button is clicked
).pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()