
import pygame
from pygame.locals import *
import random

def begin():
    class jiangshi1(object):
        def __init__(self, _screen, _x, _y):
            self.image = pygame.image.load("images//僵尸.png")
            self.x = _x
            self.list_x = []
            self.y = _y
            self.list_y = []
            self.screen = _screen
            self.speed_x = 0.1
            self.blood = 10

        def show1(self):                                                #打印僵尸
            for i in range(len(self.list_x)):
                screen.blit(self.image, (self.list_x[i], self.list_y[i]))

        def show2(self):                                                #打印倒地的僵尸
            img = pygame.transform.rotate(self.image, 30)
            screen.blit(img, (self.x, self.y))

        def move(self):                                                 #僵尸移动
            for i in range(len(self.list_x)):
                self.list_x[i] -= self.speed_x

        def back(self):                                                 #僵尸被击倒后移动回屏幕外
            self.x = 1500


    class wandousheshou(object):
        def __init__(self, _screen, _x, _y):
            self.image = pygame.image.load("images//射手.png")
            self.zidan = pygame.image.load("images//子弹.png")
            self.zidan = pygame.transform.scale(self.zidan, (22, 22))
            self.x = _x                 #豌豆射手的x坐标
            self.list_x = []
            self.y = _y                 #豌豆射手的y坐标
            self.list_y = []
            self.screen = _screen
            self.zidan_speedx = 0.5     #子弹速度
            self.zidan_x = _x          #子弹x坐标初始化
            self.zidan_y = _y           #子弹y坐标初始化
            self.zidan_list_x = []
            self.zidan_list_y = []
            self.zidan_list_time = []             #射出时间
            self.zidan_x1 = _x        #子弹最初坐标
            self.zidan_list_x1 = []
            self.a = -1                 #控制索引

        def show(self, _x, _y):                             #打印射手
            self.screen.blit(self.image, (self.x, self.y))


                        # self.zidan_list_x[i] += self.zidan_speedx


    class xiangrikui(object):
        def __init__(self, _screen, _x, _y):
            self.image = pygame.image.load("images//向日葵.png")
            self.x = _x
            self.list_x = []
            self.y = _y
            self.list_y = []
            self.now_x = random.randint(100, 500)
            self.now_y = random.randint(250, 550)
            self.a = -1
            self.rect = self.image.get_rect()
            self.width = self.rect.width
            self.height = self.rect.height
            self.time = 700
            self.sunshinex = 100
            self.sunshiney = 100
            self.screen = _screen
            self.taiyang = pygame.image.load("images//小太阳.png")

        def show(self, _x, _y):                             #打印向日葵
            self.screen.blit(self.image, (self.x, self.y))

        def fangyangguang(self):                            #向日葵放阳光
            self.screen.blit(self.taiyang, (self.now_x, self.now_y))


    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    background1 = pygame.image.load("images//u=1844012553,3000876172&fm=27&gp=0.jpg")    #导入花园背景
    background1 = pygame.transform.scale(background1, (1060, 629))
    yangguang = pygame.image.load("images//太阳.png")                           #导入阳光
    xiaotaiyang = pygame.image.load("images//小太阳.png")
    bianlitie = pygame.image.load("images//贴纸.png")
    bianlitie = pygame.transform.scale(bianlitie, (80, 38))
    xuanzewandou = pygame.image.load("images//选择豌豆.jpg")                     #导入选择卡
    wandouqushile = pygame.image.load("images//豌豆去世了.jpg")
    xuanzewandou = pygame.transform.scale(xuanzewandou, (75, 95))
    wandouqushile = pygame.transform.scale(wandouqushile, (75, 95))
    xuanzexiangrikui = pygame.image.load("images//选择向日葵.jpg")
    xiangrikuiqushile = pygame.image.load("images//向日葵去世了.jpg")
    xiangrikuiqushile = pygame.transform.scale(xiangrikuiqushile, (75, 95))
    xuanzexiangrikui = pygame.transform.scale(xuanzexiangrikui, (75, 95))
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)

    time = 50
    shoot = 0
    yangguangliang = 0
    diren = []
    zhiwu = []
    taix = []
    taiy = []
    for i in range(20):                                                 #决定下放的阳光的位置
        taiyangx = random.randint(100, 700)
        taiyangy = random.randint(0, 20)
        taix.append(taiyangx)
        taiy.append(taiyangy)

    stopy = random.randint(150, 500)    #用于确定下放阳光最后的位置
    dropcount = 700     #用于下放阳光倒计时
    j = 0        #用于下放阳光
    k = 700       #用于向日葵长阳光计时
    flag = 0    #击中数
    moving = 0      #鼠标事件
    score = 0       #分数→通关
    jiangshi1A = jiangshi1(screen, 1000, 390)
    wandousheshouA = wandousheshou(screen, 100, 100)
    xiangrikuiA = xiangrikui(screen, 100, 100)
    a = 0

    for i in range(20):
        shix = random.randrange(1000, 2000, 10)
        shiy = random.randrange(100, 550, 90)
        jiangshi1A.list_x.append(shix)
        jiangshi1A.list_y.append(shiy)

    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(background1, (0, 0))  # 打印背景
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if moving == 102:                   #种向日葵
                    xiangrikuiA.list_x.append(mouse_x - 90)
                    xiangrikuiA.list_y.append(mouse_y - 90)
                    moving = 0
                    put = 1
                    yangguangliang -= 50
                if moving == 103:                   #种豌豆射手
                    wandousheshouA.list_x.append(mouse_x - 90)
                    wandousheshouA.list_y.append(mouse_y - 90)
                    wandousheshouA.zidan_list_x.append(mouse_x + 187/2 - 17 - 90)
                    wandousheshouA.zidan_list_y.append(mouse_y + 187/2 - 17 - 90)
                    wandousheshouA.zidan_list_time.append(50)
                    shoot = 1
                    moving = 0
                    yangguangliang -= 100
                if moving == 0 and (160 <= mouse_x <= 160 + 75 and 4 <= mouse_y <= 4 + 95) or \
                        (83 <= mouse_x <= 83 + 75 and 4 <= mouse_y <= 4 + 95):
                        if 160 <= mouse_x <= 160 + 75 and 4 <= mouse_y <= 4 + 95 and yangguangliang >= 50:
                            moving = 2
                        if 83 <= mouse_x <= 83 + 75 and 4 <= mouse_y <= 4 + 95 and yangguangliang >= 100:
                            moving = 3
                if taix[j] <= mouse_x <= taix[j] + 24 and taiy[j] <= mouse_y <= taiy[j] + 24:
                    taiy[j] = -1000
                    j += 1
                    yangguangliang += 25
                    dropcount = 700
                if xiangrikuiA.sunshinex != 0:
                    if xiangrikuiA.now_x <= mouse_x <= xiangrikuiA.now_x + 24 and \
                            xiangrikuiA.now_y <= mouse_y <= xiangrikuiA.now_y + 24:
                        k = 700
                        xiangrikuiA.now_y = random.randint(250, 500)
                        yangguangliang += 25
                else:
                    pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        count_yangguang = font.render(str(yangguangliang), True, [0, 0, 0])

        plantChoose1 = pygame.draw.rect(screen, [139, 69, 0], (0, 0, 380, 100))         #↓打印选择卡↓
        sunChoose = pygame.draw.rect(screen, [205, 102, 0], (0, 0, 80, 100), 4)
        plantChoose = pygame.draw.rect(screen, [205, 102, 0], (80, 0, 300, 100), 4)

        if yangguangliang < 50:
            screen.blit(wandouqushile, (83, 4))
            screen.blit(xiangrikuiqushile, (160, 4))
        if 50 <= yangguangliang < 100:
            screen.blit(xuanzexiangrikui, (160, 4))
            screen.blit(wandouqushile, (83, 4))
        if yangguangliang >= 100:
            screen.blit(xuanzexiangrikui, (160, 4))
            screen.blit(xuanzewandou, (83, 4))

        if moving == 2:
            screen.blit(xiangrikuiqushile, (160, 4))
            xiangrikuiA.show(mouse_x - 50, mouse_y - 50)
            moving = 102
        if moving == 3:
            screen.blit(wandouqushile, (83, 4))
            wandousheshouA.show(mouse_x - 50, mouse_y - 50)
            moving = 103

        if dropcount:                                           #↓用于下放阳光↓
            dropcount -= 1
        else:
            for i in range(5):
                screen.blit(xiaotaiyang, (taix[j], taiy[j]))
                if taiy[j] <= stopy:
                    taiy[j] += 0.1                               #↑用于下放阳光↑

        xuanwandou = pygame.draw.rect(screen, [255, 255, 255], (90, 75, 60, 20))
        xuanxiangrikui = pygame.draw.rect(screen, [255, 255, 255], (167, 76, 60, 20))
        test_xiangrikui = font.render("50", True, [0, 0, 0])
        test_wandou = font.render("100", True, [0, 0, 0])
        screen.blit(test_wandou, (95, 73))
        screen.blit(test_xiangrikui, (180, 73))
        screen.blit(xiaotaiyang, (128, 73))
        screen.blit(xiaotaiyang, (200, 75))
        screen.blit(yangguang, (8, 8))
        screen.blit(bianlitie, (0, 65))
        screen.blit(count_yangguang, (30, 75))                                      #↑打印选择卡↑

        for i in range(len(xiangrikuiA.list_x)):
            screen.blit(xiangrikuiA.image, (xiangrikuiA.list_x[i], xiangrikuiA.list_y[i]))

        for i in range(len(wandousheshouA.list_x)):
            screen.blit(wandousheshouA.image, (wandousheshouA.list_x[i], wandousheshouA.list_y[i]))

        if len(xiangrikuiA.list_x) > 0 and put == 1:
            if k:
                k -= 1
            else:
                xiangrikuiA.fangyangguang()

        if len(wandousheshouA.zidan_list_time) > 0 and shoot == 1:
            if time:
                time -= 1
            else:
                if wandousheshouA.zidan_list_x[i] > 800:
                    wandousheshouA.zidan_list_x[i] = wandousheshouA.list_x[i]
                wandousheshouA.zidan_list_x[i] += wandousheshouA.zidan_speedx + 10
                screen.blit(wandousheshouA.zidan, (wandousheshouA.zidan_list_x[i] + 10, wandousheshouA.zidan_list_y[i] - 10))

                wandousheshouA.zidan_list_time[i] = 50


        if flag < jiangshi1A.blood:                                                 #打怪兽
            jiangshi1A.show1()
            jiangshi1A.move()
        if flag >= jiangshi1A.blood:
            jiangshi1A.show2()
            if flag >= jiangshi1A.blood + 1:
                jiangshi1A.back()
                score += 1
        pygame.display.update()
