# FACTORIAL of a NUMBER using Loops
# ----------------------------------------------------------------
"""
    # CONCEPT :

    > Product of an integer and all the integers below it
    > Example :
        2! = 1 x 2
        3! = 1 x 2 x 3
        4! = 1 x 2 x 3 x 4

"""
# ----------------------------------------------------------------
# CODE :
# ----------------------------------------------------------------
print("Factorial of a Number\n-------------------")
fact = 1
num = int(input("Enter number :"))

if num <= 0:
    print("""
        Please enter a positive number!
        Factorial doesn't exist for negative numbers.
    """)
    # Negative numbers don't have a factorial value
else:
    while(1, num + 1):
        fact = fact * i
    print("Factorial of a Number is ", fact)

# --- Code by Abel Roy --- #
