#
#
# def Fibonacci(n):
#     a = 0
#     b = 1
#
#     print(a)
#     print(b)
#
#     for i in range(n):
#         c = a + b
#         print(c)
#         a, b = b, c
#
# # Fibonacci(5)
#
# # Fibonacci series using recursion
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(8))

def tri_recursion(k):
    if ( k > 0):
        result = k + tri_recursion(k-1)
        print(result)

    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(4)
