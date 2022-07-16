# BMI Calculator
# =================================================
def bmi(height, widthpipi):
    height = height / 100.0
    bmi = weight / (height ** 2)
    return bmi

height = int(input("Enter height (in cm) : "))
weight = int(input("Enter weight (in kg) : "))

print("Your Body Mass Index is ",bmi(height,weight))
# ================================================
# Code by Abel Roy #
