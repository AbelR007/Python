# Bubble Sort in Python
# =================================================
import random

def adding_elements_to_list(arr):
    for j in range(5):
        x = random.randint(1,50)
        arr.append(x)
    return arr

def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

arr = []
arr = adding_elements_to_list(arr)
print("Array before Bubble Sort : ",arr)
bubble_sort(arr)
print("Array after Bubble Sort : ",arr)
# ================================================
# Code by Abel Roy #
