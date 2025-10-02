import tkinter as tk
from tkinter import ttk

# Function to show the selected size
def show_selected_size():
    result = selected.get()  # Get the selected value (S, M, L, XL, XXL)
    text_label.config(text=result)

# --- Main Window ---
root = tk.Tk()
root.title('Radiobutton Example')   # Melhor que "CheckButton 1"
root.geometry('300x200')
root.resizable(True, True) 

# StringVar to store the selected size
selected = tk.StringVar()

# Title label
label = tk.Label(text="What's your T-shirt size?")
label.grid(row=0, column=0, padx=10, pady=2)

# Options for T-shirt sizes
sizes = (
    ('Small', 'S'),
    ('Medium', 'M'),
    ('Large', 'L'),
    ('Extra Large', 'XL'),
    ('Extra Extra Large', 'XXL')
)

# Frame to hold the radiobuttons
frame = tk.Frame(root)
frame.grid(row=1, column=0, padx=5, pady=2)

# Create radiobuttons for each size
for size in sizes:
    r = ttk.Radiobutton(frame, text=size[0], value=size[1], variable=selected)
    r.grid(sticky='W', padx=5, pady=2)

# Button to confirm the selection
button = ttk.Button(root, text='Get Selected Size', command=show_selected_size)
button.grid(row=2, column=0, pady=5)

# Label to display the result
text_label = tk.Label(root, text='', foreground="blue")
text_label.grid(row=3, column=0, pady=5)

# Start the Tkinter event loop
root.mainloop()