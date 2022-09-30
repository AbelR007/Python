# Linear Search in Python
# =================================================
# Variables Defined
li = []
pos = 0
found = False

# List Input
length = int(input("Enter length of list : "))
print("Add Elements :")
for i in range(length):
    a = int(input(" "))
    li.append(a)

# Input
element = int(input("Enter element to be searched : "))

# MAIN LOGIC
# Loop to run through the list of items
for i in li:
    if i == element:
        found = True
        pos = li.index(i) + 1
        break

if found:
    print(f"{element} found at position {pos}")
else:
    print(f"{element} not found!")
# ================================================
# Code by Abel Roy #
