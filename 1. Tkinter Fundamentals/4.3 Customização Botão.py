import tkinter as tk

# Function to close the main window
def close_window():
    root.destroy()  # Terminates the Tkinter main loop and closes the window

# Create the main application window
root = tk.Tk()
root.title('Button Customization')
root.geometry('300x200')

# --- Creating a button with an image ---

# Load an image for the button (must be .png, .gif, or .ppm)
image_button = tk.PhotoImage(file='assets/Button_Click-Here.png')

# Create a Button widget using the image and link it to the close function
button = tk.Button(
    root,
    image=image_button,  # Display the image on the button
    command=close_window # Function executed when the button is clicked
)
button.pack(pady=20)    # Add vertical padding

# Start the Tkinter event loop (keeps the window open)
root.mainloop()