import pygame
import random
pygame.init()

WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Nome')

METEOR_WIDTH = 50
METEOR_HEIGHT = 38
SHIP_WIDTH = 50
SHIP_HEIGHT = 38
meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
meteor_img = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT))
ship_img = pygame.image.load('assets/img/playerShip1_orange.png').convert_alpha()
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
x_lista = [0,WIDTH-METEOR_WIDTH]
speed_list = [-8,0,8]
speed_list2 = [-8,8]

class character(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT /2
        self.speedx = 0
        self.speedy = 0
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
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(x_lista)
        self.rect.y = random.randint(-METEOR_HEIGHT, HEIGHT)
        self.speedx = random.choice(speed_list)
        self.speedy = random.choice(speed_list)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.choice(x_lista)
            self.rect.y = random.randint(0, HEIGHT)
            if self.speedy == 0:
                self.speedx = random.choice(speed_list2)
            elif self.speedx == 0:
                self.speedy = random.choice(speed_list2)

clock = pygame.time.Clock()
FPS = 30

game = True
all_sprites = pygame.sprite.Group()
all_meteors = pygame.sprite.Group()
player = character(ship_img)
all_sprites.add(player)
for i in range(2):
    meteor = arrow(meteor_img)
    all_sprites.add(meteor)
    all_meteors.add(meteor)
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
    all_sprites.update()
    window.fill((255,255,255))
    all_sprites.draw(window)
    pygame.display.update()
    
pygame.quit()