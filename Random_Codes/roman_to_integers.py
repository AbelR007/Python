# Convert Roman Symbols to Integers
# =================================================
# Difficulty: Medium
# -----------------------------------------------
def func(i):
    if i == "M":
        val = 1000
    elif i == "D":
        val = 500
    elif i == "C":
        val = 100
    elif i == "L":
        val = 50
    elif i == "X":
        val = 10
    elif i == "V":
        val = 5
    elif i == "I":
        val = 1
    else:
        return 0
    return val

class MyClass:

    def romanToInt(s: str) -> int:
        val = 0
        order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        for i in range(len(s)):

            indx = order.index(s[i])
            if i == 0:
                val += func(s[i])
                continue

            prev_indx = order.index(s[i-1])
            if prev_indx >= indx:
                val += func(s[i])
            else:
                new_val = func(s[i]) - func(s[i-1])
                val += (new_val - func(s[i-1]))
        return val

your_no = str(input("Enter your input : "))
ans = MyClass.romanToInt(your_no)
print(ans)
# ans = MyClass.romanToInt("IV")
# print(ans,ans==4)
# ================================================
# Code by Abel Roy #
