import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the window title
root.title('Window Behavior')

# Set the initial size and position of the window: 'widthxheight+x_offset+y_offset'
root.geometry('400x200+600+300')

# Allow the window to be resized: (width_resizable, height_resizable)
root.resizable(True, True)

# Set the minimum window size
root.minsize(350, 200)

# Set the maximum window size
root.maxsize(1050, 600)

# Set the window transparency: 0.0 (fully transparent) to 1.0 (fully opaque)
root.attributes('-alpha', 1.0)

# Open the window maximized (commented as string in your code, corrected here)
# root.state('zoomed')

# Load and set the window icon (must be .ico format on Windows)
root.iconbitmap('assets/pythontutorial-1-150x150.ico')

# Set the background color of the window
root.config(background='lightblue')

# Start the Tkinter event loop (keeps the window open)
root.mainloop()
