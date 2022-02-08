# Printing using the "GRID" function
# ------------------------------------------------------------
from tkinter import *

# Creates the application
root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello, world!")
myLabel2 = Label(root, text="My name is Abel Roy!").grid(row=1, column=0)
# Shoving into the screen
myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)

# Runs the program
root.mainloop()
# ------------------------------------------------------------
# Code by Abel Roy #
