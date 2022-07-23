# Pass or Fail Grading System
# =================================================
# QUESTION:
"""
Write a program in Python to take marks of 5 subjects and
    print the overall result as pass or fail
"""
# =================================================
# CODE:
result = True
percent = 0
for i in range(1,6):
    marks = int(input(f"Enter Subject {i} in 100 : "))
    percent += marks
    if marks <= 45:
        result = False
    else:
        pass

print("Overall Result : ")
if result is False:
    print("FAIL")
else:
    print("PASS")
print("Overall Percentage :\n",percent/5)
# ================================================
# Code by Abel Roy #
