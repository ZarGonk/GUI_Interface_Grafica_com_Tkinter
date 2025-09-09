import tkinter as tk

# Main Window
root = tk.Tk()
root.title('Frame')
root.geometry('300x200')
root.config(bg='Lightblue')

# In Tkinter, a Frame is like a box or container used to organize other widgets 
# (buttons, labels, entries, etc.) inside the main window. 
# It does not appear on its own with functionalities (like a button or label), 
# but it helps structure the interface. 
frame = tk.Frame(root, bg='green', bd=2, relief='groove')
# bg → background color
# bd → border thickness
# relief → border style (flat, raised, sunken, groove, ridge)
# width and height → width and height of the frame
frame.grid(row=0, column=0, sticky='EW')
tk.Label(frame, text='Frame', background='green').pack()

# Configure grid expansion
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Show the window
root.mainloop()