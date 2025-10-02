import tkinter as tk
from tkinter import ttk

sequence = []  # Stores the counting sequence

def show_count():
    """Starts counting based on user input."""
    start_button.config(state='disabled')  # Disable button during counting
    try:
        start = int(value_1.get())
        end   = int(value_2.get())
        step  = int(value_3.get())

        # Validation
        if step == 0:
            text_result.config(text='Step cannot be 0')
            start_button.config(state='normal')
            return
        if end < start and step > 0:
            step = -step  # Auto-invert step if direction is wrong

        def count(i):
            """Recursive counting using root.after() for delay."""
            if (step > 0 and i <= end) or (step < 0 and i >= end):
                text_count.config(text=f'{i}')
                sequence.append(str(i))
                root.after(300, lambda: count(i + step))
            else: 
                result = ' -> '.join(sequence)
                text_result.config(text=result)
                start_button.config(state='normal')  # Re-enable button

        # Reset before starting
        text_result.config(text='')
        sequence.clear()
        count(start)

    except ValueError:
        text_result.config(text='Invalid Value')
        start_button.config(state='normal')
    except Exception as e:
        print(e)
        start_button.config(state='normal')


# --- Main Window ---
root = tk.Tk()
root.title('Counter')
root.geometry('300x200')
root.resizable(True, True) 

style = ttk.Style()
style.configure('Custom.TLabel')

# Instruction
text_label = ttk.Label(root, text='Choose start, end, and step:')
text_label.grid(row=0, column=0, pady=5)

# Input Frame
frame = tk.Frame(root)
frame.grid(row=1, column=0, sticky='W', padx=10, pady=2)

# Labels
ttk.Label(frame, text='Start:').grid(row=0, column=0)
ttk.Label(frame, text='End:').grid(row=1, column=0)
ttk.Label(frame, text='Step:').grid(row=2, column=0)

# Input Variables
value_1 = tk.IntVar(value=0)
value_2 = tk.IntVar(value=0)
value_3 = tk.IntVar(value=0)

# Entry Fields
entry_1 = ttk.Entry(frame, textvariable=value_1, width=10)
entry_2 = ttk.Entry(frame, textvariable=value_2, width=10)
entry_3 = ttk.Entry(frame, textvariable=value_3, width=10)

entry_1.grid(row=0, column=1, padx=5, pady=2)
entry_1.focus()
entry_2.grid(row=1, column=1, padx=5, pady=2)
entry_3.grid(row=2, column=1, padx=5, pady=2)

# Start Button
start_button = ttk.Button(root, text='Start', command=show_count)
start_button.grid(row=2, column=0, pady=5)

# Current Count Display
text_count = ttk.Label(root, text='0', font=('Arial', 20, 'bold'), foreground='blue')
text_count.grid(row=1, column=1)

# Result Label
text_result = ttk.Label(root, text='', wraplength=230, justify='center', style='Custom.TLabel')
text_result.grid(row=3, column=0, sticky='WE', pady=10)

# Start the Tkinter event loop
root.mainloop()