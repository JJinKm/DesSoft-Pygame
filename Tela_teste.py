import pygame
import random
pygame.init()

WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Nome')

ARROW_WIDTH = 38
ARROW_HEIGHT = 7
CHARACTER_WIDTH = 25
CHARACTER_HEIGHT = 25
meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
meteor_img = pygame.transform.scale(meteor_img, (ARROW_WIDTH, ARROW_HEIGHT))
ship_img = pygame.image.load('assets/img/playerShip1_orange.png').convert_alpha()
ship_img = pygame.transform.scale(ship_img, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
x_lista = [-ARROW_WIDTH, WIDTH + ARROW_WIDTH]
speed_list = [0,8]
font = pygame.font.SysFont(None, 48)

player_lives = 3 # vidas
heart_img = pygame.image.load('assets/img/health.png').convert_alpha()
heart_img = pygame.transform.scale(heart_img, (30, 30))

class character(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[CHARACTER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT /2
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class arrow(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self, assets)
        self.image = assets[ARROW_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(x_lista)
        self.rect.y = random.randint(-ARROW_HEIGHT, HEIGHT+ARROW_HEIGHT)
        self.speedx = random.randint(9,16)
        self.speedy = random.choice(speed_list)
        self.initposx = self.rect.x
        self.initposy = self.rect.y
    def update(self):
        if self.initposx == -ARROW_WIDTH:
            if self.initposy <= HEIGHT/2:
                self.rect.y += self.speedy
                self.rect.x += self.speedx
            elif self.initposy > HEIGHT/2:
                self.rect.y -= self.speedy
                self.rect.x += self.speedx
        if self.initposx == WIDTH + ARROW_WIDTH:
            if self.initposy <= HEIGHT/2:
                self.rect.y += self.speedy
                self.rect.x -= self.speedx
            elif self.initposy > HEIGHT/2:
                self.rect.y -= self.speedy
                self.rect.x -= self.speedx


        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH + ARROW_WIDTH or self.rect.bottom < 0:
            self.rect.x = random.choice(x_lista)
            self.rect.y = random.randint(0, HEIGHT)
            self.speedx = random.randint(9,16)
            self.speedy = random.choice(speed_list)

clock = pygame.time.Clock()
FPS = 60

game = True
all_sprites = pygame.sprite.Group()
all_arrow = pygame.sprite.Group()
player = character(ship_img)
all_sprites.add(player)
for i in range(8):
    Arrow = arrow(meteor_img)
    all_sprites.add(Arrow)
    all_arrow.add(Arrow)
    
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            if event.key == pygame.K_UP:
                player.speedy -= 8
            if event.key == pygame.K_DOWN:
                player.speedy += 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8
            if event.key == pygame.K_UP:
                player.speedy += 8
            if event.key == pygame.K_DOWN:
                player.speedy -= 8

    collisions = pygame.sprite.spritecollide(player, all_arrow, True)  # Verifica colisão e remove os meteoros

    if collisions:  # Se houve colisão
        player_lives -= 1  # Reduz uma vida do jogador
        
        if player_lives == 0:  # Se as vidas acabaram
            game = False  # Encerra o jogo

    

    t = pygame.time.get_ticks()
    timer = font.render('{0:.2f}'.format(t/1000), True, (0,0,255)) # A função "get_ticks" dá o valor em milissegundos, divide por 1000 para ter em segundos.

    all_sprites.update()
    window.fill((255,255,255))
    window.blit(timer, (10,10))
    for i in range(player_lives):
            window.blit(heart_img, (10 + i * 40, 550)) # As vidas não tava aparecendo na tela, porque tava antes do Window.fill
    all_sprites.draw(window)
    pygame.display.update()
    
pygame.quit()