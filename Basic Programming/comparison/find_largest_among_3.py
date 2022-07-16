# Finds the largest number among 3
# =================================================
a = int(input("Enter FIRST number : "))
b = int(input("Enter SECOND number : "))
c = int(input("Enter THIRD number : "))

if a > b and a > c:
    print(a," is the largest")
elif b > c and b > a:
    print(b," is the largest")
elif c > a and c > b:
    print(c," is the largest")
else:
    print("No idea.")
# ================================================
# Code by Abel Roy #
