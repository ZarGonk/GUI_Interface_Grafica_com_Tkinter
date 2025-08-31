import tkinter as tk
from tkinter import ttk

def convert_distance(unit):
    try:
        km = float(entry.get())

        # Conversões
        conversions = {
            "m": km * 1000,
            "dm": km * 10000,
            "cm": km * 100000,
            "mm": km * 1000000
        }

        result = conversions[unit]
        text.config(
            text=f"{km} Km = {result:.2f} {unit}",
            font=("Arial", 12, "bold"),
            bg="LightBlue",
            fg="Green"
        )
    except ValueError:
        text.config(
            text="Erro! Invalid Entry",
            font=("Arial", 12, "bold"),
            fg="Red",
            bg="LightBlue"
        )


# Main Window
root = tk.Tk()
root.title("Distance Converter")
root.config(bg="lightblue")
root.geometry("350x220")

# Title
message = tk.Label(
    root,
    text="Distance Converter",
    font=("Helvetica", 15, "bold"),
    bg="lightblue"
)
message.pack(pady=5)

# Instruction
text_converter = tk.Label(
    root,
    text="Enter the kilometers:",
    font=("Arial", 11),
    bg="lightblue"
)
text_converter.pack()

# Entry
entry = tk.Entry(root, foreground="blue", font=("Arial", 11))
entry.pack(pady=3)

# Buttons
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=15)

ttk.Button(frame, text="Meter", command=lambda: convert_distance("m")).pack(side="left", padx=5)
ttk.Button(frame, text="Decimeter", command=lambda: convert_distance("dm")).pack(side="left", padx=5)
ttk.Button(frame, text="Centimeter", command=lambda: convert_distance("cm")).pack(side="left", padx=5)
ttk.Button(frame, text="Millimeter", command=lambda: convert_distance("mm")).pack(side="left", padx=5)

# Result
text = tk.Label(root, text="", bg="lightblue", font=("Arial", 12))
text.pack(pady=10)

root.mainloop()
