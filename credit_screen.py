import pygame
from config import RED, QUIT, INIT, FPS, WHITE
from assets import load_assets, TIMER_FONT

def credit_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    text1 = assets[TIMER_FONT].render('Creditos',True, RED)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = INIT
                    running = False
        window.fill(WHITE)
        window.blit(text1, (10,10))
        pygame.display.flip()
    return state