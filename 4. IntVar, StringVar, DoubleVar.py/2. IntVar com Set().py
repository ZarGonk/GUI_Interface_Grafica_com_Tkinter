import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Example 2 - Changing Values")

# Create an IntVar counter starting at 0
counter = tk.IntVar(value=0)

# Function to increase the counter
def increase():
    counter.set(counter.get() + 1)

# Function to decrease the counter
def decrease():
    counter.set(counter.get() - 1)

# Label linked to the IntVar to display the current counter value
label = tk.Label(root, textvariable=counter, font=("Arial", 20))
label.pack(pady=10)

# Button to increase the counter
btn1 = tk.Button(root, text="Increase", command=increase)
btn1.pack(side="left", padx=10)

# Button to decrease the counter
btn2 = tk.Button(root, text="Decrease", command=decrease)
btn2.pack(side="right", padx=10)

# Start the Tkinter event loop
root.mainloop()
