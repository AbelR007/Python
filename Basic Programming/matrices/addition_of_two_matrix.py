# Addition of 2 Matrices
# ==================================================
def print_matrix(matrix):
    print("Matrix :")
    for i in range(len(matrix)):
        print("\n\t",end="")
        for j in range(len(matrix[i])):
            print(matrix[i][j],end="   ")
        # print("\n")
    print("\n-------------------------------")

mat = []
def input_matrix(mat):
    size = eval(input("Enter size of matrix : "))
    rows = size[0]
    cols = size[1]

    for i in range(0,rows):
        row_mat = []
        for j in range(0,cols):
            x = int(input("Enter value : "))
            row_mat.append(x)
            # print(mat)
        mat.append(row_mat)
    return mat

x = []
x = input_matrix(x)
print_matrix(x)
y = []
y = input_matrix(y)
print_matrix(y)

def multiply_matrix(first,second):
    mat = []
    for i in range(len(first)):
        row_mat = []
        for j in range(len(first[i])):
            x = first[i][j] * second[i][j]
            row_mat.append(x)
        mat.append(row_mat)
    return mat

def addition_matrix(first,second):
    mat = []
    for i in range(len(first)):
        row_mat = []
        for j in range(len(first[i])):
            x = first[i][j] + second[i][j]
            row_mat.append(x)
        mat.append(row_mat)
    return mat

mul_matrix = multiply_matrix(x,y)
print_matrix(mul_matrix)
add_matrix = addition_matrix(x,y)
print_matrix(add_matrix)
# ================================================
# Code by Abel Roy #
