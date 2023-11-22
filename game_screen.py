import pygame
import random
from config import FPS, WIDTH, HEIGHT, HORIZONTAL, VERTICAL
from assets import load_assets, TIMER_FONT
from sprites import Character, Arrow

def game_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_arrow = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_arrow'] = all_arrow

    player = Character(groups, assets)
    all_sprites.add(player)
    for i in range(8):
        posicao = random.choice([HORIZONTAL, VERTICAL])
        arrow = Arrow(assets, posicao)
        all_sprites.add(arrow)
        all_arrow.add(arrow)
    
    DONE = 0
    PLAYING = 1
    OVER = 2
    state = PLAYING

    keys_down = {}
    lives = 1

    t = pygame.time.get_ticks()

    while state != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx -= 6
                if event.key == pygame.K_RIGHT:
                    player.speedx += 6
                if event.key == pygame.K_UP:
                    player.speedy -= 6
                if event.key == pygame.K_DOWN:
                    player.speedy += 6
                if event.key == pygame.K_ESCAPE:
                    state = DONE
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx += 6
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 6
                if event.key == pygame.K_UP:
                    player.speedy += 6
                if event.key == pygame.K_DOWN:
                    player.speedy -= 6

        collisions = pygame.sprite.spritecollide(player, all_arrow, True, pygame.sprite.collide_mask)  # Verifica colisão e remove os meteoros

        if len(collisions) > 0:  # Se houve colisão
            lives -= 1  # Reduz uma vida do jogador

            if lives == 0:  # Se as vidas acabaram
                state = DONE  # Encerra o jogo

        t = pygame.time.get_ticks()
        time_playing = t/1000
        timer = assets[TIMER_FONT].render('{0:.2f}'.format(time_playing), True, (0,0,255)) # A função "get_ticks" dá o valor em milissegundos, divide por 1000 para ter em segundos.

        all_sprites.update()
        window.fill((255,255,255))
        window.blit(timer, (10,10))
        all_sprites.draw(window)
        pygame.display.update()