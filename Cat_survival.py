import pygame
import random
import time
from os import path
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, CREDIT, best_score, SND_DIR
from game_screen import game_screen
from init_screen import init_screen
from credit_screen import credit_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat's Survival")

state = INIT

clock = pygame.time.Clock()
start_time = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or state == QUIT:
            running = False

    if state == INIT:
        state = init_screen(window)
        start_time = time.time()  
    elif state == GAME:
        pygame.mixer.music.fadeout(600)
        pygame.time.wait(600)
        screen_game = game_screen(window,best_score)
        state = screen_game[0]
        best_score = screen_game[1]

        
        if state == 0:
            end_time = time.time()
            survived_time = end_time - start_time - 2.33 if start_time is not None else 0

            font = pygame.font.Font(None, 36)
            text = font.render(f'Game Over', True, (255, 255, 255))
            text2 = font.render(f'Você Sobreviveu por {survived_time:.2f} segundos', True, (255,255,255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            text2_rect = text2.get_rect(center=(WIDTH //2, HEIGHT // 2 + 56))

            window.fill((0, 0, 0))
            window.blit(text, text_rect)
            window.blit(text2, text2_rect)
            pygame.mixer.music.fadeout(5000)
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.mixer.music.stop()
            state = INIT

            start_time = None  

    elif state == CREDIT:
        state = credit_screen(window)

    pygame.display.update()
    clock.tick(60)

pygame.quit()