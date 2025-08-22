import tkinter as tk

# Function to update the second label when the button is clicked
def click():
    message2['text'] = 'Button was clicked'  # Update the text of message2

# Create the main application window
root = tk.Tk()
root.title('Button Example')
root.geometry('300x200')

# Create the first Label with instructions
message = tk.Label(
    root,
    text='Click the Button',          # Instruction message
    font=('Arial', 12)
)
message.pack()

# Create a Button and link it to the click function
button = tk.Button(root, text='Click', command=click)
button.pack()

# Create the second Label to show the status of the button
message2 = tk.Label(
    root,
    text='Button has not yet been clicked'  # Initial status message
)
message2.pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()