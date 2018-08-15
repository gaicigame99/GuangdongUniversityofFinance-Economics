import pygame
class Bullet(pygame.sprite.Sprite):
    image1 = pygame.image.load(r"images\bullet1.png")
    image2 = pygame.image.load(r"images\bullet-1.gif")
    imagegroup = [image1,image2]
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"images\bullet-1.gif")
        self.frame = 0
        self.time = 0
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.speed = (0, -5)

    # def move(self,screen):
    #     self.rect = self.rect.move(self.speed)
    #     screen.blit(self.image,self.rect)
    #     if self.rect.top < 0:
    #         return True

    def update(self,current_time,rate = 800):
        self.rect = self.rect.move(self.speed)
        if current_time > self.time +  rate:
            self.image = Bullet.imagegroup[self.frame]
            if self.frame == 1:
                self.frame = 0
            else:
                self.frame = 1
            self.time = current_time
        if self.rect.top < 0:
            self.kill()