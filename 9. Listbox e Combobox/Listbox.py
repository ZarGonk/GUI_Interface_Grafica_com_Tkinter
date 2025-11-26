import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Listbox Example')
        self.geometry('300x200')

        self.items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

        self.list_variable = tk.Variable(value=self.items)

        self.label = tk.Label(self, text="Select an item from the list:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.listbox = tk.Listbox(self, listvariable=self.list_variable, height=5)
        self.listbox.grid(row=1, column=0, padx=10, pady=10) 


if __name__ == "__main__":
    app = App()
    app.mainloop()