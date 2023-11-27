import random
import pygame
from config import WIDTH, HEIGHT, ARROW_HEIGHT_X, ARROW_WIDTH_X,ARROW_WIDTH_Y,ARROW_HEIGHT_Y, CHARACTER_HEIGHT, CHARACTER_WIDTH, x_lista, speed_list, HORIZONTAL, VERTICAL, y_lista
from assets import CHARACTER_IMG, ARROW_IMG_X, ARROW_IMG_Y

class Character(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[CHARACTER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT /2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
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

class Arrow(pygame.sprite.Sprite):
    def __init__(self, assets, posicao, DIFF):
        pygame.sprite.Sprite.__init__(self)
        self.position = posicao
        self.assets = assets
        self.diff = DIFF
        if self.position == HORIZONTAL:
            self.image = assets[ARROW_IMG_X]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(x_lista)
            self.rect.y = random.randint(-ARROW_HEIGHT_X, HEIGHT+ARROW_HEIGHT_X)
            self.speedx = random.randint(5+DIFF,7+DIFF)
            self.speedy = random.choice(speed_list)
            self.initposx = self.rect.x
            self.initposy = self.rect.y
        elif self.position == VERTICAL:
            self.image = assets[ARROW_IMG_Y]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(-ARROW_WIDTH_Y, WIDTH+ARROW_WIDTH_Y)
            self.rect.y = random.choice(y_lista)
            self.speedx = random.choice(speed_list)
            self.speedy = random.randint(5+DIFF,7+DIFF)
            self.initposx = self.rect.x
            self.initposy = self.rect.y
    def update(self):
        if self.position == HORIZONTAL:
            if self.initposx == -ARROW_WIDTH_X:
                if self.initposy <= HEIGHT/2:
                    self.rect.y += self.speedy
                    self.rect.x += self.speedx
                elif self.initposy > HEIGHT/2:
                    self.rect.y -= self.speedy
                    self.rect.x += self.speedx
            if self.initposx == WIDTH + ARROW_WIDTH_X:
                if self.initposy <= HEIGHT/2:
                    self.rect.y += self.speedy
                    self.rect.x -= self.speedx
                elif self.initposy > HEIGHT/2:
                    self.rect.y -= self.speedy
                    self.rect.x -= self.speedx
        elif self.position == VERTICAL:
            if self.initposy == -ARROW_HEIGHT_Y:
                if self.initposx <= WIDTH/2:
                    self.rect.y += self.speedy
                    self.rect.x += self.speedx
                elif self.initposx > WIDTH/2:
                    self.rect.y += self.speedy
                    self.rect.x -= self.speedx
            if self.initposy == HEIGHT + ARROW_HEIGHT_Y:
                if self.initposx <= WIDTH/2:
                    self.rect.y -= self.speedy
                    self.rect.x += self.speedx
                elif self.initposx > WIDTH/2:
                    self.rect.y -= self.speedy
                    self.rect.x -= self.speedx

        if self.rect.top > HEIGHT+ARROW_HEIGHT_Y or self.rect.right < 0 or self.rect.left > WIDTH + ARROW_WIDTH_X or self.rect.bottom < -ARROW_HEIGHT_Y:
            posicao = random.choice([HORIZONTAL, VERTICAL])
            self.position = posicao
            if self.position == HORIZONTAL:
                self.image = self.assets[ARROW_IMG_X]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.x = random.choice(x_lista)
                self.rect.y = random.randint(-ARROW_HEIGHT_X, HEIGHT+ARROW_HEIGHT_X)
                self.speedx = random.randint(5+self.diff,7+self.diff)
                self.speedy = random.choice(speed_list)
                self.initposx = self.rect.x
                self.initposy = self.rect.y
            elif self.position == VERTICAL:
                self.image = self.assets[ARROW_IMG_Y]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.x = random.randint(-ARROW_WIDTH_Y, WIDTH+ARROW_WIDTH_Y)
                self.rect.y = random.choice(y_lista)
                self.speedx = random.choice(speed_list)
                self.speedy = random.randint(5+self.diff,7+self.diff)
                self.initposx = self.rect.x
                self.initposy = self.rect.y