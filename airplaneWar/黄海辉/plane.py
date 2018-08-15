import pygame
import random


# 飞机大战
# 手机上单手操作游戏
# 屏幕长方形

class Hero(object):
    def __init__(self, _screen, _x, _y):
        self.image = pygame.image.load("images\hero.gif")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = _x
        self.y = _y

    def show(self, _x, _y):
        self.x = _x
        self.y = _y
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen.blit(self.image, (self.x, self.y))


class bullet(object):
    def __init__(self, _screen, _x, _y, _shoot_speed, _b_v):
        self.image = pygame.image.load(r"images\bullet.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.speed = _shoot_speed
        self.b_v = _b_v

    def shooting(self, _x, _y, _shoot_speed, _b_v):
        self.b_x = []
        self.b_y = []
        self.times = self.b_v
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = _x
        self.y = _y
        if self.times:
            self.times -= 1
        else:
            self.b_x.append(self.x)
            self.b_y.append(self.y)
        for i in range(len(self.b_x)):
            screen.blit(self.image, (self.b_x[i], self.b_y[i]))
            self.b_y[i] -= self.speed

pygame.init()
pygame.mixer.init()

back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()

screen = pygame.display.set_mode((495, 800))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (498, 800))
# bullet = pygame.image.load(r"images\bullet.png")
# b_rect = bullet.get_rect()
# b_w = b_rect.width
# b_h = b_rect.height
# b_x = []
# b_y = []
# b_v = 20
# times = b_v

enemy2 = pygame.image.load(r"images\enemy0_down1.png")
enemy3 = pygame.image.load(r"images\enemy0_down2.png")
enemy4 = pygame.image.load(r"images\enemy0_down3.png")
enemy5 = pygame.image.load(r"images\enemy0_down4.png")
enemy = pygame.image.load(r"images\enemy0.png")
e_rect = enemy.get_rect()
e_h = e_rect.height
e_w = e_rect.width
ex = 100
ey = 0

heroA = Hero(screen, 100, 100)
# hero = pygame.image.load("images\hero.gif")
# h_rect = hero.get_rect()
# h_w = h_rect.width
# h_h = h_rect.height

bulletA = bullet(screen,100,100,5,20)
shoot_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(bg, (0, 0))
    hx, hy = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    heroA.show(hx - heroA.width / 2, hy - heroA.height / 2)
    # screen.blit(hero, (hx-h_w/2, hy-h_h/2))
    screen.blit(enemy, (ex, ey))
    if ey < 800:
        ey += 1
    else:
        ey = random.randint(-100, -50)
    bulletA.shooting(hx - bulletA.width / 2 + 2,hy - heroA.height / 2 - bulletA.height,5,20)
    # if times:
    #     times -= 1
    # else:
    #     b_x.append(hx - b_w / 2 + 2)
    #     b_y.append(hy - heroA.height / 2 - b_h)
    #     times = b_v
    # for i in range(len(b_x)):
    #     screen.blit(bullet, (b_x[i], b_y[i]))
    #     b_y[i] -= shoot_speed

    #     if b_y[i] <= ey + e_h and ex < b_x[i] < ex + e_w:  # 击中敌人
    #         b_y[i] = -500  # 子弹消失
    #         for i in range(1000):
    #             screen.blit(enemy2, (ex, ey))
    #         screen.blit(enemy3, (ex, ey))
    #         screen.blit(enemy4, (ex, ey))
    #         ey = random.randint(-60, -50)
    #         ex = random.randint(0 + e_w, 495 - e_w)

    pygame.display.update()

    # if a ==0:
    #     bx = hx - h_w / 10
    #     by = hy - h_h /2
    #     a = 1
    # by -= shoot_speed
    # screen.blit(bullet, (bx, by))
    # if by < 0:
    #     a = 0