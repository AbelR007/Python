# Matrix Multiplication using Nested Loops
# =================================================
# input two matrices of size n x m
matrix1 = [ [10,20,10], [4 ,5,6], [2,3,5]]
matrix2 = [ [3,2,4], [3,3,9], [4,4,2]]

res = [[0 for x in range(3)] for y in range(3)]

# Accurate Matrix Multiplication
# -----------------------------------
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            # resulted matrix
            res[i][j] += matrix1[i][k] * matrix2[k][j]

# Direct Matrix Multiplication [Incorrect]
# -----------------------------------
# for i in range(len(matrix1)):
#     for j in range(len(matrix2)):
#         res[i][j] = matrix1[i][j] * matrix2[i][j]

print("The Resultant Matrix is :\n",res)
# ================================================
# Code by Abel Roy #
