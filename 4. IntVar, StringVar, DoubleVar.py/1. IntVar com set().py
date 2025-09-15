import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Example 1 - Basic IntVar")

# Create an IntVar (special Tkinter variable for integers)
number = tk.IntVar()

# Set an initial value
number.set(10)

# Function to display the current value
def show():
    print("Current value is:", number.get())

# Button that calls the show() function
btn = tk.Button(root, text="Show Value", command=show)
btn.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
