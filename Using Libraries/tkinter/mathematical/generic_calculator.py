# Generic Calculator using Tkinter Python
# =================================================
from tkinter import *

root = Tk()
root.title("Generic Calculator")

# Entry widget
e = Entry(root, width = 35, borderwidth=5)
e.grid(row=0,column=0,columnspan=2,padx =5,pady=5)

fno = 0

def button_click(number):
    current = e.get()
    e.delete(0, END) # Deletes what already exists
    e.insert(0, str(current) + str(number)) # Inserts the number

def button_clear():
    e.delete(0, END)

def button_add():
    first = e.get()
    global fno
    fno = int(first)
    e.delete(0, END)

def button_subtract():
    first = e.get()
    global fno
    fno = int(first)


def button_eq():
    if fno == 0:
        e.delete(0, END)
    else:
        sno = int(e.get())
        add = int(fno + sno)
        e.delete(0, END)
        e.insert(0, int(add))

# Buttons for Numbers
button1 = Button(root, text="1",padx=50,pady=20,command=lambda: button_click(1))
button2 = Button(root, text="2",padx=50,pady=20,command=lambda: button_click(2))
button3 = Button(root, text="3",padx=50,pady=20,command=lambda: button_click(3))
button4 = Button(root, text="4",padx=50,pady=20,command=lambda: button_click(4))
button5 = Button(root, text="5",padx=50,pady=20,command=lambda: button_click(5))
button6 = Button(root, text="6",padx=50,pady=20,command=lambda: button_click(6))
button7 = Button(root, text="7",padx=50,pady=20,command=lambda: button_click(7))
button8 = Button(root, text="8",padx=50,pady=20,command=lambda: button_click(8))
button9 = Button(root, text="9",padx=50,pady=20,command=lambda: button_click(9))
button0 = Button(root, text="0",padx=50,pady=20,command=lambda: button_click(0))

button_add = Button(root, text="+", padx=50,pady=20,command=button_add)
button_eq = Button(root, text="=", padx=50,pady=20,command=button_eq)
button_clear = Button(root, text="clear", padx=35,pady=15,command=button_clear)

# Put Buttons on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=1)

button_add.grid(row=4,column=0)
button_eq.grid(row=4,column=2)
button_clear.grid(row=0,column=2)

root.mainloop()
# ================================================
# Code by Abel Roy #
