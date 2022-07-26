# Length of Last Word
# =================================================
# Difficulty : Easy
# =================================================
""" Problem Statement :
Using the user-defined string, calculate the length of the last word in the string,
    Example :
'Hello World' -> 5
'Abel Roy' -> 3
"""
class Solution:
    def lengthOfLastWord(s: str):
        l = len(s)
        val = 0
        flag = False
        for i in range(1,l+1):
            if s[-i].isalpha() is True:
                flag = True

            if flag is True:
                if s[-i].isspace() is True:
                    break
                val+=1
        return val

your_str = input("Enter your string : ")
ans = Solution.lengthOfLastWord(your_str)
print(ans)
# ================================================
# Code by Abel Roy #
