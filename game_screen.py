import pygame
import random
from config import FPS, WIDTH, HEIGHT, HORIZONTAL, VERTICAL, best_score
from assets import load_assets, TIMER_FONT
from sprites import Character, Arrow
# from leaderboard import leaderboard

def game_screen(window, best_score):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_arrow = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_arrow'] = all_arrow

    player = Character(groups, assets)
    all_sprites.add(player)
    DIFF = 1
    N_ARROW = 5
    AUG = 1
    for i in range(N_ARROW):
        posicao = random.choice([HORIZONTAL, VERTICAL])
        arrow = Arrow(assets, posicao, AUG)
        all_sprites.add(arrow)
        all_arrow.add(arrow)
    
    DONE = 0
    PLAYING = 1
    OVER = 2
    state = PLAYING

    keys_down = {}

    t_init = pygame.time.get_ticks()
    
    current = N_ARROW
    current_aug = AUG
    t_aug = 5

    best_text = assets[TIMER_FONT].render('{0:.2f}'.format(best_score), True, (0, 0, 255))

    while state != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
                    player.speedx -= 3
                    player.speedy += 3
                if event.key == pygame.K_RIGHT and event.key == pygame.K_UP:
                    player.speedx += 3
                    player.speedy += 3
                if event.key == pygame.K_LEFT and event.key == pygame.K_DOWN:
                    player.speedx -= 3
                    player.speedy += 3
                if event.key == pygame.K_RIGHT and event.key == pygame.K_DOWN:
                    player.speedx += 3
                    player.speedy += 3
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
            time_finished = time_playing
            if time_finished > best_score:
                best_score = time_finished
            state = DONE
        t = pygame.time.get_ticks()
        time_playing = (t - t_init)/1000

        bool_diff = False
        if time_playing >= t_aug:
            bool_diff = True
        if bool_diff:
            current += DIFF
            current_aug += DIFF
            t_aug += 10
            bool_diff = False
            for i in range(current):
                posicao = random.choice([HORIZONTAL, VERTICAL])
                arrow = Arrow(assets, posicao, current_aug)
                all_sprites.add(arrow)
                all_arrow.add(arrow)
        timer = assets[TIMER_FONT].render('{0:.2f}'.format(time_playing), True, (0,0,255)) # A função "get_ticks" dá o valor em milissegundos, divide por 1000 para ter em segundos.

        all_sprites.update()
        window.fill((255,255,255))
        window.blit(timer, (10,10))
        window.blit(best_text, (10,40))
        all_sprites.draw(window)
        pygame.display.update()
    return [state,best_score]