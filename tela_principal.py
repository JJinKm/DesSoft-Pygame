import pygame
import random
from config import WIDTH, HEIGHT
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Nome')

game_screen(window)

pygame.quit()