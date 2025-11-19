import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        # Inicializa a classe Tk (janela principal)
        super().__init__()

        # -------------------------------------------------
        # Basic window configuration
        # -------------------------------------------------

        # Title of the window
        self.title('Window Behavior')

        # Size and initial screen position: width x height + offsetX + offsetY
        self.geometry('400x200+600+300')

        # Whether the window can be resized (horizontal, vertical)
        self.resizable(True, True)

        # If you want, here is the best place to call a method
        # that creates widgets (recommended in OOP)
        self.create_widgets()

    def create_widgets(self):
        """Create and organize all widgets inside the window."""
        label = tk.Label(self, text="This is an example window.", font=("Arial", 12))
        label.pack(pady=20)

        button = tk.Button(self, text="Click me!", command=self.on_click)
        button.pack()

    def on_click(self):
        """Callback function for the button."""
        print("Button clicked!")


if __name__ == "__main__":
    window = Window()
    window.mainloop()