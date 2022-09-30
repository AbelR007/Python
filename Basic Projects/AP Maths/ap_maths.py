from tkinter import *
import color_pallette as clr

root = Tk()
root.title("AP Maths Calculator")
root.geometry("500x500")

title = Label(
    root,
    text = "AP Maths Calculator",
    fg = clr.title_color,
    bg = clr.title_bg,
    font = clr.myfont
)
title.pack(fill=X)

enter_a = Label(
    root,
    text = "Enter value of 'a' :",
    fg = clr.label_color,
    font = clr.label_font
)
enter_a.place(relx = 0.1, rely = 0.11)

root.mainloop()
