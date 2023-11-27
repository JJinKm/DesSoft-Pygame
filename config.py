from os import path
from game_screen import game_screen

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

WIDTH = 545
HEIGHT = 465
FPS = 30

HORIZONTAL = 15
VERTICAL = 20

ARROW_WIDTH_X = 35
ARROW_HEIGHT_X = 7
ARROW_HEIGHT_Y = 35
ARROW_WIDTH_Y = 7
CHARACTER_WIDTH = 25
CHARACTER_HEIGHT = 25

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

x_lista = [-ARROW_WIDTH_X, WIDTH + ARROW_WIDTH_X]
speed_list = [0,8]
y_lista = [-ARROW_HEIGHT_Y, HEIGHT + ARROW_HEIGHT_Y]

INIT = 0
GAME = 1
QUIT = 2
CREDIT = 3

best_score = 0