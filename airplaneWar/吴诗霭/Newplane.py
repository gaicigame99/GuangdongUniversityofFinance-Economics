import pygame
import random

class bullet(object):
    def __init__(self,screen,b_p):
        self.image = b_p
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = []
        self.y = []
        self.r = self.rect.width / 2
        self.speed = 3
        self.v = 20
        self.time = self.v

    def show(self,hx,hy,h_height):
        if self.time:
            self.time -= 1
        else:
            self.x.append(hx - self.r)
            self.y.append(hy - h_height / 2 - self.r)
            self.time = self.v
        for i in range(len(self.x)):
            screen.blit(self.image, (self.x[i], self.y[i]))
            self.y[i] -= self.speed
        for i in self.y:
            index = self.y.index(i)
            if i < 0:
                self.x.pop(index)
                self.y.pop(index)

class enemy(object):
    def __init__(self, screen,enemy,enemy_down1,enemy_down2,enemy_down3,enemy_down4,number,e_s):
        self.image0 = enemy
        self.image1 = enemy_down1
        self.image2 = enemy_down2
        self.image3 = enemy_down3
        self.image4 = enemy_down4
        self.rect = self.image0.get_rect()
        self.screen = screen
        self.w = self.rect.width
        self.h = self.rect.height
        self.x = []
        self.y = []
        self.blood = []  # 生命值为图片列表长度
        self.p = []
        self.n = number
        self.speed = e_s * 0.5
        self.photos = [self.image4, self.image3, self.image2, self.image1, self.image0]
        while True:
            if len(self.y) == self.n:
                break
            self.y.append(random.randint(-40, -10) * 10)
        while True:
            if len(self.x) == self.n:
                break
            self.x.append(random.randint(5, 45) * 10)
        #   敌机添加血槽
        while True:
            if len(self.blood) == self.n:
                break
            self.blood.append(len(self.photos) - 1)
        #   敌机添加默认图片
        while True:
            if len(self.p) == self.n:
                break
            self.p.append(self.image0)

    def show(self,score,bx,by,br):
        for i in range(self.n):
            self.y[i] += self.speed
            self.p[i] = self.photos[self.blood[i]]
            pygame.draw.line(screen, (255, 0, 0), (self.x[i], self.y[i] + self.h + 6), (self.x[i] + self.w * self.blood[i] * 0.25, self.y[i] + self.h + 6),6)
            pygame.draw.line(screen, (255,255,255), (self.x[i] + self.w * self.blood[i] * 0.25, self.y[i] + self.h + 6),(self.x[i] + self.w * 4 * 0.25, self.y[i] + self.h + 6), 6)

            for j in range(len(bx)):
                if (self.x[i] - br) <= bx[j] <= (self.x[i] + self.w + br) and self.y[i] <= by[j] <= (self.y[i] + self.h + br):
                    self.blood[i] -= 1
                    by[j] = -100

            if self.y[i] >= 800:
                self.y[i] = random.randint(-20, -10) * 10
                self.x[i] = random.randint(5, 45) * 10
                print(self.x)
                print(self.y)

            if self.blood[i] == 0:
                self.p[i] = self.photos[self.blood[i]]
                screen.blit(self.p[i], (self.x[i], self.y[i]))
                self.y[i] = random.randint(-200, -100)
                self.x[i] = random.randint(5, 45) * 10
                self.blood[i] = len(self.photos) - 1
                score += 1
                print(self.blood)
                print(self.p)

            screen.blit(self.p[i], (self.x[i], self.y[i]))
        return score

class hero(object):
    def __init__(self,screen):
        self.image = pygame.image.load(r"images\hero.gif")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = 100
        self.y = 100
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = []
        self.y = []

    def show(self,x,y):
        self.x = x
        self.y = y
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))

pygame.init()
pygame.mixer.init()

bgm = pygame.mixer.Sound("sound\game_music.ogg")
bgm.play()

screen = pygame.display.set_mode((495, 800))
button_p = pygame.image.load(r"images\button_p.png")
button_np = pygame.image.load(r"images\button_nor.png")
name = pygame.image.load(r"images\name.png")

game_pause = pygame.image.load(r"images\game_pause_pressed.png")
game_resume = pygame.image.load(r"images\game_resume_pressed.png")
quit = pygame.image.load(r"images\quit_sel.png")
restart = pygame.image.load(r"images\restart_sel.png")
resume = pygame.image.load(r"images\resume_sel.png")

font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",24)
title = pygame.font.Font("C:\Windows\Fonts\Verdana.ttf",56)

hero_blowup = pygame.image.load(r"images\hero_blowup_n3.png")
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))
bgover = pygame.image.load(r"images\gameover.png")
bgover = pygame.transform.scale(bgover, (495, 800))

