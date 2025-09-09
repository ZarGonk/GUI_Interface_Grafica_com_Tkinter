import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Example with Multiple Frames')
root.geometry('400x300')
root.configure(bg="#96FBFB")

# ----- TOP FRAME -----
frame_top = tk.Frame(root, bg='lightblue', bd=3, relief='ridge')
frame_top.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

label_top = tk.Label(frame_top, text='I am the TOP Frame', bg='lightblue')
label_top.pack(padx=5, pady=5)

# ----- MIDDLE FRAME -----
frame_middle = tk.Frame(root, bg='lightgreen', bd=3, relief='ridge')
frame_middle.grid(row=1, column=0, padx=10, pady=5, sticky="ewsn")

label_middle = tk.Label(frame_middle, text='This is the MIDDLE Frame', bg='lightgreen')
label_middle.pack(pady=5)

button_middle = ttk.Button(frame_middle, text='Click here')
button_middle.pack(pady=5)

# ----- BOTTOM FRAME -----
frame_bottom = tk.Frame(root, bg='lightyellow', bd=3, relief='ridge')
frame_bottom.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

label_bottom = tk.Label(frame_bottom, text='I am the BOTTOM Frame', bg='lightyellow')
label_bottom.pack(padx=5, pady=5)

# Make the middle frame expand when resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()