# Calculates the gross salary using base salary
# =================================================
"""
Write a python program to calculate grose salary of an Employee.
Gross Salary = DA + Basic Salary + HRA
DA = 10% of Basic Salary
HRA = 4% of Basic Salary
"""
# CODE
def salary(base_salary):
    da = 0.10 * base_salary
    hra = 0.04 * base_salary
    return da, hra

def main():
    bs = int(input("Enter your salary : "))
    da, hra = salary(bs)
    gross_salary = da + bs + hra

    print("Your DA is : ",da)
    print("Your HRA is : ",hra)
    print("Gross Salary : ", gross_salary)

main()
# ================================================
# Code by Abel Roy #