enemy0 = pygame.image.load(r"images\enemy0.png")
enemy0_down1 = pygame.image.load(r"images\enemy0_down1.png")
enemy0_down2 = pygame.image.load(r"images\enemy0_down2.png")
enemy0_down3 = pygame.image.load(r"images\enemy0_down3.png")
enemy0_down4 = pygame.image.load(r"images\enemy0_down4.png")
enemy1 = pygame.image.load(r"images\enemy1.png")
enemy1_down1 = pygame.image.load(r"images\enemy1_down1.png")
enemy1_down2 = pygame.image.load(r"images\enemy1_down2.png")
enemy1_down3 = pygame.image.load(r"images\enemy1_down3.png")
enemy1_down4 = pygame.image.load(r"images\enemy1_down4.png")
enemy2 = pygame.image.load(r"images\enemy2.png")
enemy2_down1 = pygame.image.load(r"images\enemy2_down1.png")
enemy2_down2 = pygame.image.load(r"images\enemy2_down2.png")
enemy2_down3 = pygame.image.load(r"images\enemy2_down3.png")
enemy2_down4 = pygame.image.load(r"images\enemy2_down4.png")

bullet0 = pygame.image.load(r"images\bullet.png")
bullet1 = pygame.image.load(r"images\bullet1.png")
bullet2 = pygame.image.load(r"images\bullet2.png")
bullets = [bullet0,bullet1,bullet2]

score = 0
bulletA = bullet(screen,bullets[0])
bulletB = bullet(screen,bullets[1])
bulletC = bullet(screen,bullets[2])
enemyA = enemy(screen,enemy0,enemy0_down1,enemy0_down2,enemy0_down3,enemy0_down4,3,3)
enemyB = enemy(screen,enemy1,enemy1_down1,enemy1_down2,enemy1_down3,enemy1_down4,2,2)
enemyC = enemy(screen,enemy2,enemy2_down1,enemy2_down2,enemy2_down3,enemy2_down4,1,1)
heroA = hero(screen)
flag = 1 #启动开始界面

def startscreen(a,mx,my):
    screen.blit(bg, (0, 0))
    screen.blit(name, (40, 100))
    screen.blit(button_np, (195, 250))
    text2 = font.render("Start", True, (255, 255, 255))
    screen.blit(text2, (235, 260))
    if a and (195 <= mx <= 325) and (250 <= my <= 300):
        return 0
    else:
        return 1

def resumescreen(a,mx,my):
    screen.blit(bg, (0, 0))
    screen.blit(name, (40, 100))
    screen.blit(resume, (210, 250))
    screen.blit(quit, (195, 350))
    screen.blit(game_resume, (430, 740))
    if (a and 195 < mx < 250 and 250 < my < 275 ):
        return 0
    elif a and 195 < mx < 325 and 350 < my < 375:
        return 3
    else:
        return 2

def overscreen(score):
    screen.blit(bg, (0, 0))
    text_score = title.render("Score:" + str(score), True, (255, 255, 255))
    screen.blit(text_score, (110, 250))
    bgm.stop()

while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    mx, my = pygame.mouse.get_pos()
    a, b, c = pygame.mouse.get_pressed()

    if flag == 1:
        flag = startscreen(a,mx,my)
    elif flag == 2:
        flag = resumescreen(a,mx,my)
    elif flag == 3:
        overscreen(score)
    elif flag == 0:
        screen.blit(game_pause, (430, 740))
        heroA.show(mx, my)
        if score <= 10:
            bulletA.show(mx, my, heroA.height)
            score = enemyA.show(score, bulletA.x, bulletA.y, bulletA.r)
            score = enemyB.show(score, bulletA.x, bulletA.y, bulletA.r)
        elif 10 < score <= 25:
            bulletB.show(mx, my, heroA.height)
            score = enemyB.show(score, bulletB.x, bulletB.y, bulletB.r)
            score = enemyC.show(score, bulletB.x, bulletB.y, bulletB.r)
        else:
            bulletC.show(mx, my, heroA.height)
            score = enemyA.show(score, bulletC.x, bulletC.y, bulletC.r)
            score = enemyB.show(score, bulletC.x, bulletC.y, bulletC.r)
            score = enemyC.show(score, bulletC.x, bulletC.y, bulletC.r)

        if a and 430 < mx < 480 and 740 < my < 795:
            screen.blit(game_resume, (430, 740))
            flag = 2

        use_score ="    Score:" + str(score)
        text1 = font.render(use_score, True, (255, 255, 255))
        screen.blit(text1, (0, 750))
    print(flag)
    pygame.display.update()