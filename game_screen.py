import pygame
import random
from os import path
from config import FPS, WIDTH, HEIGHT, HORIZONTAL, VERTICAL, best_score, QUIT, SND_DIR, BLACK,BLUE
from assets import load_assets, TIMER_FONT, BACKGROUND
from sprites import Character, Arrow

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
    for i in range(N_ARROW):
        posicao = random.choice([HORIZONTAL, VERTICAL])
        arrow = Arrow(assets, posicao, 0)
        all_sprites.add(arrow)
        all_arrow.add(arrow)
    
    DONE = 0
    PLAYING = 1
    OVER = 2
    state = PLAYING

    bgd_random = random.randint(0,3)

    t_init = pygame.time.get_ticks()
    
    current = N_ARROW
    t_aug = 10

    best_text = assets[TIMER_FONT].render('{0:.2f}'.format(best_score), True, (0, 0, 255))

    music_random = random.randint(0,4)

    pygame.mixer.music.load(path.join(SND_DIR, 'bgm{0}.wav'.format(music_random)))
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play()

    past_time = pygame.time.get_ticks()
    past_time = (past_time - t_init)/1000

    while state != DONE:
        clock.tick(FPS)
        t = pygame.time.get_ticks()
        time_playing = (t - t_init)/1000
        timer = assets[TIMER_FONT].render('{0:.2f}'.format(time_playing), True, BLUE) # A função "get_ticks" dá o valor em milissegundos, divide por 1000 para ter em segundos.
        window.fill((255,255,255))
        window.blit(assets[BACKGROUND][bgd_random], (0,0))
        window.blit(timer, (10,10))
        window.blit(best_text, (10,40))
        if state == PLAYING:
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

        if pygame.mixer.music.get_busy() == False:
            music_random = random.randint(0,4)
            pygame.mixer.music.load(path.join(SND_DIR, 'bgm{0}.wav'.format(music_random)))
            pygame.mixer.music.set_volume(0.10)
            pygame.mixer.music.play()

        if len(collisions) > 0:  # Se houve colisão
            time_finished = time_playing
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path.join(SND_DIR, 'Game_over_bgm.wav'))
            pygame.mixer.music.play()
            if time_finished > best_score:
                best_score = time_finished
            i = HEIGHT
            while i >= 0:
                rect = pygame.Rect(0,i,WIDTH,8)
                pygame.draw.rect(window,BLACK, rect)
                pygame.display.update()
                pygame.time.wait(15)
                i -= 5
            state = DONE

        bool_diff = False
        if time_playing >= t_aug:
            bool_diff = True
        if bool_diff:
            bgd_random = random.randint(0,3)
            current += DIFF
            t_aug += 10
            bool_diff = False
            for i in range(DIFF):
                posicao = random.choice([HORIZONTAL, VERTICAL])
                arrow = Arrow(assets, posicao, current)
                all_sprites.add(arrow)
                all_arrow.add(arrow)

        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()
    return [state,best_score]