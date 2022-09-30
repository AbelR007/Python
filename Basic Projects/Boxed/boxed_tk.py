import numpy as np
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

main_font = ("JetBrains Mono", 25)
root.resizable(False, False)

rows = 11
cols = 11
board = np.zeros((rows, cols))
playing_player = 1

first_color = "#c65b4c"
second_color = "#40c0d0"

title = tk.Label(
    root,
    text = "BoxeD",
    bg = "#222",
    fg = "#ddd",
    font = main_font
)
game_area = tk.Frame(
    root,
    height = 200,
    width = 200,
    bg = "#fff"
)
def height_id(x,y):
    if x % 2 != 0:
        height = 5
    else:
        height = 1
    return height
def width_id(x,y):
    if y % 2 != 0:
        width = 10
    else:
        width = 2
    return width
def state_id(x,y):
    # if x % 2 == 1 or y % 2 == 1:
    if (x + y) % 2 == 1:
        state = tk.NORMAL
    else:
        state = tk.DISABLED
    return state
def color_id(x,y, cplayer):
    if (x+y) % 2 == 1:
        color = "#fff"
    elif x % 2 == 0 and y % 2 == 0:
        color = "#222"
    else:
        color = "#fff"
    return color


class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        global playing_player

        self.button = tk.Button(
            game_area,
            text = f'',
            width = width_id(x,y),
            height = height_id(x,y),
            state = state_id(x,y),
            bg = color_id(x,y, board[x][y]),
            command = self.game_dynamics
        )
        self.button.grid(row=x,column=y)

    def player_color(self, player):
        if player == 1:
            return first_color
        if player == 2:
            return second_color

    def player_change(self, player):
        if player == 1:
            return 2
        if player == 2:
            return 1

    def boxes_check(self,player):
        global board, playing_player

        for x in range(rows-2):
            for y in range(cols-2):
                if board[x][y] == board[x-1][y+1] == board[x][y+2] == board[x+1][y+1]:
                    if board[x][y] == 0:
                        continue
                    board[x][y+1] = playing_player
                    if board[x][y+1] == 0:
                        Game(x,y+1).button.configure(
                            bg = self.player_color(playing_player)
                        )
                        print("Game over")
                    return True


    def game_dynamics(self):
        global board, playing_player
        print(board)
        board[self.x][self.y] = playing_player
        Game(self.x,self.y).button.configure(bg=self.player_color(playing_player))

        if self.boxes_check(playing_player) is True:
            # Game(self.x,self.y)
            print("...")

        playing_player = self.player_change(playing_player)



title.pack(fill=tk.X)
game_area.pack(padx=10,pady=10)

# Creates Board
for row in range(rows):
    for col in range(cols):
        Game(row,col)

root.mainloop()
