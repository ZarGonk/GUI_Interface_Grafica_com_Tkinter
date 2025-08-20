import tkinter as tk

root = tk.Tk()
root.title('Centralizando Janela')

window_width = 400
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_heigth/2 - window_height/2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# keep the windiw open
root.mainloop()