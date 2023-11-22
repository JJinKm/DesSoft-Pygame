import pygame
from assets import load_assets, TIMER_FONT
from config import FPS, INIT, QUIT, BLACK, WHITE

def leaderboard(window, LEADERBOARD, time):
    clock = pygame.time.Clock()

    assets = load_assets()
    YES = 0
    NO = 1
    cursor = YES
    base_font = assets[TIMER_FONT]
    user_text = ''
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                if event.key == pygame.K_RETURN:
                    if cursor == YES:
                        LEADERBOARD[user_text] = time
                        state = INIT
                if event.key == pygame.K_RIGHT:
                    if cursor == YES:
                        cursor = NO
                if event.key == pygame.K_LEFT:
                    if cursor == NO:
                        cursor == YES
                else:
                    user_text += event.unicode
        window.fill(WHITE)
        text_surface = base_font.render(user_text,True,BLACK)
        i = 0
        for usuar, tempo in LEADERBOARD.items():
            window.blit(usuar, (30,10+i))
            window.blit(tempo, (50,10+i))
            i += 10
        window.blit(text_surface,(10,10))
        pygame.display.flip()
    return state