# Armstrong Number or not
# =================================================
# Armstrong Function
def armstrong_or_not(num: int):
    org = num
    sum = 0
    while (num>0):
        a = num % 10
        sum = sum + a*a*a
        num = num//10
    return sum == org

num = eval(input("Enter a number : "))
armstrong = armstrong_or_not(num)

if armstrong:
    print("The given number is Armstrong number")
else:
    print("The given number is not Armstrong number")
# ================================================
# Code by Abel Roy #
