import tkinter as tk
from datetime import date

# Function to display today's date in the Label
def show_date():
    today = date.today()                       # Get today's date
    text_date.set(today.strftime('%d/%m/%y')) # Format the date and update the StringVar

# Create the main application window
root = tk.Tk()
root.title('Button Example')
root.geometry('300x200')

# Create a StringVar to store the Label text dynamically
text_date = tk.StringVar()  # Initially empty

# Create a Label widget linked to the StringVar
lbl_date = tk.Label(
    root, 
    textvariable=text_date,    # Link the Label text to the StringVar
    font=('Times New Roman', 14)
)
lbl_date.pack(pady=20)

# Create a Button widget to show the date
button_date = tk.Button(
    root,
    text='Show Date',          # Button text
    command=show_date,         # Function executed when clicked
    bg='blue',                 # Background color
    fg='white'                 # Text color
)
button_date.pack(pady=10)

# Start the Tkinter event loop (keeps the window open)
root.mainloop()