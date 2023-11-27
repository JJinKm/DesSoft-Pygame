from os import path

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

def LEADERBOARD(leaderboard,s,time):
    saida = {}
    lista_usuar = []
    lista_tempo = []
    for usuar, tempo in leaderboard.items():
        lista_usuar.append(usuar)
        lista_tempo.append(tempo)
    i = 0
    lista_saida_t = [0]*len(lista_usuar)
    lista_saida_usuar = [0]*len(lista_usuar)
    while i < len(lista_tempo):
        j = 0
        while j < len(lista_tempo):
            if lista_tempo[i] < lista_tempo[j] or j == len(lista_tempo) - 1:
                lista_saida_t[j] = lista_tempo[i]
                lista_saida_usuar[j] = lista_usuar[i]
            j += 1
        i += 1