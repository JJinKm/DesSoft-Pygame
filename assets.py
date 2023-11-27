import pygame
import os
from config import ARROW_HEIGHT_X, ARROW_WIDTH_X,ARROW_HEIGHT_Y,ARROW_WIDTH_Y, CHARACTER_HEIGHT, CHARACTER_WIDTH, IMG_DIR, SND_DIR, FNT_DIR

ARROW_IMG_X = 'arrow_img_x'
ARROW_IMG_X = 'arrow_img_x'
ARROW_IMG_Y = 'arrow_img_y'
ARROW_IMG_Y = 'arrow_img_y'
CHARACTER_IMG = 'character_img'
CHARACTER_IMG = 'character_img'
TIMER_FONT = 'timer_font'
CURSOR_IMG = 'cursor_img'

def load_assets():
    assets = {}
    assets[ARROW_IMG_X] = pygame.image.load(os.path.join(IMG_DIR, 'meteorBrown_med1.png')).convert_alpha()
    assets[ARROW_IMG_X] = pygame.transform.scale(assets['arrow_img_x'], (ARROW_WIDTH_X, ARROW_HEIGHT_X))
    assets[ARROW_IMG_Y] = pygame.image.load(os.path.join(IMG_DIR, 'meteorBrown_med1.png')).convert_alpha()
    assets[ARROW_IMG_Y] = pygame.transform.scale(assets['arrow_img_y'], (ARROW_WIDTH_Y, ARROW_HEIGHT_Y))
    assets[CHARACTER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[CHARACTER_IMG] = pygame.transform.scale(assets['character_img'], (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    assets[TIMER_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    assets[CURSOR_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Cursor.png')).convert()
    return assets