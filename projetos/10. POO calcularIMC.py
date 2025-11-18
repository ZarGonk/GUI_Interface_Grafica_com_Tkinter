import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):
    def __init__(self, container, result_label):
        super().__init__(container)

        # Reference to the result label in the main app
        self.result_label = result_label

        # Variables for weight and height
        self.weight = tk.DoubleVar()
        self.height = tk.DoubleVar()


        # Labels for inputs
        self.text_weight = ttk.Label(self, text='Weight (kg):')
        self.text_weight.grid(row=0, column=0)
        
        self.text_height = ttk.Label(self, text='Height (m):')
        self.text_height.grid(row=1, column=0)

        # Entry fields
        self.entry_weight = ttk.Entry(self, textvariable= self.weight, width=10)
        self.entry_weight.grid(row=0, column=1, padx=5, pady=2)

        self.entry_height = ttk.Entry(self, textvariable= self.height, width=10)
        self.entry_height.grid(row=1, column=1, padx=5, pady=2)

    def calculate_bmi(self):
        """
        Calculate BMI using user's input.
        Updates the result label with the value or an error message.
        """
        try:
            bmi = self.weight.get() / (self.height.get()**2)
            self.result_label.config(text=f'Your BMI is {bmi:.2f}')
        except ZeroDivisionError:
            self.result_label.config(text='Height cannot be 0')
        except Exception as e:
            self.result_label.config(text=f'Error: {e}')


class BMICalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('BMI Calculator')
        self.geometry('200x150')
        self.resizable(True, True)

        # Instruction Label
        self.text_label = ttk.Label(self, text='Calculate your BMI', font=('Times New Roman', 16, 'bold'))
        self.text_label.grid(row=0, column=0, padx=10, pady=2, sticky='WE')

        # Result Label (passed to MainFrame)
        self.text_result = ttk.Label(self, text='')
        self.text_result.grid(row=3, column=0)

        # Main Frame
        self.main_frame = MainFrame(self, self.text_result)
        self.main_frame.grid(row=1, column=0)

        # Button to calculate BMI
        self.button = ttk.Button(self, text='Calculate', command=self.main_frame.calculate_bmi)
        self.button.grid(row=2, column=0)


if __name__ == '__main__':
    app = BMICalculatorApp()
    app.mainloop()
       
