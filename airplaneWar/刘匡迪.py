import pygame
import random

pygame.init()
pygame.mixer.init()
#背景 屏幕
screen = pygame.display.set_mode((495, 800))
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",24)

bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))
back_mousic= pygame.mixer.Sound("sound\game_music.ogg")
back_mousic1= pygame.mixer.Sound("sound\enemy1_down.wav")
back_mousic2= pygame.mixer.Sound("sound\enemy2_down.wav")
back_mousic3= pygame.mixer.Sound("sound\enemy3_down.wav")
back_mousic.play(-1)
#英雄类
class Hero(object):
    def __init__(self):
        self.image = pygame.image.load("images\hero1.png")
        self.image1 = pygame.image.load("images\hero2.png")
        self.image2 = pygame.image.load("images\hero_blowup_n1.png")
        self.image3 = pygame.image.load("images\hero_blowup_n2.png")
        self.image4 = pygame.image.load("images\hero_blowup_n3.png")
        self.image5 = pygame.image.load("images\hero_blowup_n4.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
    def show(self,x,y,ticks):
        if ticks % 50 < 25:
            screen.blit(self.image, (mouse_x - self.width / 2, mouse_y - self.height / 2))
        else:
            screen.blit(self.image1, (mouse_x - self.width / 2, mouse_y - self.height / 2))
hero=Hero()
ticks = 0
#敌人类
class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load("images\\enemy0.png")
        self.image1 = pygame.image.load("images\enemy0_down1.png")
        self.image2 = pygame.image.load("images\enemy0_down2.png")
        self.image3 = pygame.image.load("images\enemy0_down3.png")
        self.image4 = pygame.image.load("images\enemy0_down4.png")
        self.rect = self.image.get_rect()
        self.enemy_x = []
        self.enemy_y = []
        self.des = []
        self.speed_y = 1
        for i in  range(10):
            self.enemy_x.append(random.randint(0, 495 - 51))
            self.enemy_y.append(random.randint(-500, -100))
            self.des.append(0)
    # def add(self):
    #     for k in range(self.num):
    #         self.enemy_x.append(random.randint(0, 495 - 51))
    #         self.enemy_y.append(random.randint(-400, -300))
    def show(self):
        for i in range(len(self.enemy_x)):
            self.enemy_y[i] += self.speed_y
            screen.blit(self.image, (self.enemy_x[i], self.enemy_y[i]))
            # pygame.draw.rect(screen, [0,225, 0], [self.enemy_x[i], self.enemy_y[i],69,5] )
            # pygame.draw.rect(screen, [225,0, 0], [self.enemy_x[i]+35, self.enemy_y[i], 35, 5])
            if self.enemy_y[i] > 800:
                self.enemy_y[i] = random.randint(-200,-100)

    def check(self,bullet):
        for i in range(len(bullet.bx)):
            for j in range(len(self.enemy_x)):
                if collection(bullet.bx[i], bullet.by[i], bullet.rect, self.enemy_x[j], self.enemy_y[j], self.rect):
                    back_mousic2.play()
                    bullet.by[i] =-40
                    self.des.append(j)
                    # self.enemy_y[j]=800
class Enemy1(object):
    def __init__(self):
        self.image = pygame.image.load("images\\enemy1.png")
        self.image1 = pygame.image.load("images\enemy1_down1.png")
        self.image2 = pygame.image.load("images\enemy1_down2.png")
        self.image3 = pygame.image.load("images\enemy1_down3.png")
        self.image4 = pygame.image.load("images\enemy1_down4.png")
        self.rect = self.image.get_rect()
        self.enemy_x = []
        self.enemy_y = []
        self.des = []
        self.speed_y = 0.6
        self.blood=[]
        for i in range(10):
            self.enemy_x.append(random.randint(0, 495 - 51))
            self.enemy_y.append(random.randint(-600, -500))
            self.des.append(0)
            self.blood.append(3)


    # def add(self):
    #     for k in range(self.num):
    #         self.enemy_x.append(random.randint(0, 495 - 51))
    #         self.enemy_y.append(random.randint(-400, -300))
    def show(self):
        for i in range(len(self.enemy_x)):
            self.enemy_y[i] += self.speed_y
            screen.blit(self.image, (self.enemy_x[i], self.enemy_y[i]))
            if self.blood[i] == 3:
                pygame.draw.rect(screen, [0,225, 0], [self.enemy_x[i], self.enemy_y[i],self.rect.width,5] )
            if self.blood[i] ==2:
                pygame.draw.rect(screen, [0, 225, 0], [self.enemy_x[i], self.enemy_y[i], self.rect.width, 5])
                pygame.draw.rect(screen, [225, 0, 0], [self.enemy_x[i] + self.rect.width//2, self.enemy_y[i], self.rect.width//2, 5])
            if self.blood[i] ==1:
                pygame.draw.rect(screen, [225, 0, 0], [self.enemy_x[i] , self.enemy_y[i], self.rect.width, 5])
            if self.enemy_y[i] > 800:
                self.enemy_y[i] = 800


    def check(self, bullet):
        for i in range(len(bullet.bx)):
            for j in range(len(self.enemy_x)):
                if collection(bullet.bx[i], bullet.by[i], bullet.rect, self.enemy_x[j], self.enemy_y[j],
                              self.rect):
                    back_mousic2.play()
                    bullet.by[i] = -40
                    self.blood[j]-=1
                    if self.blood[j] ==0:
                        self.des.append(j)


                    # self.enemy_y[j]=800
class Enemy2(object):
    def __init__(self):
        self.image = pygame.image.load("images\\enemy2.png")
        self.image1 = pygame.image.load("images\enemy2_down1.png")
        self.image2 = pygame.image.load("images\enemy2_down2.png")
        self.image3 = pygame.image.load("images\enemy2_down3.png")
        self.image4 = pygame.image.load("images\enemy2_down4.png")
        self.rect = self.image.get_rect()
        self.enemy_x = []
        self.enemy_y = []
        self.des = []
        self.speed_y = 0.3
        self.blood = []
        for i in range(10):
            self.enemy_x.append(random.randint(0, 495 - 51))
            self.enemy_y.append(random.randint(-800, -600))
            self.des.append(0)
            self.blood.append(10)

    # def add(self):
    #     for k in range(self.num):
    #         self.enemy_x.append(random.randint(0, 495 - 51))
    #         self.enemy_y.append(random.randint(-400, -300))
    def show(self):
        for i in range(len(self.enemy_x)):
            self.enemy_y[i] += self.speed_y
            screen.blit(self.image, (self.enemy_x[i], self.enemy_y[i]))
            if self.blood[i] in(9,11):
                pygame.draw.rect(screen, [0,225, 0], [self.enemy_x[i], self.enemy_y[i],self.rect.width,5] )
            if self.blood[i] in(7,9):
                pygame.draw.rect(screen, [0, 225, 0], [self.enemy_x[i] , self.enemy_y[i], self.rect.width*0.8, 5])
                pygame.draw.rect(screen, [225, 0, 0], [self.enemy_x[i]+ self.rect.width*0.8, self.enemy_y[i], self.rect.width*0.2, 5])
            if self.blood[i] in(5,7):
                pygame.draw.rect(screen, [0, 225, 0], [self.enemy_x[i] , self.enemy_y[i], self.rect.width//2, 5])
                pygame.draw.rect(screen, [225, 0, 0], [self.enemy_x[i]+ self.rect.width//2, self.enemy_y[i], self.rect.width*0.5, 5])
            if self.blood[i] in(2,5):
                pygame.draw.rect(screen, [0, 225, 0], [self.enemy_x[i] , self.enemy_y[i], self.rect.width*0.3, 5])
                pygame.draw.rect(screen, [225, 0, 0], [self.enemy_x[i]+ self.rect.width*0.3, self.enemy_y[i], self.rect.width*0.7, 5])
            if self.blood[i] ==1:
                pygame.draw.rect(screen, [225, 0, 0], [self.enemy_x[i] , self.enemy_y[i], self.rect.width, 5])
            if self.enemy_y[i] > 800:
                self.enemy_y[i] = 800
            pygame.draw.rect(screen, [0,225, 0], [self.enemy_x[i], self.enemy_y[i],69,5] )
            pygame.draw.rect(screen, [225,0, 0], [self.enemy_x[i]+35, self.enemy_y[i], 35, 5])
            if self.enemy_y[i] > 800:
                self.enemy_y[i] = 800

    def check(self, bullet):
        for i in range(len(bullet.bx)):
            for j in range(len(self.enemy_x)):
                if collection(bullet.bx[i], bullet.by[i], bullet.rect, self.enemy_x[j], self.enemy_y[j],
                              self.rect):
                    back_mousic2.play()
                    bullet.by[i] = -40
                    self.blood[j] -= 1
                    if self.blood[j] == 0:
                        self.des.append(j)
                    # self.enemy_y[j]=800
#碰撞检测
def collection(bax, bay, ball_rt, blx, bly, block_rect):
    if bax + ball_rt.width > blx and \
                    bax < blx + block_rect.width and \
                    bay < bly + block_rect.height and \
                            bay + ball_rt.height > bly:
        return True
    else:
        return False

                    # self.screen.blit(bullet, (b_x[i], b_y[i]))
                    # self.enemy_x[j], self.enemy_y[j] = 1000, 1000
                    # self.n_num = 0
                # if self.enemy_y[j] > 800:
                #     self.enemy_x[j], self.enemy_y[j] = randint(0, 495 - 15), randint(-600, -300)
#爆炸动画
def boom(tick,diren):
    for i in diren.des:
        if tick in range(0,10):
            screen.blit(diren.image1, (diren.enemy_x[i],diren.enemy_y[i]))
        elif tick in range(10,20):
            screen.blit(diren.image2, (diren.enemy_x[i],diren.enemy_y[i]))
        elif tick in range(30,40):
            screen.blit(diren.image3, (diren.enemy_x[i],diren.enemy_y[i]))
        elif tick in range(40,50):
            screen.blit(diren.image4, (diren.enemy_x[i],diren.enemy_y[i]))
enemy=Enemy()
enemy1=Enemy1()
enemy2=Enemy2()
#子弹类
class Bullet(object):
    def __init__(self):
        self.image = pygame.image.load(r"images\bullet.png")
        self.image1 = pygame.image.load(r"images\bullet1.png")
        self.image2 = pygame.image.load(r"images\bullet2.png")
        self.rect = self.image.get_rect()
        self.bx =[]
        self.by = []
        self.speed=3
        self.kind=0      #0(buttet号子弹)，1（buttet1号子弹），>2（buttet1号子弹）
    def add_b(self,time1,x,y):
        if time1:
            time1=time1-1
            return  time1
        else:
            # 添加子弹的位置
            self.bx.append(x - self.rect.width / 2 + 2)
            self.by.append(y - 124 / 2 - self.rect.height)
            # 重置 添加频率
            return 20

    def shoot(self,kind):
        for i in range(len(self.bx)):
            if kind==0:
                screen.blit(self.image, (self.bx[i],self.by[i]))    #显示子弹
            if kind==1 :
                screen.blit(self.image1, (self.bx[i],self.by[i]))  # 显示子弹
            if kind==2:
                screen.blit(self.image2, (self.bx[i],self.by[i]))  # 显示子弹
            self.by[i]-=self.speed
                       #子弹速度
    def clean (self):
        for i in self.by:
            index = self.by.index(i)
            if i < 0:
                self.by.pop(index)
                self.bx.pop(index)
time1=20
bullet=Bullet()
#道具类
class tool(object):
    def __init__(self):
        self.image = pygame.image.load("images\\bomb-1.gif")
        self.image1 = pygame.image.load("images\\bomb-2.gif")
        self.rect = self.image.get_rect()
        self.x =random.randint(20, self.rect.width)
        self.y = random.randint(-self.rect.height,0)
        self.speed_y = 1.5
    def show(self,_num):
        if _num==1:
            screen.blit(self.image1, (self.x, self.y))
        elif _num ==2:
            screen.blit(self.image, (self.x, self.y))
        self.y += self.speed_y
        self.x += random.randint(-5,5)
        if self.y > 800:
            self.y=self.y = random.randint(-self.rect.height,0)
    def check(self,x,y,her,):
        if (self.x< x+her.width//2 and self.x+self.rect.width>x-her.width//2 and self.y<y+her.height//2 and self.y+self.rect.height>y-her.height):
            self.y = random.randint(-900, -600)




                    # self.enemy_y[j]=800
Tool=tool()
# b_x = []  #
# b_y = []
# b_speed = 3
# b_v = 20
# time1 = b_v
# 计数ticks == new add ==
tick=0
score=0
clock = pygame.time.Clock()  # 帧率可以理解为游戏在一秒钟内进行多少次画面刷新

while True:
    # clock.tick(60)  # 一秒内刷新60次 限制游戏的最大帧率
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # 绘制背景
    screen.blit(bg, (0, 0))
    use_score = "    Score:" + str(score)
    text1 = font.render(use_score, True, (255, 255, 255))
    screen.blit(text1, (0, 750))
    #绘制飞机
    hero.show(mouse_x, mouse_y,ticks)
    ticks += 1
    #发射子弹
    time1 = bullet.add_b(time1,mouse_x, mouse_y)
    bullet.clean()
    bullet.shoot(1)
    #绘制敌人
    enemy.show()
    enemy.check(bullet) #碰撞检测 但不要马上 改变敌人Y坐标
    enemy1.show()
    enemy1.check(bullet)  # 碰撞检测 但不要马上 改变敌人Y坐标
    enemy2.show()
    enemy2.check(bullet)  # 碰撞检测 但不要马上 改变敌人Y坐标

    # 爆炸动画
    boom(tick,enemy)
    boom(tick,enemy1)
    boom(tick,enemy2)
    Tool.show(1)
    Tool.check(mouse_x, mouse_y, hero)
    if tick>50 :

        for i in enemy.des:
            enemy.des[i] = 0
            enemy.enemy_y[i] = 800
            score+=1
        for i in enemy1.des:
            enemy1.des[i] = 0
            enemy1.enemy_y[i] = 800
            score += 5
        for i in enemy2.des:
            enemy2.des[i] = 0
            enemy2.enemy_y[i] = 800
            score += 10
        tick=0
    tick += 1

    pygame.display.update()