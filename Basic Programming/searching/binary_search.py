# Binary Search in Python using Iterative method
# =================================================
# Main Function
def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2

        # Check if num is present at mid
        if arr[mid] < num:
            low = mid + 1

        # If num is greater, compare to the right of mid
        elif arr[mid] > num:
            high = mid - 1

        # If num is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return False


# Initial arr
arr = [12, 24, 32, 39, 45, 50, 54]
num = int(input("Enter number to be searched : "))
# Function call
result = True
result = binary_search(arr, num)

# Condition Check
if result:
    print("Element is present at index", str(result))
else:
    print("Element is not present in the list")
# ================================================
# Code by Abel Roy #
