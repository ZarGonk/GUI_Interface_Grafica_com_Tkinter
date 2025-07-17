import tkinter as tk

def open_window():
    root_2 = tk.Toplevel()
    root_2.title('Second Window')
    root_2.config(background= "#EE3C3C")

    #Window Size
    window_width = 300
    window_height = 200

    # Get the dimensions of the screen used
    screen_width= root_2.winfo_screenwidth()
    screen_height = root_2.winfo_screenheight()

    # Calculate the coordinates to center the window 2
    x = int((screen_width - window_width) // 2)
    y = int((screen_height - window_height) // 2)

    # Sets the geometry of the second window
    root_2.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Main Window
root = tk.Tk()
root.title('Main Window')
root.geometry('600x400+600+300')

# Open a second window
root.bind('<Button-1>', lambda event: open_window())

root.mainloop()