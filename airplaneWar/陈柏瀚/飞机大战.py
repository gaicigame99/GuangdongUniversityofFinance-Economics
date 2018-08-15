import pygame
import random
import time

#飞机大战

pygame.init()
pygame.mixer.init()

move_list={}
#背景赋值
back_music=pygame.mixer.Sound("sound/game_music.ogg")
back_music.play()
screen=pygame.display.set_mode((495,800))
bg=pygame.image.load("images/background.png")
bg=pygame.transform.scale(bg,(495,800))

#背景位置
bgx = 0
bgy = 0
move_list["背景位置"] = [bgx, bgy]

#游戏名字
game_name=pygame.image.load("images/name.png")
name_rect=game_name.get_rect()
ntx=35
nty=50
move_list["按钮0位置"]=[ntx,nty]

# 摆放开始按钮
start1 = pygame.image.load("images/game_resume_nor.png")
start1_rect = start1.get_rect()
btx = 247
bty = 400
move_list["按钮1位置"] = [btx, bty]

# 开始深色按钮
star2 = pygame.image.load("images\game_resume_pressed.png")
gtx = 247
gty = 400
move_list["按钮2位置"] = [gtx, gty]
#背景，文字移动速度
speedx = 0
speedy = 0

# 游戏开始计时器
game_start_time = 150

game_start = 0

#飞机类
class hero(object):
    def __init__(self,_screen,_x,_y):
        self.image=pygame.image.load("images/hero.gif")
        self.x=_x
        self.y=_y
        self.screen=_screen
        self.rect=self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
    def show(self):
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))
    def move(self):
        self.x, self.y = pygame.mouse.get_pos()
#子弹类
class button(object):
    def __init__(self,_screen,hero):
        self.image=pygame.image.load("images/bullet.png")
        self.x=[]
        self.y=[]
        self.screen=_screen
        self.speed = 3
        self.v = 5
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.time=5
        self.hero=hero
        self.score=0

    def show(self):
        for i in range(len(self.x)):
            screen.blit(self.image, (self.x[i], self.y[i]))
            self.y[i] -= self.speed
            # if self.y[i]>800 and self.y[i]<0:
            #     self.y.pop(i)
            #     self.x.pop(i)
        for i in self.y:
            index = self.y.index(i)
            if i <0:
                self.y.pop(index)
                self.x.pop(index)

    def addbutton(self):
        if self.time:
            self.time -= 1
        else:
            # 添加子弹位置
            self.x.append(self.hero.x - self.width / 2 + 2)
            self.y.append(self.hero.y - self.hero.height / 2 - self.height)
            self.time = self.v

    def collection(self,enemy):
        for i in range(len(self.x)):
            for j in range(len(enemy.x)):
                if self.x[i] + self.rect.width > enemy.x[j] and \
                        self.x[i] < enemy.x[j] + enemy.width and \
                        self.y[i] < enemy.y[j] + enemy.height and \
                        self.y[i] + self.rect.height > enemy.y[j]:
                    self.y[i] = -100
                    if enemy.blood[j]==0:
                        enemy.y[j] = 900
                        self.score += 1
                    else:
                        enemy.blood[j]-=1
                        self.score+=1
                else:
                    pass

#敌人类
class enemy(object):
    def __init__(self,_screen,_type):
        self.type=_type
        self.etype=["images/enemy0.png","images/enemy1.png",
                    "images/enemy2.png"]
        self.image = pygame.image.load(self.etype[_type])
        self.x = []
        self.y = []
        self.blood = []
        self.screen = _screen
        self.speed = []
        self.v = 50
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.level = 5

    def show(self):
        if self.level:
            self.level -= 1
        else:
            self.y.append(random.randint(-500, -30))
            self.x.append(random.randint(0, 495 - int(self.width)))
            self.speed.append(random.randint(2, 3))
            self.level = self.v
            if self.type==0:
                self.blood.append(0)
            elif self.type==1:
                self.blood.append(1)
            elif self.type==2:
                self.blood.append(2)


    def move(self):
        for i in range(len(self.x)):
            screen.blit(self.image, (self.x[i], self.y[i]))
            self.y[i] += self.speed[i]
            pygame.draw.line(self.screen,(220,20,60),(self.x[i],self.y[i]+self.height+5),(self.x[i]+self.width,self.y[i]+self.height+5),5)
           #飞机去血
            if self.type==1:
                if self.blood[i]==0:
                    pygame.draw.line(self.screen, (128, 128, 128), (self.x[i]+self.width/2, self.y[i] + self.height + 5),
                                     (self.x[i] + self.width, self.y[i] + self.height + 5), 5)
            if self.type==2:
                if self.blood[i]==1:
                    pygame.draw.line(self.screen, (128, 128, 128), (self.x[i]+2*self.width/3, self.y[i] + self.height + 5),
                                     (self.x[i] + self.width, self.y[i] + self.height + 5), 5)
                if self.blood[i]==0:
                    pygame.draw.line(self.screen, (128, 128, 128), (self.x[i] +  self.width / 3, self.y[i] + self.height + 5),
                                     (self.x[i] + self.width, self.y[i] + self.height + 5), 5)

         # 存储优化
        for i in self.y:
            index = self.y.index(i)
            if i > 800:
                self.y.pop(index)
                self.x.pop(index)
                self.blood.pop(index)

#初始化
heroA=hero(screen,247,800)
enemyA=enemy(screen,0)
enemyB=enemy(screen,1)
enemyC=enemy(screen,2)
buttonA=button(screen,heroA)

#得分文字类型
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # 开始游戏逻辑
    screen.blit(bg, (0, 0))
    #显示得分
    show_score = font.render("得分：" + str(buttonA.score), True, (0, 0, 0))
    screen.blit(show_score,(0,0))
    screen.blit(bg, (move_list["背景位置"][0], move_list["背景位置"][1]))
    a,b,c = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()


    if mouse_x > btx and mouse_x < btx+start1_rect.width and mouse_y> bty and mouse_y < bty + start1_rect.height and a:
        screen.blit(start1, (move_list["按钮1位置"][0], move_list["按钮1位置"][1]))
        screen.blit(game_name,(move_list["按钮0位置"][0],move_list["按钮0位置"][1]))
        speedx = 0
        speedy = -30
        game_start = 1
    else:
        screen.blit(star2, (move_list["按钮2位置"][0], move_list["按钮2位置"][1]))
        screen.blit(game_name,(move_list["按钮0位置"][0],move_list["按钮0位置"][1]))

    for i in move_list:
        move_list[i][0] += speedx
        move_list[i][1] += speedy


    if game_start:
        game_start_time -= 1

    if game_start and game_start_time<0:
        heroA.move()
        buttonA.addbutton()
        # 添加子弹位置
        heroA.show()
        #子弹绘制移动
        buttonA.show()
        #添加飞机
        enemyA.show()
        enemyB.show()
        enemyC.show()
        #碰撞检测
        buttonA.collection(enemyA)
        buttonA.collection(enemyB)
        buttonA.collection(enemyC)
        #飞机移动
        enemyA.move()
        enemyB.move()
        enemyC.move()

    pygame.display.update()