import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    """Calculate BMI and update the label with the result."""
    try:
        bmi = weight.get() / (height.get()**2)
        text_result.config(text=f'Your BMI is {bmi:.2f}')
    except ZeroDivisionError:
        text_result.config(text='Height cannot be 0')
    except Exception as e:
        text_result.config(text=f'Error: {e}')

# Main Window
root = tk.Tk()
root.title('BMI Calculator')  # Changed from "Calcular IMC" to English
root.geometry('300x200')
root.resizable(True, True) 

# Instruction Label
text_label = ttk.Label(root, text='Calculate your BMI')
text_label.grid(row=0, column=0, padx=10, pady=2)

# Variables for weight and height
weight = tk.DoubleVar()
height = tk.DoubleVar()

# Frame to organize inputs
frame = ttk.Frame(root)
frame.grid(row=1, column=0)

# Labels for inputs
text_1 = ttk.Label(frame, text='Weight (kg):')
text_2 = ttk.Label(frame, text='Height (m):')

text_1.grid(row=0, column=0)
text_2.grid(row=1, column=0)

# Entry fields
entry_1 = ttk.Entry(frame, textvariable=weight, width=10)
entry_2 = ttk.Entry(frame, textvariable=height, width=10)

entry_1.grid(row=0, column=1, padx=5, pady=2)
entry_2.grid(row=1, column=1, padx=5, pady=2)

# Button to calculate BMI
button = ttk.Button(root, text='Calculate', command=calculate_bmi)
button.grid(row=2, column=0)

# Result Label
text_result = ttk.Label(root, text='')
text_result.grid(row=3, column=0)

# Start the Tkinter event loop
root.mainloop()