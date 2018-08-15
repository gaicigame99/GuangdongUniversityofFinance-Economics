import pygame
import random
import time

pygame.init()

pygame.mixer.init()
back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
font_small = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 25)

screen = pygame.display.set_mode((495, 800))
background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background, (495, 800))

enemy0_down1 = pygame.image.load("images\enemy0_down1.png")
enemy0_down2 = pygame.image.load("images\enemy0_down2.png")
enemy0_down3 = pygame.image.load("images\enemy0_down3.png")
enemy0_down4 = pygame.image.load("images\enemy0_down4.png")

enemy1_down1 = pygame.image.load("images\enemy1_down1.png")
enemy1_down2 = pygame.image.load("images\enemy1_down2.png")
enemy1_down3 = pygame.image.load("images\enemy1_down3.png")
enemy1_down4 = pygame.image.load("images\enemy1_down4.png")

enemy2_down1 = pygame.image.load("images\enemy2_down1.png")
enemy2_down2 = pygame.image.load("images\enemy2_down2.png")
enemy2_down3 = pygame.image.load("images\enemy2_down3.png")
enemy2_down4 = pygame.image.load("images\enemy2_down4.png")
enemy2_down5 = pygame.image.load("images\enemy2_down5.png")
enemy2_down6 = pygame.image.load("images\enemy2_down6.png")


# 子弹类
class Bullet0(object):
    def __init__(self, _screen):
        self.image = pygame.image.load(r"images\bullet.png")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.x = []
        self.y = []
        self.speed = 3
        self.clip = 25
        self.time_up = 25

    def update(self, _hx, _hy, h_height):
        if self.time_up:
            self.time_up -= 1
        else:
            x = _hx - self.rect.width / 2 + 2
            y = _hy - h_height / 2 - self.rect.height
            self.x.append(x)
            self.y.append(y)
            self.time_up = self.clip

    def show(self):
        for i in range(len(self.y)):
            self.screen.blit(self.image, (self.x[i], self.y[i]))

    def move(self):
        for i in range(len(self.y)):
            self.y[i] -= self.speed
            if self.y[i] + self.rect.height < 0:
                self.y[i] = -1000

    def remove(self):
        for i in self.y:
            index = self.y.index(i)
            if i < 0:
                self.x.pop(index)
                self.y.pop(index)


# 英雄机类
class Hero(object):
    def __init__(self, _screen, _hx, _hy):
        self.image = pygame.image.load("images\hero.gif")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.x = _hx - self.rect.width / 2
        self.y = _hy - self.rect.height / 2


# 敌机类
class Enemy0(object):
    def __init__(self, _screen, _num):
        self.image = pygame.image.load("images\enemy0.png")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.x = []
        self.y = []
        for i in range(_num):
            self.x.append(random.randint(0, 495 - self.rect.width))
            self.y.append(-100)
        self.speed = 1

    def show(self):
        for i in range(len(self.x)):
            self.screen.blit(self.image, (self.x[i], self.y[i]))

    def remove(self, _index):
        self.x[_index] = random.randint(0, 495 - self.rect.width)
        self.y[_index] = -100

    def move(self):
        for i in range(len(self.y)):
            self.y[i] += self.speed
            if self.y[i] > 800:
                self.remove(i)


class Enemy1(Enemy0):
    def __init__(self, _screen, _num):
        self.image = pygame.image.load("images\enemy1.png")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.x = []
        self.y = []
        self.life = []
        for i in range(_num):
            self.x.append(random.randint(0, 495 - self.rect.width))
            self.y.append(-300)
            self.life.append(3)
        self.speed = 0.7

    def remove(self, _index):
        self.x[_index] = random.randint(0, 495 - self.rect.width)
        self.y[_index] = -300
        self.life[_index] = 5

    def show(self):
        for i in range(len(self.x)):
            self.screen.blit(self.image, (self.x[i], self.y[i]))
            pygame.draw.line(screen, GREEN_COLOR, (self.x[i], self.y[i]), (self.x[i] + self.rect.width, self.y[i]), 4)
            pygame.draw.line(screen, RED_COLOR, (self.x[i] + self.rect.width / 5 * self.life[i], self.y[i]),
                             (self.x[i] + self.rect.width, self.y[i]), 5)


class Enemy2(Enemy0):
    def __init__(self, _screen, _num):
        self.image = pygame.image.load("images\enemy2.png")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.x = []
        self.y = []
        self.life = []
        for i in range(_num):
            self.x.append(random.randint(0, 495 - self.rect.width))
            self.y.append(-600)
            self.life.append(5)
        self.speed = 0.4

    def remove(self, _index):
        self.x[_index] = random.randint(0, 495 - self.rect.width)
        self.y[_index] = -600
        self.life[_index] = 10

    def show(self):
        for i in range(len(self.x)):
            self.screen.blit(self.image, (self.x[i], self.y[i]))
            pygame.draw.line(screen, GREEN_COLOR, (self.x[i], self.y[i]), (self.x[i] + self.rect.width, self.y[i]), 4)
            pygame.draw.line(screen, RED_COLOR, (self.x[i] + self.rect.width / 10 * self.life[i], self.y[i]),
                             (self.x[i] + self.rect.width, self.y[i]), 5)


