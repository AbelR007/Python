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
def sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

# def gp_or_not(arr):

def Solution(arr, k):

    length = len(arr)
    for pos in range(1,length):
        i = arr[pos]

        first_half = arr[:pos]
        second_half = arr[pos+1:]
        print(first_half, second_half)

        sum_first = sum(first_half)
        sum_second = sum(second_half)

        gp_array = [sum_first,i,sum_second]
        try:
            if (i/sum_first) == (sum_second/i):
                return pos+1
        except ZeroDivisionError:
            print("Zero hua")
    return 0

arr = [ -3, 5, 0, 2, 1, 25, 25, 100 ]
k = 5
out = 6

x = Solution(arr, k)
print("============")
print(x)
print(x==out)
# ================================================
# Code by Abel Roy #
