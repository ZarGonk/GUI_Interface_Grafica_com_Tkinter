import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Combobox Example')
        self.geometry('300x200')

        self.selected_items = tk.StringVar()

        self.label = tk.Label(self, text="Select an item from the list:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.combobox = ttk.Combobox(self, textvariable=self.selected_items, values=[
            'Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'
        ])
        self.combobox.grid(row=1, column=0, padx=10, pady=10)

        self.combobox.current(0)  # set the selected item

if __name__ == "__main__":
    app = App()
    app.mainloop()