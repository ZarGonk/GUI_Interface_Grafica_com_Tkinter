import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title('Centering Window')

# Define the window dimensions
window_width = 400
window_height = 200

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center point (so the window appears in the middle of the screen)
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the size and position of the window (centered on the screen)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Start the Tkinter event loop (keeps the window open)
root.mainloop()