import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):
    def __init__(self, container, result_label):
        super().__init__(container)

        # Reference to the result label from the main application
        self.result_label = result_label

        # Variables to store user input
        self.weight = tk.DoubleVar()  # User's weight (kg)
        self.height = tk.DoubleVar()  # User's height (m)

        # --- Labels for Input Fields ---
        self.text_weight = ttk.Label(self, text='Weight (kg):')
        self.text_weight.grid(row=0, column=0)

        self.text_height = ttk.Label(self, text='Height (m):')
        self.text_height.grid(row=1, column=0)

        # --- Entry Fields (user inputs) ---
        self.entry_weight = ttk.Entry(self, textvariable=self.weight, width=10)
        self.entry_weight.grid(row=0, column=1, padx=5, pady=2)

        self.entry_height = ttk.Entry(self, textvariable=self.height, width=10)
        self.entry_height.grid(row=1, column=1, padx=5, pady=2)

    def calculate_bmi(self):
        """
        Calculate BMI using the values entered by the user.
        Updates the result label with the calculated BMI or an error message.
        """
        try:
            bmi = self.weight.get() / (self.height.get() ** 2)
            self.result_label.config(text=f'Your BMI is {bmi:.2f}')
        except ZeroDivisionError:
            # Height cannot be zero (division by zero)
            self.result_label.config(text='Height cannot be 0')
        except Exception as e:
            # Any other unexpected errors
            self.result_label.config(text=f'Error: {e}')


class BMICalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main window configuration
        self.title('BMI Calculator')
        self.geometry('200x150')
        self.resizable(True, True)

        # Window title / instruction message
        self.text_label = ttk.Label(self, text='Calculate your BMI', font=('Times New Roman', 16, 'bold'))
        self.text_label.grid(row=0, column=0, padx=10, pady=2, sticky='WE')

        # Label that will display the BMI result
        self.text_result = ttk.Label(self, text='')
        self.text_result.grid(row=3, column=0)

        # Main frame that contains inputs
        self.main_frame = MainFrame(self, self.text_result)
        self.main_frame.grid(row=1, column=0)

        # Button that triggers the calculation
        self.button = ttk.Button(self, text='Calculate', command=self.main_frame.calculate_bmi)
        self.button.grid(row=2, column=0)


if __name__ == '__main__':
    app = BMICalculatorApp()
    app.mainloop()