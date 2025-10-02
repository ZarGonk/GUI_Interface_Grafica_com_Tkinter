import tkinter as tk
from tkinter import ttk

def show_answer():
    style = ttk.Style()
    if selected.get() == 'Roger':
        result_text.config(text='Correct! Gol D. Roger is the king of the pirates')
        style.configure('Custom.TLabel', background= 'Green')
    else:
        result_text.config(text=f'Wrong! {selected.get()} is not the King of the pirates')
        style.configure('Custom.TLabel', background= 'Red')

# Main Window
root = tk.Tk()
root.title('CheckButton 1')
root.geometry('300x200')
root.resizable(True, True) 

text_label = ttk.Label(root, text="Who is known as the 'Pirate King' in One Piece?")
text_label.grid(row=0, column=0, padx=10, pady=4)

selected = tk.StringVar()

answers = (('Monkey D. Luffy', 'Luffy'),
('Barba Negra', 'Teach'),
('Edward Newgate', 'Newgate'),
('Gol D. Roger', 'Roger'))

frame = ttk.Frame(root)
frame.grid(row=1, column=0,padx=15, pady=4, sticky='W')

for answer in answers:
    r = ttk.Radiobutton(frame, text=answer[0], value=answer[1], variable=selected)
    r.grid(sticky='W')

button = ttk.Button(root, text='Check', command=show_answer)
button.grid(row=2, column=0)

result_text = ttk.Label(root, text='Resposta', wraplength=300, justify='center', style='Custom.TLabel')
result_text.grid(row=3, column=0, pady=15)

# Start the Tkinter event loop
root.mainloop()