import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, CREDIT
from game_screen import game_screen
from init_screen import init_screen
from credit_screen import credit_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Nome')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == CREDIT:
        state = credit_screen(window)
    else:
        state = QUIT

pygame.quit()