# 爆炸显示类
class Boom0(object):
    def __init__(self):
        self.past_time = []
        self.now_time = []
        self.boom_x = []
        self.boom_y = []
        self.loc = 0

    def add(self, box, boy):
        self.boom_x.append(box)
        self.boom_y.append(boy)
        self.past_time.append(time.time())
        self.now_time.append(time.time())

    def remove(self, ):
        for i in self.boom_y:
            index = self.boom_y.index(i)
            if i == self.loc:
                self.boom_x.pop(index)
                self.boom_y.pop(index)
                self.past_time.pop(index)
                self.now_time.pop(index)

    def judge(self):
        if len(self.past_time):
            for i in range(len(self.past_time)):
                self.now_time[i] = time.time()
                time_span = self.now_time[i] - self.past_time[i]
                if time_span < 0.2:
                    screen.blit(enemy0_down1, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.4:
                    screen.blit(enemy0_down2, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.6:
                    screen.blit(enemy0_down3, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.8:
                    screen.blit(enemy0_down4, (self.boom_x[i], self.boom_y[i]))
                else:
                    self.boom_y[i] = self.loc


class Boom1(Boom0):
    def judge(self):
        if len(self.past_time):
            for i in range(len(self.past_time)):
                self.now_time[i] = time.time()
                time_span = self.now_time[i] - self.past_time[i]
                if time_span < 0.2:
                    screen.blit(enemy1_down1, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.4:
                    screen.blit(enemy1_down2, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.6:
                    screen.blit(enemy1_down3, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.8:
                    screen.blit(enemy1_down4, (self.boom_x[i], self.boom_y[i]))
                else:
                    self.boom_y[i] = self.loc


class Boom2(Boom0):
    def judge(self):
        if len(self.past_time):
            for i in range(len(self.past_time)):
                self.now_time[i] = time.time()
                time_span = self.now_time[i] - self.past_time[i]
                print(time_span)
                if time_span < 0.2:
                    screen.blit(enemy2_down1, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.4:
                    screen.blit(enemy2_down2, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.6:
                    screen.blit(enemy2_down3, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 0.8:
                    screen.blit(enemy2_down4, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 1.0:
                    screen.blit(enemy2_down5, (self.boom_x[i], self.boom_y[i]))
                elif time_span < 1.2:
                    screen.blit(enemy2_down6, (self.boom_x[i], self.boom_y[i]))
                else:
                    self.boom_y[i] = self.loc


# 碰撞检测方法
def collection(b_x, b_y, b_rect, e_x, e_y, e_rect):
    if b_x + b_rect.width > e_x and \
            b_x < e_x + e_rect.width and \
            b_y < e_y + e_rect.height and \
            b_y + b_rect.height > e_y:
        return True
    else:
        return False


# 子弹初始化
bullet0 = Bullet0(screen)

# 敌机初始化
enemy0 = Enemy0(screen, 5)
enemy1 = Enemy1(screen, 3)
enemy2 = Enemy2(screen, 1)

# 爆炸初始化
boom0 = Boom0()
boom1 = Boom1()
boom2 = Boom2()

score = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(background, (0, 0))

    # 获取鼠标位置
    mou_x, mou_y = pygame.mouse.get_pos()

    # 绘制英雄机
    hero = Hero(screen, mou_x, mou_y)
    screen.blit(hero.image, (hero.x, hero.y))

    # 子弹更新
    bullet0.update(mou_x, mou_y, hero.rect.height)

    # 敌机的展示与移动
    enemy0.show()
    enemy0.move()

    enemy1.show()
    enemy1.move()

    enemy2.show()
    enemy2.move()

    # 子弹的展示与移动
    bullet0.show()
    bullet0.move()

    # 子弹与各种敌机的碰撞判断
    for i in range(len(bullet0.x)):
        for j in range(len(enemy0.x)):
            if collection(bullet0.x[i], bullet0.y[i], bullet0.rect, \
                          enemy0.x[j], enemy0.y[j], enemy0.rect):
                boom0.add(enemy0.x[j], enemy0.y[j])
                enemy0.remove(j)
                bullet0.y[i] = -1000
                score += 1

    for i in range(len(bullet0.x)):
        for j in range(len(enemy1.x)):
            if collection(bullet0.x[i], bullet0.y[i], bullet0.rect, \
                          enemy1.x[j], enemy1.y[j], enemy1.rect):
                enemy1.life[j] -= 1
                bullet0.y[i] = -1000
                if enemy1.life[j] == 0:
                    boom1.add(enemy1.x[j], enemy1.y[j])
                    enemy1.remove(j)
                    score += 5

    for i in range(len(bullet0.x)):
        for j in range(len(enemy2.x)):
            if collection(bullet0.x[i], bullet0.y[i], bullet0.rect, \
                          enemy2.x[j], enemy2.y[j], enemy2.rect):
                enemy2.life[j] -= 1
                bullet0.y[i] = -1000
                if enemy2.life[j] == 0:
                    boom2.add(enemy2.x[j], enemy2.y[j])
                    enemy2.remove(j)
                    score += 10
    # 子弹优化
    bullet0.remove()

    # 爆炸判断及优化
    boom0.judge()
    boom0.remove()

    boom1.judge()
    boom1.remove()

    boom2.judge()
    boom2.remove()

    # 显示分数
    text_score = font_small.render(str("score:%d" % score), True, BLACK_COLOR)
    screen.blit(text_score, (0, 15))

    pygame.display.update()
