import pygame
import random
import time
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, CREDIT
from game_screen import game_screen
from init_screen import init_screen
from credit_screen import credit_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nome')

state = INIT

clock = pygame.time.Clock()
start_time = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state == INIT:
        state = init_screen(window)
        start_time = time.time()  
    elif state == GAME:
        state = game_screen(window)

        
        if state == 0:
            end_time = time.time()
            survived_time = end_time - start_time if start_time is not None else 0

            font = pygame.font.Font(None, 36)
            text = font.render(f'Game Over - Você Sobreviveu por {survived_time:.2f} segundos', True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

            window.fill((0, 0, 0))
            window.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(5000)  
            running = False

            start_time = None  

    elif state == CREDIT:
        state = credit_screen(window)

    pygame.display.update()
    clock.tick(60)

pygame.quit()


