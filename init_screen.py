import pygame
import random
from os import path
from assets import load_assets, TIMER_FONT, CURSOR_IMG, MAIN_MENU_MSC
from config import FPS, GAME, QUIT, IMG_DIR, CREDIT, BLACK, BLUE, WIDTH, HEIGHT, WHITE, SND_DIR

def init_screen(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    img_cursor = assets[CURSOR_IMG]
    img_cursor_rect_jogar = img_cursor.get_rect(center=(115, HEIGHT/2-10))
    img_cursor_rect_credit = img_cursor.get_rect(center=(115, HEIGHT/2+70))

    T_NOME = assets[TIMER_FONT].render("Cat's Survival", True, WHITE)
    T_NOME_RECT = T_NOME.get_rect(center=(WIDTH/2,20))
    T_JOGAR = assets[TIMER_FONT].render('Jogar',True, WHITE)
    T_JOGAR_RECT = T_JOGAR.get_rect(center=(WIDTH/2,HEIGHT/2-10))
    T_CREDIT = assets[TIMER_FONT].render('Creditos', True, WHITE)
    T_CREDIT_RECT = T_CREDIT.get_rect(center=(WIDTH/2,HEIGHT/2 + 70))


    JOGAR = 0
    CREDITO = 1
    cursor = JOGAR

    running = True

    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.load(path.join(SND_DIR, 'music_pygame.wav'))
        pygame.mixer.music.set_volume(0.4)

        pygame.mixer.music.play(loops=-1)

    while running:
        clock.tick(FPS)

        screen.fill(BLACK)
        for i in range(1,5):
            background = pygame.image.load(path.join(IMG_DIR,'Inicio{0}.png'.format(i)))
            background = pygame.transform.scale(background,(WIDTH,HEIGHT))
            backgroud_rect = background.get_rect()
            screen.blit(background,backgroud_rect)
        screen.blit(T_NOME, T_NOME_RECT)
        screen.blit(T_JOGAR, T_JOGAR_RECT)
        screen.blit(T_CREDIT, T_CREDIT_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if cursor == JOGAR:
                        state = GAME
                        running = False
                    if cursor == CREDITO:
                        state = CREDIT
                        pygame.mixer.music.pause
                        running = False
                if event.key == pygame.K_UP:
                    if cursor == CREDITO:
                        cursor = JOGAR
                if event.key == pygame.K_DOWN:
                    if cursor == JOGAR:
                        cursor = CREDITO
        if cursor == JOGAR:
            screen.blit(img_cursor, img_cursor_rect_jogar)
        if cursor == CREDITO:
                screen.blit(img_cursor, img_cursor_rect_credit)
        pygame.display.update()
    return state