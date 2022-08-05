# Connect 4 using Tkinter Python
# =================================================
import tkinter as tk
import numpy as np

root = tk.Tk()
root.title("Connect 4")

only_font = ("JetBrians Mono",16)
current_ch = 1

butt_width = 5
butt_height = 2

first_color = "#da504c"
second_color = "#4b5ae3"

tk.Label(root, text="Connect 4",font=only_font).pack()


head_area = tk.Frame(
    root,
    width = 10,
    height = 80,
    bg = "#134478"
)

area = tk.Frame(root, width=500, height=500,bg="#12d282")

board = [[0] * 7 for _ in range(6)]
cols = 7
rows = 6


class Head_Button:
    def __init__(self, x,y, board):
        self.x = x
        self.y = y
        self.board = board

        self.button = tk.Button(
            head_area,
            text = "",
            width = butt_width,
            height = butt_height,
            bg = "#da504c",
            command = self.main_dynamics
        ).grid(row=x,column=y)
        self.value = None
        self.turn = 1

    def valid_loc(self,board, col):
        board = np.transpose(np.flip(board,0))
        # print(board[col])
        for i in range(len(board[col])):
            if board[col][i] == 0:
                # print(col,i)
                return (5-i,col)
            # print(board[col][i])

    def main_dynamics(self):
        global current_ch
        print(np.array(self.board))
        # print("once")
        if not self.value:
            # print(self.board)
            print(self.x,self.y)

            self.board = np.transpose(np.flip(self.board,0))
            # print(self.board[col])
            for i in range(len(self.board[self.y])):
                if self.board[self.y][i] == 0:
                    # print(self.y,i)
                    new_x = 6-i
                    new_y = self.y
                    break

            self.board[new_x][new_y] = self.turn
            Game(new_x, new_y).button.configure(
                text = f"{self.turn}"
            )
            print("Turn : ",self.turn)
            self.change_turn(self.turn)

    def change_turn(self,turn):
        if turn == 1:
            self.turn = 2
        elif turn == 2:
            self.turn = 3
        else:
            print("idk")

def check_win(board,turn):
    for i in range(rows):
        new = 0
        for j in range(cols):
            # print(j)
            if board[i][j] == 0:
                continue
            if board[i][j] == turn:
                new += 1
        if new >= 4:
            game_over(board,turn)
            # return True
            break

def game_over(board,turn):
    if turn == 2:
        print("Player 2 won!")
        return
    elif turn == 1:
        print("Player 1 won!")
        return
    else:
        print(f"Draw {turn}")
        return

class Game:
    def __init__(self, x,y):
        self.x = x
        self.y = y

        self.button = tk.Button(
            area, text='',width=butt_width, height=butt_height,
            state = tk.DISABLED
        )
        self.button.grid(row=x, column=y)
        self.value = None

for x in range(1,6+1):
    for y in range(1,7+1):
        Head_Button(1,y, board)
        Game(x,y)

head_area.pack(fill=tk.X,padx=20,pady=5)
area.pack(padx=20,pady=10)
root.mainloop()
# ================================================
# Code by Abel Roy #
