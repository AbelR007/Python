# Checks if a number is a prime number or not
# =================================================
num = int(input("Enter a number :")) # integer
flag = True # boolean

for i in range(2,num):
    # print(i,num,num%i)
    if num % i == 0:
        flag = False
        break
        # print("Composite number")

if flag == True:
    print("Prime Number")
else:
    print("Composite number")

# ================================================
# Code by Abel Roy #
