import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Listbox Example')
        self.geometry('200x250')
        self.resizable(True, True)
        self.configure(bg='lightblue')
        
        self.label = tk.Label(self, text='Select a programming language:', bg='lightblue')
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.languages = ('Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Go', 'Swift')

        self.list_variable = tk.Variable(value=self.languages)

        self.listbox = tk.Listbox(self, cnf={}, listvariable=self.list_variable, height=7, selectmode=tk.MULTIPLE)
        self.listbox.grid(row=1, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()