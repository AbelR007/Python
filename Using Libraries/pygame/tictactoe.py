# TicTacToe Game using PyGame
# =================================================
import pygame as pg

##region Constants
val = "o"

winner = None
draw = None

# Window Size
width, height = 400, 400

# Colors
bgcolor = (255,255,255)
linecolor = (0,0,0)
##endregion

board = [
    [None]*3,
    [None]*3,
    [None]*3
]

pg.init()
font = pg.font.Font("arial.ttf",25)


class TicTacToe:

    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pg.display.set_mode(
            (self.w, self.h)
        )
        # self.init_window = init_window
        pg.display.set_caption(
            'TicTacToe'
        )
        # (pg.display.set_mode((400,400))).fill((255,255,255))
        self.score = 0
    # def display(self):
    #     display_surface = pg.display.set_mode((400,400))
    #     display_surface.fill(white)

    def start(self):
        for event in pg.event.get():
            # Quit the Game
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            # Takes Events
            if event.type == pg.MOUSEBUTTONDOWN:
                print("Pressed mouse")
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    print("Pressed 1")
                elif event.key == pg.K_2:
                    print("Pressed 2")
                elif event.key == pg.K_0:
                    game_over = True
                else:
                    print("Pressed something")

        game_over = False
        return game_over, self.score
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_LEFT:


if __name__ == '__main__':
    game = TicTacToe()
    # game.display()

    # Game Loop
    while True:
        game_over, score = game.start()
        if game_over is True:
            break
    print("The End")

pg.quit()
# ================================================
# Code by Abel Roy #
