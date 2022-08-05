import numpy as np

board = [["0"] * 7 for _ in range(6)]
cols = 7
rows = 6

def horizontal_check(board,turn):
    for i in range(rows):
        new = 0
        for j in range(cols):
            print(j)
            if board[i][j] == 0:
                continue
            if board[i][j] == turn:
                new += 1
        if new >= 4:
            return True
            break
def vertical_check(board,turn):
    for i in range(len(board)):
        new = 0
        for j in range(len(board[i])):
            if board[j][i] == 0:
                continue
            if board[j][i] == turn:
                new += 1
        if new >= 4:
            return True
            break

turns = "X"
def game(board,turns):
    arr = np.array(board)
    arr[5][3] = "U"
    arr[5][4] = "D"
    arr[5][5] = "X"
    arr[5][6] = "X"
    print(arr)
    arr = np.transpose(np.flip(arr,0))
    print(arr[4])
    # for x in range(len(board)):
    #     for y in range(len(board[x])):
    #         print(board[x][y])

game(board,turns)

def horizontals_check(board,piece):
    for c in range(cols):
        for r in range(rows):
            # print(f"|{r} {c}>>>",board[r][c],end="")
            print(r,c,board[r][c],end="")
        print()

def print_board(board):
    arr = np.array(board)
    print(arr)
    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         print(board[i][j],end="")
    #     print()

print(board)
# board[2][1]="X"
# board[1][0]

# test script
board[5][3] = "X"
board[5][4] = "X"
board[5][5] = "X"
board[5][6] = "X"
#


print_board(board)

# print()
# piece = "B"
# horizontals_check(board,piece)

result = horizontal_check(board, "X")
# result = vertical_check(board, "X")
if result is True:
    print("Line made")
else:
    print("Line not made")

# print(board)
