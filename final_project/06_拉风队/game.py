import pygame
import random
def begin():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((800, 600))
    bg0 = pygame.image.load(r"images\bg2.jpg")
    bg1 = pygame.image.load(r"images\bg1.jpg")
    play = pygame.image.load(r"images\play2.png")
    dog_p = pygame.image.load(r"images\dog.png")
    dog_p2 = pygame.image.load(r"images\dog2.png")
    xin = pygame.image.load(r"images\xin.png")

    df = pygame.image.load(r"images\df.png")
    bg2 = pygame.image.load(r"images\gameover.png")
    dog_p3 = pygame.image.load(r"images\dog3.png")
    dog_p4 = pygame.image.load(r"images\dog4.png")

    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",36)

    d_blood = 50
    d_num = 0

    px = 0
    py = 300

    xx = 350
    xy = 300

    dog3_x = 0
    dog3_y = 540
    dog4_x = 0
    dog4_y = 150
    dog4_s = 5

    flag = 0
    flag1 = 1
    score = 0

    #   dog
    class dog(object):
        def __init__(self, screen,number):
            self.image = dog_p
            self.image2 = dog_p2
            self.rect = self.image.get_rect()
            self.screen = screen
            self.w = self.rect.width
            self.h = self.rect.height
            self.x = []
            self.y = []
            self.n = number
            self.num = 0
            self.xspeed = []
            self.yspeed = []
            while True:
                if len(self.y) == self.n:
                    break
                self.y.append(random.randint(0, 5) * 100)
            while True:
                if len(self.x) == self.n:
                    break
                self.x.append(random.randint(8,12) * 100)
            while True:
                if len(self.xspeed) == self.n:
                    break
                self.xspeed.append(random.randint(1,2))
            while True:
                if len(self.yspeed) == self.n:
                    break
                self.yspeed.append(random.randint(1,3))

        def show(self,xx,xy,d_blood,flag1,flag,py,photo,score):
            for i in range(self.n):
                self.x[i] -= self.xspeed[i]
                self.y[i] += self.yspeed[i]
                #   当心未触碰狗粮时
                if flag1 == 1:
                    #   生命值
                    pygame.draw.line(screen, (255, 0, 0), (0, 10), (d_blood * 5, 10), 10)
                    pygame.draw.line(screen, (255, 255, 255), (d_blood * 5, 10), (250, 10), 10)
                    if self.x[i] <= xx <= self.x[i] + 50 and self.y[i] <= xy <= self.y[i] + 50:
                        d_blood -= 1
                    if self.x[i] <= 0:
                        self.y[i] = random.randint(1, 5) * 100
                        self.x[i] = random.randint(8,20) * 100
                        self.xspeed[i] = random.randint(1,2)
                        self.yspeed[i] = random.randint(1,3)
                    if self.y[i] <= 0 or self.y[i] >= 550:
                        self.yspeed[i] = - self.yspeed[i]
                    photo = self.image2

                #   鼠标所移动的图案变狗粮后
                elif flag1 == 0:
                    text1 = font.render("   Dogs:" + str(self.n - self.num), True, (255, 255, 255))
                    screen.blit(text1, (0, 5))
                    if self.y[i] <= 10 or self.y[i] >= 500:
                        self.yspeed[i] = - self.yspeed[i]
                    if self.x[i] - 50 <= xx <= self.x[i] + 100 and self.y[i] - 50 <= xy <= self.y[i] + 70:
                        self.x[i] = -100
                        self.y[i] = -100
                        self.num += 1
                        #print(self.x)
                        #print(self.y)
                        for j in range(len(self.x)):
                            if (self.x[j] <= -100 and self.y[j]) > 0 or(self.x[j] >= 0 and self.y[j] <= -100):
                                self.y[j] = random.randint(1, 5) * 100
                                self.x[j] = random.randint(8, 20) * 100
                                self.xspeed[j] = random.randint(1, 2)
                                self.yspeed[j] = random.randint(1, 3)
                    #   当消灭20只时score则为1，此时退出该游戏页面
                    if self.num == 20:
                        score += 1
                        flag = 4
                        py = 200
                        self.num = 0
                        flag1 = 1
                    photo = self.image
                screen.blit(photo, (self.x[i], self.y[i]))
            return d_blood,flag,py,flag1,score

    dogA = dog(screen,20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            pressed_keys = pygame.key.get_pressed()
            # 角色移动
            if event.type == pygame.KEYDOWN:
                if flag == 0:
                    if (chr(event.key) == "a" or pressed_keys[pygame.K_LEFT])and px > 0:
                        px -= 50
                    elif (chr(event.key) == "d"or pressed_keys[pygame.K_RIGHT]) and px < 700:
                        px += 50
                    elif (chr(event.key) == "w"or pressed_keys[pygame.K_UP]) and py >= 200:
                        py -= 50
                    elif (chr(event.key) == "s"or pressed_keys[pygame.K_DOWN]) and py <= 350:
                        py += 50
                elif flag == 1:
                    if (chr(event.key) == "a" or pressed_keys[pygame.K_LEFT])and xx > 0:
                        xx -= 50
                    elif (chr(event.key) == "d"or pressed_keys[pygame.K_RIGHT]) and xx < 800:
                        xx += 50
                    elif (chr(event.key) == "w"or pressed_keys[pygame.K_UP]) and xy > 0:
                        xy -= 50
                    elif (chr(event.key) == "s"or pressed_keys[pygame.K_DOWN]) and xy <= 550:
                        xy += 50
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        if px == 700 and score < 1:
            flag = 2
            px = 0
            py = 350
        # if px == 700 and score >= 1:
        #     flag = 4

        #   小游戏页面
        if flag == 1:
            screen.blit(bg0, (0, 0))
            screen.blit(df, (0,500))
            #   当生命值为零时退出小游戏界面
            if d_blood <= 0:
                flag = 2
            #   当鼠标移动到狗粮时则变身
            if 0 <= xx <= 100 and 500 <= xy <= 580:
                flag1 = 0
            #   显示dog
            d_blood, flag, py, flag1,score = dogA.show(xx, xy, d_blood,flag1,flag,py,0,score)
            #   变身标志
            if flag1:
                screen.blit(xin, (xx, xy))
            else:
                screen.blit(df, (xx, xy))

        #   初始游戏界面
        elif flag == 0:
            screen.blit(bg1, (0, 0))
            screen.blit(play, (px, py))
            #   到达小游戏点时触发小游戏
            if px == 400 and py == 150:
                flag = 1
        #   gameover页面
        elif flag == 2:
            screen.blit(bg2, (0, 0))
            screen.blit(dog_p3, (dog3_x, dog3_y))
            dog3_x += 2
            if dog3_x >= 800:
                dog3_x = 0
                flag = 0
                py += 100
                d_blood = 50
        #   胜利页面
        elif flag == 4:
            screen.blit(bg0, (0, 0))
            screen.blit(dog_p4, (dog4_x,dog4_y))

            if dog4_x > 800 :
                screen.blit(bg2, (00, 00))
            else:
                screen.blit(bg2, (dog4_x - 800,0))
            dog4_x += 5
            dog4_y += dog4_s
            dog4_s = -dog4_s

        pygame.display.update()
