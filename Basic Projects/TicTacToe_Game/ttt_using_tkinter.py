# TicTacToe Game by Abel Roy using Tkinter Python
# =================================================
import tkinter as tk

root = tk.Tk()

root.resizable(False,False)
root.title("Tic Tac Toe")
the_font = ("JetBrians Mono",16)

tk.Label(root, text="Tic Tac Toe", font=the_font).pack()

current_ch = "X"
area = tk.Frame(root, width=300, height=300, bg="black")

matrix = [[0]*3 for _ in range(3)]
objects = []

# Status
status = tk.Label(root, text="", font=the_font, bg="grey", fg="snow")
status.pack(fill=tk.X)

class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button = tk.Button(area, text="",width=9,height=4, command=self.game_dynamics)
        self.button.grid(row=x, column=y)
        self.value = None

    def game_dynamics(self):
        global current_ch
        if not self.value:
            self.button.configure(text=current_ch,bg="snow",fg="black")
            self.value = current_ch
            matrix[self.x-1][self.y-1] = self.value
            print(">",matrix)
            if current_ch == "X":
                current_ch = "O"
            else:# current_ch == "O":
                current_ch = "X"
            status.configure(text=f"< {current_ch}'s Turn >")
        check_win(matrix)

    def reset_matrix(self):
        self.button.configure(text="",bg="lightgray")
        self.value=None

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
def check_win(mat):
    for x in possibliity:
        # print(x[0][0])
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
                status.configure(text=f"{res} Won! ")
                disable_game()
                return
        else:
            pass
    draw_check(mat)

def draw_check(mat):
    zeros = 0
    for x in range(3):
        for y in range(3):
            if mat[x][y] == 0:
                zeros += 1
    if zeros == 0:
        res = "D"
        game_over(mat,res)
        disable_game()
        return 0
    else:
        pass

def game_over(matrix, result):
    if result == "X":
        print("X Won!")
        return
    elif result == "O":
        print("O Won!")
        return
    else:
        print("DRAW")
        return

# Game RUN
for x in range(1,4):
    for y in range(1,4):
        objects.append(Game(x,y))
        # print(matrix)
# ^^^ Important

# Disables the Buttons in the Game UI
def disable_game():
    for x in objects:
        x.button.configure(state=tk.DISABLED)
    play_again_button.pack()

def play_again():
    global current_ch
    current_ch = "X"
    for x in objects:
        x.button.configure(state=tk.NORMAL)
        x.reset_matrix()
    global matrix
    matrix = [[0]*3 for _ in range(3)]
play_again_button = tk.Button(root, text="Play Again?", font= the_font,command=play_again)

area.pack(padx=10, pady=10)
footer = tk.Label(root, text=" <> by Abel Roy",font=the_font, bg="snow", fg="grey")
footer.pack(fill=tk.X)

root.mainloop()
# ================================================
# Code by Abel Roy #
