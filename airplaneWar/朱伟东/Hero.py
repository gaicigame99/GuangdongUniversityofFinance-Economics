import pygame
class Hero(pygame.sprite.Sprite):
    image1 = pygame.image.load("images\hero1.png")
    image2 = pygame.image.load("images\hero2.png")
    crashimage1 = pygame.image.load("images\hero_blowup_n1.png")
    crashimage2 = pygame.image.load("images\hero_blowup_n2.png")
    crashimage3 = pygame.image.load("images\hero_blowup_n3.png")
    crashimage4 = pygame.image.load("images\hero_blowup_n4.png")
    imagegroup = [image1, image2]
    crashimagegroup = [crashimage1, crashimage2, crashimage3, crashimage4, crashimage4]
    def __init__(self,x,y,hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\hero.gif")

        self.frame = 0
        self.crashframe = 0
        self.time = 0
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.hp = hp

    def crash(self):
        self.hp -= 1

    def update(self,x,y,current_time, screen,rate=60):
        if self.hp > 0:
            self.rect.left, self.rect.top = (x, y)
            if current_time > self.time + 2*rate:
                self.image = Hero.imagegroup[self.frame]
                if self.frame == 1:
                    self.frame = 0
                else:
                    self.frame = 1
                self.time = current_time
            screen.blit(self.image, [x - 50, y - 64])
        else:
            if current_time > self.time + rate:
                self.image = Hero.crashimagegroup[self.crashframe]
                self.crashframe += 1
                self.time = current_time
                screen.blit(self.image,self.rect)
                if self.crashframe >= 5:
                    self.kill()