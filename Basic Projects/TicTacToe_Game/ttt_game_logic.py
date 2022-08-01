# Game Logic used for TTT Game
# =================================================
matrix = [[0]*3 for _ in range(3)]

def game_over(matrix, res):
    if res == "O":
        print("O won!")
        print(matrix)
    if res == "X":
        print("X won!")
        print(matrix)

possibliity = (
    ((0,0),(1,1),(2,2)),
    ((0,2),(1,1),(2,0)),

    ((0,0),(0,1),(0,2)),
    ((1,0),(1,1),(1,2)),
    ((2,0),(2,1),(2,2)),

    ((0,0),(1,0),(2,0)),
    ((0,1),(1,1),(2,1)),
    ((0,2),(1,2),(2,2)),
)

def game_over_check(mat):
    for x in possibliity:
        print(x[0][0])
        print(mat)
        if mat[x[0][0]][x[0][1]] == mat[x[1][0]][x[1][1]] == mat[x[2][0]][x[2][1]]:
            if mat[x[0][0]][x[0][1]] == 0:
                pass
            elif mat[x[1][0]][x[1][1]] == 0:
                pass
            elif mat[x[2][0]][x[2][1]] == 0:
                pass
            else:
                if mat[x[0][0]][x[0][1]] != 0:
                    res = mat[x[0][0]][x[0][1]]
                if mat[x[1][0]][x[1][1]] != 0:
                    res = mat[x[1][0]][x[1][1]]
                if mat[x[2][0]][x[2][1]] != 0:
                    res = mat[x[2][0]][x[2][1]]
                game_over(mat,res)
        else:
            pass

def ui(mat):
    game_over_check()

print(matrix)
matrix[1][1] = matrix[0][0] = matrix[2][2] = "X"
game_over_check(matrix)
print(matrix)
# ================================================
# Code by Abel Roy #
