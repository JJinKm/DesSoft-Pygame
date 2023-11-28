import pygame
from os import path
from config import RED, QUIT, INIT, FPS, WHITE, IMG_DIR, WIDTH, HEIGHT
from assets import load_assets, CREDIT_FONT, CURSOR_IMG_MIRROR

def credit_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    cursor = assets[CURSOR_IMG_MIRROR]

    text1 = assets[CREDIT_FONT].render('Creditos',True, WHITE)
    text2 = assets[CREDIT_FONT].render('Desenvolvedores',True, WHITE)
    text2_rect = text2.get_rect(center=(WIDTH/2,65))
    nomes_dev = assets[CREDIT_FONT].render('Joshua, Materusse e Otto', True, WHITE)
    dev_rect = nomes_dev.get_rect(center=(WIDTH/2, 95))
    music = assets[CREDIT_FONT].render('Música', True, WHITE)
    music_rect = music.get_rect(center=(WIDTH/2, 200))
    name_music = assets[CREDIT_FONT].render('Joshua e Davi Bruder',True,WHITE)
    name_music_rect = name_music.get_rect(center=(WIDTH/2, 230))
    agradecimento = assets[CREDIT_FONT].render('Agradecimento',True,WHITE)
    agradecimento_rect = agradecimento.get_rect(center=(WIDTH/2, 340))
    professor = assets[CREDIT_FONT].render('Professor Fillipe Resina',True, WHITE)
    professor_rect = professor.get_rect(center=(WIDTH/2, 370))
    voltar = assets[CREDIT_FONT].render('Voltar', True, WHITE)

    running = True

    while running:
        clock.tick(FPS)
        window.fill(WHITE)
        for i in range(1,5):
            background = pygame.image.load(path.join(IMG_DIR,'Credit{0}.png'.format(i)))
            background = pygame.transform.scale(background,(WIDTH,HEIGHT))
            backgroud_rect = background.get_rect()
            window.blit(background,backgroud_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = INIT
                    running = False

        window.blit(text1, (10,10))
        window.blit(text2, text2_rect)
        window.blit(nomes_dev, dev_rect)
        window.blit(music, music_rect)
        window.blit(name_music,name_music_rect)
        window.blit(agradecimento,agradecimento_rect)
        window.blit(professor,professor_rect)
        window.blit(voltar, (10, HEIGHT - 28))
        window.blit(cursor, (125, HEIGHT - 28))

        pygame.display.flip()
    return state