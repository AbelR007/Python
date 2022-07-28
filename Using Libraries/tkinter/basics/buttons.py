# Creating Buttons in Tkinter
# =================================================
from tkinter import *

root = Tk()

def myClicks():
    myLabel = Label(root, text="You just clicked it!")
    myLabel.pack()

# Buttons
myButton = Button(root, text="Click me!", command=myClicks,fg="white",bg="green")
# myButton = Button(root, text="Click me!", state=DISABLED)
# myButton = Button(root, text="Click me!", padx=50, pady = 50)
myButton.pack()

# Runs the program
root.mainloop()
# ================================================
# Code by Abel Roy #
