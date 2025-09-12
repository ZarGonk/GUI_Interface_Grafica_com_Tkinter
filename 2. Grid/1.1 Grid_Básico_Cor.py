import tkinter as tk

# Main Window
root = tk.Tk()
root.title('Grid')

# Creating labels in different cells
tk.Label(root, text="Row 0: Column 0", background='Red').grid(row=0, column=0)
tk.Label(root, text="Row 0: Column 1", background='Blue').grid(row=0, column=1)
tk.Label(root, text="Row 1: Column 0", background='Green').grid(row=1, column=0)
tk.Label(root, text="Row 1: Column 1", background='Yellow').grid(row=1, column=1)

# Show the Window
root.mainloop()