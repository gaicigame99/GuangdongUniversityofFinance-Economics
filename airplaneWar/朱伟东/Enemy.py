import pygame
import random
class Enemy(pygame.sprite.Sprite):
    image1 = pygame.image.load(r"images\enemy0_down1.png")
    image2 = pygame.image.load(r"images\enemy0_down2.png")
    image3 = pygame.image.load(r"images\enemy0_down3.png")
    image4 = pygame.image.load(r"images\enemy0_down4.png")
    animation = [image1,image2,image3,image4,image4]
    def __init__(self,x,y,speed,hp):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.time = 0
        i = random.randint(0,2)
        if i == 0:
            self.image = pygame.image.load(r"images\enemy0.png")
            self.hp = 1
        elif i == 1:
            self.image = pygame.image.load(r"images\enemy1.png")
            self.hp = 5
        else:
            self.image = pygame.image.load(r"images\enemy2.png")
            self.hp = 10
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (x,y)
        self.speed = speed

    def move(self,screen):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

    def crash(self):
        self.hp -= 1
        return self.hp

    def update(self,current_time, rate=60):
        if self.hp > 0:
            self.rect = self.rect.move(self.speed)
            # screen.blit(self.image, self.rect)
        else:
            if current_time > self.time + rate:
                self.image = Enemy.animation[self.frame]
                self.frame += 1
                self.time = current_time
                if self.frame >= 5:
                    self.kill()

