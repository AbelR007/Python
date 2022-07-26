# Add Two Numbers
# =================================================
# Difficulty: Medium
# ---------------------------------------------------------
""" Problem Statement :
Given two lists of non-negative integers, the digits are stored in reverse order.
Add the two numbers in their correct order and return the sum as a linked list
"""
class Solution:
    def addTwoNumbers(l1: list, l2: list) -> list:
        List = []

        first = ""
        for i in range(len(l1)):
            first += str(l1[i])
        first = first[::-1]

        second = ""
        for i in range(len(l2)):
            second += str(l2[i])
        second = second[::-1]

        val = str(int(first) + int(second))
        for i in range(len(val)):
            List.append(val[i])
        return List[::-1]

ans = Solution.addTwoNumbers([2,4,3],[5,6,4])
print(ans)
# ================================================
# Code by Abel Roy #
