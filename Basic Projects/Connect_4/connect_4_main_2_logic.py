import numpy as np

cols = 7
rows = 6
board = np.zeros((6,7))
player = 1

# print(board)

def player_change(prev):
    if prev == 1:
        return 2
    if prev == 2:
        return 1

def check_winner(board, turn):
    for c in range(cols-3):
        for r in range(rows):
            if board[r][c] == 0:
                continue
            if board[r][c] == board[r][c+1] == board[r][c+2]:
                print("True")
            # print(board[c][j])
    # for i in range(len(board)):
    #     new = 0
    #     for j in range(len(board[i])):
    #         # print(j)
    #         if board[i][j] == 0:
    #             continue
    #         if board[i][j] == turn:
    #             new += 1
    #
    #     print(">",new)
    #     if new >= 4:
    #         return True
    #         break

while True:
    print("--------------------------------\n",board)
    col = int(input(f"Enter {player} column no: "))

    col -= 1
    new_board = np.transpose(np.flip(board,0))
    for i in range(len(new_board[col])):
        if new_board[col][i] == 0:
            x = 5 - i
            y = col
            break
    board[x][y] = player

    check_winner(board, player)

    player = player_change(player)
    if col == -1:
        break
