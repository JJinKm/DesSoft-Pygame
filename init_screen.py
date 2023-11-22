import pygame
import random
from os import path
from config import FPS, GAME, QUIT, IMG_DIR, CREDIT, BLACK

def init_screen(screen):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR,'inicio.png')).convert()
    backgroud_rect = background.get_rect()

    jogar = 0
    credito = 1
    cursor = jogar

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if cursor == jogar:
                        state = GAME
                        running = False
                    if cursor == credito:
                        state = CREDIT
                        running = False
                if event.key == pygame.K_UP:
                    if cursor == credito:
                        cursor = jogar
                if event.key == pygame.K_DOWN:
                    if cursor == jogar:
                        cursor = credito
        screen.fill(BLACK)
        screen.blit(background,backgroud_rect)
        pygame.display.update()
    return state