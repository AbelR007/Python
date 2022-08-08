import numpy as np
import tkinter as tk

root = tk.Tk()
root.title("This is Not a Test")

only_font = ("JetBrians Mono",16)

butt_width = 5
butt_height = 2

cols = 7
rows = 6
board = np.zeros((rows,cols))
current_player = 1
objects = []

first_color = "#da504c"
second_color = "#4b5ae3"

butt_area = tk.Frame(
    root,
    width = 50*7,
    height = 60,
    bg = "#444"
)
area = tk.Frame(
    root,
    width = 350,
    height = 350,
    bg = "#000"
)
def turn_name(no):
    if no == 1:
        return "Red"
    if no == 2:
        return "Blue"
status = tk.Label(
    root,
    text = f"{turn_name(current_player)}'s Turn'",
    bg = "#ddd",
    font = only_font,
)

class Drop_Area:
    def __init__(self, col):
        self.col = col

        self.button = tk.Button(
            butt_area,
            text = "",
            bg = "#e0bf2e",
            width = butt_width,
            height = butt_height,
            command = self.game_dynamics
        )
        self.button.grid(row=0,column=col)
        self.value = None

    def game_dynamics(self):
        global board, current_player
        # print(board,current_player, self.col)

        new_board = np.transpose(np.flip(board,0))
        for i in range(len(new_board[self.col])):
            if new_board[self.col][i] == 0:
                x = 5 - i
                y = self.col
                break


        board[x][y] = current_player
        bg_color = self.colour_change(current_player)
        Area(x,y).button.configure(bg=bg_color)

        result = self.check_win(current_player)
        print(".")
        if result is True:
            return

        current_player = self.player_change(current_player)
        status.configure(text = f"{turn_name(current_player)}'s Turn")
        print(board)

    def colour_change(self,player):
        if player == 1:
            return first_color
        if player == 2:
            return second_color

    def check_win(self, player):
        global board

        # Horizontal Check
        for i in range(len(board)):
            for j in range(len(board[i])-3):
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                    self.game_over(player)
                    return True

        # Vertical Check
        for i in range(len(board)-3):
            for j in range(len(board[i])):
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                    # status.configure(text=f"Game Over")
                    self.game_over(player)
                    return True

        # Diagonal Check
        for i in range(len(board)-3):
            for j in range(len(board[i])-3):
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                    # status.configure(text=f"Game Over")
                    self.game_over(player)
                    return True

        # Backslash Diagonal Check
        # for i in range(len(board)-3):
        #     for j in range(3,len(board[i])):
        #         # print(i,j,board[i][j])
        #         if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == player:
        #             self.game_over(player)
        #             return True

    def game_over(self, player):
        print("Game Over")
        print(f"Player {player} won!")
        status.configure(text=f"{turn_name(current_player)} won!")
        disable_game()
        return

    def player_change(self, player):
        if player == 1:
            return 2
        if player == 2:
            return 1

class Area:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.button = tk.Button(
            area,
            text = "",
            width = butt_width,
            height = butt_height,
            state = tk.DISABLED
        )
        self.button.grid(row=x, column=y)
        self.value = None

    def reset_board(self):
        # global board
        self.button.configure(text="",bg="lightgray")
        self.value=None

def disable_game():
    for x in objects:
        x.button.configure(state=tk.DISABLED)
    play_again_button.pack()

def play_again():
    global current_player
    current_ch = 1

    for x in range(rows):
        for y in range(cols):
            Area(x,y).reset_board()
    for x in objects:
        x.button.configure(state=tk.NORMAL)

    global board
    board = np.zeros((rows,cols))
play_again_button = tk.Button(
    root,
    text="Play Again?",
    font= only_font,
    command=play_again
)

for col in range(cols):
    objects.append(Drop_Area(col))
for x in range(rows):
    for y in range(cols):
        Area(x,y)

tk.Label(root, text="Connect 4", font=only_font).pack()
status.pack(fill=tk.X)
butt_area.pack(padx= 20,pady=5)
area.pack(padx= 20,pady= 10)
tk.Label(root, text="<> by Abel Roy",font=only_font).pack(fill=tk.X)

root.mainloop()
