# BMI Calculator
# =================================================
height = int(input("Enter height (in cm) : "))
weight = int(input("Enter weight (in kg) : "))
height = height / 100.0
bmi = weight / (height ** 2)

print("Your Body Mass Index is ",bmi)
# ================================================
# Code by Abel Roy #
