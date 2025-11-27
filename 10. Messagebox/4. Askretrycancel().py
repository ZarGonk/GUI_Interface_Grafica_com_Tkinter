import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo

# create the root window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter OK/Retry Dialog')
        self.geometry('300x150')

        # click event handler
        def confirm():
            answer = askretrycancel(
                title='Connection Issue',
                message='The database server is unreachable. Do you want to retry?'
            )
            if answer:
                showinfo(
                    title='Information',
                    message='Attempt to connect to the database again.')


        ttk.Button(
            self,
            text='Connect to the Database Server',
            command=confirm).pack(expand=True)


if __name__ == '__main__':
    app = App()
    app.mainloop()
