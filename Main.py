from GUI import GUI
from Game import Game


# setup game
game = Game()

# setup gui
gui = GUI(font=40, game=game)


# start game/gui
gui.start()