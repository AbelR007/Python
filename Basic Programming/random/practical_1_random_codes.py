"""
Question :
    Write a python program to demonstrate the use of looping statements, while loop, for loop and nested loops.
    1) Write a python program to print all even numbers between 1 to 100 using while loop
    2) Write a python program to find the sum of the first ten natural numbers using for loop
    3) Write a python program to calculate the factorial of a number
    4) Write a python program to reverse a given number
    5) Write a python program to calculate the palindrome of a given number
    6) Write a python program to print the fibonacci series
"""
# ===========================================================================
# SOLUTIONS to those questions
# --------------------------------
# Q1)
# i = 1
# while i<=100:
#     if i % 2 == 0:
#         print(i)
#     i+=1
# --------------------------------
# Q2)
# sum = 0
# for i in range(1,11):
#     sum += i
# print(sum,"is the sum of first ten natural numbers")
# --------------------------------
# Q3)
# fact = 1
# x = int(input("Enter a number : "))
# for i in range(1,x+1):
#     fact *= i
# print(fact,"is the factorial of",x)
# --------------------------------
# Q4)
# x = input("Enter number : ")
# print(x[::-1])
# --------------------------------
# Q5)
# x = input("Enter a number : ")
# if x == x[::-1]:
#     print(x,"is a palindrome")
# else:
#     print(x,"is NOT a palindrome")
# --------------------------------
# Q6)
# x = int(input("Enter no. of terms : "))
# a = b = 1
# print(a,b,sep="\n")
# for i in range(x-2):
#     c = a + b
#     a,b = b,c
#     print(c)
# ================================================
# Code by Abel Roy #
