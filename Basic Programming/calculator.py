# Simple Calculator
# =================================================
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def divide(a,b):
    return a / b
def multiply(a,b):
    return a * b
def square(a):
    return a ** 2
def cube(a):
    return a ** 3
def exponent(a,b):
    return a ** b
def square_root(a):
    return math.sqrt(a)

def calculator():
    print("SIMPLE CALCULATOR")
    print("================================")
    while True:
        print(
            """
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Square
            6. Cube
            7. Exponent
            8. Square Root
            """
        )
        op = eval(input("Enter operation : "))
        x = int(input("Enter a number : "))
        y = int(input("Enter a number : "))

        if op == 0:
            break

        if op == 1:
            print("Addition : ",add(x,y))
        elif op == 2:
            print("Subtract : ",subtract(x,y))
        elif op == 3:
            print("Multiply : ",multiply(x,y))
        elif op == 4:
            print("Divide : ",divide(x,y))
        elif op == 5:
            print("Square : ",square(x))
        elif op == 6:
            print("Cube : ",cube(x))
        elif op == 7:
            print("Exponent : ",exponent(x,y))
        elif op == 8:
            print("Square Root : ",square_root(x))
        else:
            print("Invalid Option")
            continue
    print("Thanks for using my calculator")
calculator()
# ================================================
# Code by Abel Roy #
