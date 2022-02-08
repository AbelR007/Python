# Printing "Hello, world!" in Tk window
# ------------------------------------------------------------------------
from tkinter import *

# Creates the application object
root = Tk()

# Creating a label widget
myLabel = Label(root, text="Hello, world!")
# Shoving into the screen
myLabel.pack()

# Runs the application
root.mainloop()
# -------------------------------------------------------------------------
# Code by Abel Roy #
