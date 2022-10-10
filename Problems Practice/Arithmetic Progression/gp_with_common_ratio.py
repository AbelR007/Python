"""
    Problem :
    Given an array, arr[] and a positive integer K. The task is to find the position say i of the element in arr[] such that prefix sum till i-1, i and suffix sum till i+1 are in Geometric Progression with common ratio K.

    Input:
    arr[] = { 5, 1, 4, 20, 6, 15, 9, 10 }, K = 2

    Output: 4

    Explanation:
    The following operations are performed to get required GP.
    Sum of element from position 1 to 3 is 5 + 1 + 4 = 10 and from 5 to 8 is 6 + 15 + 9 + 10 = 40.
    And element at position 4 is 20.
    Therefore10, 20, 40 is a Geometric Progression series with common ratio K.

"""
# =================================================
# Given Constants
arr = [ -3, 5, 0, 2, 1, 25, 25, 100 ]
k = 5
out = 6
# =================================================
# CODE
def sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
def Solution(arr, k):

    length = len(arr)
    for pos in range(1,length):
        i = arr[pos]

        first_half = arr[:pos]
        second_half = arr[pos+1:]

        sum_first = sum(first_half)
        sum_second = sum(second_half)

        gp_array = [sum_first,i,sum_second]
        try:
            if (i/sum_first) == (sum_second/i):
                return pos+1
        except ZeroDivisionError:
            pass
    return 0

x = Solution(arr, k)
print(x==out)
# ================================================
def Solution2(arr, k):
    n = len(arr)
    for i in range(1,len(arr)-1):
        indices = range(i)
        prefix_sum = sum([arr[p] for p in indices])

        suffix_indices = range(i+1,n)
        suffix_sum = sum([arr[q] for q in suffix_indices])

        try:
            val = arr[i]
            if (val/prefix_sum) == (suffix_sum/val):
                return i+1
        except ZeroDivisionError:
            pass
    return 0

y = Solution2(arr,k)
print(y==out)
# ================================================
# Above Code by Abel Roy #
# ================================================
# Problem Solution [From the internet, not by me]
def Actual_Solution(arr, k):
    N = len(arr)
    if (N < 3):
        return -1
    Sum = 0
    temp = 0
    for i in range(0, N):
    	Sum += arr[i]
    R = (k * k + k + 1)
    if (Sum % R !=  0):
    	return 0
    Mid = k * (Sum // R)
    for i in range(1, N-1):
    	temp += arr[i - 1]
    	if (arr[i] == Mid):
    		if (temp == Mid // k):
    			return i + 1
    		else:
    			return 0
    return 0

z = Actual_Solution(arr, k)
print(z==out)
# ================================================
