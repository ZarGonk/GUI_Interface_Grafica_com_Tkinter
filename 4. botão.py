import tkinter as tk

def click():
    message2['text'] = 'Button was clicked'

# Main Window
root = tk.Tk()
root.title('Button')
root.geometry('300x200')

# Create Label Message
message = tk.Label(
    root,
    text='Click The Button',
    font=('Arial', 12)
)
message.pack()

# Create Button
button = tk.Button(root, text='Click', command=click)
button.pack()

# Create Second Label Message
message2 = tk.Label(
    root,
    text='Button has not yet beet clicked'
)
message2.pack()

root.mainloop()