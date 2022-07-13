
def main():
    print("Grade Calculator\n")

    maths  = int(input("Enter Maths marks : "))
    science = int(input("Enter Science marks : "))
    social = int(input("Enter Social marks : "))
    english = int(input("Enter English marks : "))
    hindi = int(input("Enter Hindi marks : "))

    percent = (maths + science + social + english + hindi)/5

    print("\nYour Average Percentage is ",percent)

    grade, feedback = grade_system(percent)
    print("Grade : ",grade)
    print("Feedback : ",feedback)

def grade_system(x):
    if x >= 90:
        grade = "A+"
        feedback = "Excellent Marks!"
    elif x >= 80:
        grade = "A"
        feedback = "Good Marks!"
    elif x >= 70:
        grade = "B"
        feedback = "Good but can be better!"
    elif x >= 60:
        grade = "C"
        feedback = "Not so great, not bad!"
    elif x >= 50:
        grade = "D"
        feedback = "You did okay, improve next time!"
    elif x >= 40:
        grade = "E"
        feedback = "You just passed!"
    else:
        grade = "F"
        feedback = "Failed :("
    return grade, feedback

main()
