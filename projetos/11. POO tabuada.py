import tkinter as tk
from tkinter import ttk

class MultiplicationTable(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main window configuration
        self.title('Multiplication Table')
        self.geometry('300x350')
        self.resizable(True, True)

        # Configure grid weights for responsive layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)  # linha extra para o Sizegrip

        # Title label
        self.text_label = ttk.Label(
            self,
            text='Multiplication Table',
            font=('Times New Roman', 16, 'bold'),
            anchor='center'
        )
        self.text_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='WE')

        # Label that requests the number
        self.text_number = ttk.Label(self, text='Enter a number:')
        self.text_number.grid(row=1, column=0, padx=(10, 5), pady=5, sticky='E')

        # Entry that retrieves the number
        self.entry_number = ttk.Entry(self, width=10)
        self.entry_number.grid(row=1, column=1, padx=(0, 10), pady=5, sticky='W')

        # Button to generate the multiplication table
        self.button_generate = ttk.Button(self, text='Generate Table', command=self.generate_table)
        self.button_generate.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky='EW')

        # Label that will display the multiplication table result
        self.text_result = ttk.Label(self, text='', justify='left', font=('Courier New', 12), anchor='nw')
        self.text_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')

        # Add Sizegrip properly
        sizegrip = ttk.Sizegrip(self)
        sizegrip.grid(row=4, column=1, sticky='SE')

    def generate_table(self):
        """Generate and display the multiplication table for the entered number."""
        try:
            number = int(self.entry_number.get())
            # largura fixa para alinhar os elementos
            table = '\n'.join([f'{number:>2} x {i:<2} = {number * i:<3}' for i in range(1, 11)])
            self.text_result.config(text=table)
        except ValueError:
            self.text_result.config(text='Please enter a valid integer.')


if __name__ == '__main__':
    app = MultiplicationTable()
    app.mainloop()