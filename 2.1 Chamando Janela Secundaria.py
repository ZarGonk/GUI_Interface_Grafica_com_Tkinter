import tkinter as tk

def open_window():
    # Create a second window using Toplevel
    root_2 = tk.Toplevel()
    root_2.title('Second Window')
    root_2.config(background="#EE3C3C")

    # Window dimensions
    window_width = 300
    window_height = 200

    # Get the dimensions of the screen
    screen_width = root_2.winfo_screenwidth()
    screen_height = root_2.winfo_screenheight()

    # Calculate coordinates to center the second window
    x = int((screen_width - window_width) // 2)
    y = int((screen_height - window_height) // 2)

    # Set the size and position of the second window
    root_2.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Create the main window
root = tk.Tk()
root.title('Main Window')
root.geometry('600x400+600+300')

# Bind left mouse click to open the second window
root.bind('<Button-1>', lambda event: open_window())

# Start the Tkinter event loop (keeps the window open)
root.mainloop()