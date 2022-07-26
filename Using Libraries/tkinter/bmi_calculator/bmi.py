# BMI Calculator based on Height & Weight
# =================================================
from tkinter import *
from tkinter import messagebox

def get_height():
    height = float(ENTRY2.get())
    return height
def get_weight():
    weight = float(ENTRY1.get())
    return weight
def calculate_bmi():
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        messagebox.showinfo("Your BMI Calculated is : ", bmi)

root = Tk()

# Design
bgcolor = "#eed914"
fontcolor = "#0b3c6f"

button_color = "#ffffff"
button_bg = "#222222"

root.bind("<Return>", calculate_bmi)
root.geometry("400x400")
root.configure(background=bgcolor)

root.title("BMI Calculator")
root.resizable(width=False, height=False)
label = Label(
    root,
    bg=bgcolor,
    fg=fontcolor,
    text="BMI Calculator",
    font=("Helvetica", 15, "bold"),
    pady=10
)

label.place(x=55, y=0)

LABLE1 = Label(root, bg=fontcolor, text="Enter Weight (in kg):", bd=6, fg=button_color,
               font=("Helvetica", 10, "bold"), pady=5)
LABLE1.place(x=55, y=60)

ENTRY1 = Entry(root, bd=8, width=10, font="Roboto 11")
ENTRY1.place(x=240, y=60)

LABLE2 = Label(root, bg=fontcolor, text="Enter Height (in cm):", bd=6, fg= button_color,
               font=("Helvetica", 10, "bold"), pady=5)
LABLE2.place(x=55, y=121)

ENTRY2 = Entry(root, bd=8, width=10, font="Roboto 11")
ENTRY2.place(x=240, y=121)

BUTTON = Button(bg=button_bg,fg=button_color, bd=12, text="BMI", padx=33, pady=10, command=calculate_bmi,
                font=("Helvetica", 20, "bold"))
BUTTON.grid(row=5, column=0, sticky=W)
BUTTON.place(x=115, y=250)

root.mainloop()
