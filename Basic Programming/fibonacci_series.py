# Fibonacci Series
# =================================================
# 1 1 2 3 5 8 ...
print('The Fibonacci Series ... ')

x = int(input('Enter no.of terms :'))
a = 1
b = 1
print(a)
print(b)

for i in range (x-2):
    i+=1
    c = a + b
    a,b = b,c
    print(c)
# ================================================
# Code by Abel Roy #
