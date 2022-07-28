# Entry Bar in Tkinter Python
# =================================================
from tkinter import *

# Creates the application
root = Tk()

# Label
myLabel = Label(root, text="Enter your name").pack()

# e = Entry(root, width=50,borderwidth=5,fg="white",bg="blue")
e = Entry(root, width=50)
e.pack()
e.insert(0,"Enter your name")

def myClicks():
    hello = "Your name is " + e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack()


# Buttons
myButton = Button(root, text="Submit", command=myClicks,fg="white",bg="green")
myButton.pack()

# Runs the program
root.mainloop()
# ================================================
# Code by Abel Roy #
