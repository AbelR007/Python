# Wikipedia Search Data
# =================================================
from tkinter import *
import wikipedia as wp

# Takes RAW data
x = input("Enter text : ")
results = wp.search(x)
result_page = wp.page(results[0])
content = result_page.content

# Dumps data into GUI
root = Tk()
root.title("Search Results")
text = Label(root, text=content)
text.pack()
root.mainloop()
# ================================================
# Code by Abel Roy #
