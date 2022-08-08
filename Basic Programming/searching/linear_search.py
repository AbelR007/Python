# Linear Search in Python
# =================================================
# Variables Defined
li = []
pos = 0
found = 0

# List Input
length = int(input("Enter length of list : "))
print("Add Elements :")
for i in range(length):
    a = int(input(" "))
    li.append(a)

# Input
x = int(input("Enter element to be searched : "))

# MAIN LOGIC
# Loop to run through the list of items
for i in range(len(li)):
    if li[i] == x:
        found = 1
        pos = i
        break

if found == 1:
    print(f"{x} found at position {pos}")
else:
    print(f"{x} not found!")
# ================================================
# Code by Abel Roy #
