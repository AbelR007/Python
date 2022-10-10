# Problem Statement
"""
    Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
"""
# =================================================
# Difficulty : Medium
# =================================================
# Input :
# num = "1432219"
# k = 3
num = "43214321"
k = 4
# Output :
out = "1321"
# =================================================
# Solution :
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # initalize variables
        sort_list = []
        result = 0

        # run a loop over the "num" integer
        length = len(num)
        for i in range(length):
            exc = num[i:i+k]

            # check for overflow
            diff_digits = 0
            if len(exc) == k:
                pass
            else:
                diff_digits = k - len(exc)
                for d in range(diff_digits):
                    exc += str(num[d])
            # end of overflow

            # below code gets the "k" no of integer values from the "num"

            # run a loop to get the remaining integer values after removing "exc"
            inc = ""
            for idx in range(length):
                if diff_digits > idx:
                    inc += ""
                elif i <= idx and idx < i+k:
                    inc += ""
                else:
                    inc += num[idx]

            # print(exc, inc,idx, i,k,diff_digits)
            # the above print command for testing and debugging purposes

            try:
                inc = int(inc)
            except ValueError:
                inc = 0
            sort_list.append(inc)

        sort_list.sort()
        result = str(sort_list[0])
        return result

x = Solution()
val = x.removeKdigits(num, k)
print(val==out)
# ================================================
# Code by Abel Roy #


# ================================================
# Failures
        # result = 0
        # # numcpy = num
        # length = len(num)
        # for pos in range(length):
        #     numcpy = ""
        #     for i in range(length):
        #         if num[i] == num[pos:k]:
        #             print("",num,num[pos:k])
        #             numcpy = ""
        #         else:
        #             numcpy += num[i]
        #         print(numcpy)
        #     print(">>>",numcpy)
