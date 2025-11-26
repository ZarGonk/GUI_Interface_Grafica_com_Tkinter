import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Play')
        self.geometry('300x200')

        option = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5 }

        self.button_1 = ttk.Button(self, text='Show an error', command=lambda: showerror(title='Error', message='This is an erro')).pack(**option)

        self.button_2 = ttk.Button(self, text='Show an information', command=lambda: showinfo(title='Information', message='This is an Information')).pack(**option)

        self.button_3 = ttk.Button(self, text='Show an warning', command=lambda: showwarning(title='Warning', message='This is an Warning')).pack(**option)



if __name__ == "__main__":
    app = App()
    app.mainloop()

