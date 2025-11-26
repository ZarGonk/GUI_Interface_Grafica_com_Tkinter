import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # --- Window configuration ---
        self.title('Fruit List')
        self.geometry('300x200')
        self.configure(background='lightblue')

        # Configure ttk style to match the window background
        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='lightblue')
        
        # Title label
        self.label = ttk.Label(
            self, 
            text='Choose a Fruit', 
            font=('Times New Roman', 15), 
            justify='center',
            anchor='center'
        )
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # List of fruits
        fruits = [
            'Pineapple', 'Banana', 'Cashew', 'Apricot', 'Fig',
            'Guava', 'Jabuticaba', 'Kiwi', 'Orange', 'Mango',
            'Nectarine', 'Olive', 'Pear', 'Quince', 'Pomegranate'
        ]

        # Variable that populates the Listbox
        list_fruits = tk.Variable(value=fruits)
        
        # Listbox showing multiple fruits (allows multiple selections)
        self.listbox = tk.Listbox(
            self, 
            listvariable=list_fruits,
            height=6, 
            selectmode='multiple'
        )
        self.listbox.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Event that triggers when the user selects items
        self.listbox.bind('<<ListboxSelect>>', self.handle_selection)

        # Label that displays the selected fruits
        self.result_label = ttk.Label(
            self, 
            text='', 
            font=('Times New Roman', 12), 
            justify='center', 
            anchor='center'
        )
        self.result_label.grid(row=2, column=0, padx=10, pady=10)

        # Make column stretchable
        self.columnconfigure(0, weight=1)

    def handle_selection(self, event):
        """Update the label with the selected fruits."""
        selected_indices = self.listbox.curselection()  # Get selected index positions
        selected_fruits = [self.listbox.get(i) for i in selected_indices]  # Get fruit names

        # If nothing selected, show a default text
        text = (
            'No fruit selected'
            if not selected_fruits
            else 'Selected fruits: ' + ', '.join(selected_fruits)
        )

        # Update the label with the text
        self.result_label.config(text=text)


if __name__ == "__main__":
    app = App()
    app.mainloop()
