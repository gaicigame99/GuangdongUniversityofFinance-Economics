import pygame
import math
import random
def begin():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    bg = pygame.image.load(r"images\bg4.jpg")
    stuart = pygame.image.load(r"images\Stuart.png")
    kevin = pygame.image.load(r"images\Kevin.png")
    music = pygame.image.load(r"images\iTunes.png")
    music = pygame.transform.scale(music,(60,60),)
    gear = pygame.image.load(r"images\gear.png")
    gear = pygame.transform.scale(gear,(60,60))
    start = pygame.image.load(r"images\start4.png")
    start = pygame.transform.scale(start,(60,60),)
    home = pygame.image.load(r"images\home.png")
    home = pygame.transform.scale(home,(60,60))
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)
    jiemian = pygame.image.load(r"images\jiemian.jpg")
    jiemian = pygame.transform.scale(jiemian,(800,600))
    WHITE = (255,255,255)
    angle,score,flag,direc = 10, 0, 0, 0
    e_x, e_y = 400, 200
    x_a,y_a = [], []
    length,n,r,p,m= 50,0,50,0,""
    def collection(a_x,a_y,a_w,a_h,b_x,b_y):
        if a_w + a_x > b_x and a_x <  b_x and a_y <=  b_y  and a_h + a_y > b_y :
            return True
        else:
            return False

    class goldblock(object):
        def __init__(self,_screen):
            self.image = pygame.image.load(r"images\goldblock.png")
            self.screen = _screen
            self.x = random.randint(50,600)
            self.y = random.randint(300,400)
            self.rect = self.image.get_rect()
            self.w = self.rect.width
            self.h = self.rect.height
        def show(self):
            screen.blit(self.image,(self.x,self.y))
    class treasure(object):
        def __init__(self,_screen):
            self.image = pygame.image.load(r"images\treasure.png")
            self.screen = _screen
            self.x = random.randint(50,600)
            self.y = random.randint(350,400)
            self.rect = self.image.get_rect()
            self.w = self.rect.width
            self.h = self.rect.height
        def show(self):
            screen.blit(self.image,(self.x,self.y))
    class diamond(object):
        def __init__(self,_screen):
            self.image = pygame.image.load(r"images\diamond_gt.png")
            self.screen = _screen
            self.x = random.randint(50,700)
            self.y = random.randint(400,550)
            self.rect = self.image.get_rect()
            self.w = self.rect.width
            self.h = self.rect.height
            self.flag = 0
            self.col_flag = 1
        def show(self):
            screen.blit(self.image,(self.x,self.y))

    #生成宝藏对象
    dict_dia={}
    dict_gold={}
    dict_treasure={}
    for i in range(3):
        dict_dia["dia"+str(i)]=diamond(screen)
    for i in range(3):
        dict_gold["gold"+str(i)]=goldblock(screen)
    for i in range(3):
        dict_treasure["trea"+str(i)]=treasure(screen)
    def loading():
        screen.blit(bg, (0, 0))
        screen.blit(stuart, (400, 100))
        screen.blit(music,(740,0))
        screen.blit(home, (670, 0))
        pygame.draw.circle(screen, (255,255,255), (400, 200), 15, 15)
        for i in range(3):
            dict_treasure["trea" + str(i)].show()
            dict_gold["gold" + str(i)].show()
            dict_dia["dia" + str(i)].show()
    # def loading_j():
    #     screen.blit(jiemian, (0, 0))
    def playgame(angle,score,flag,direc,e_x,e_y,n,m,r,p):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            if pygame.mouse.get_focused():
                #初始化图标
                loading()
                p_sc = font.render("score:" + str(score), True, (255, 255, 255))
                screen.blit(p_sc, (1, 1))
                mouse_x, mouse_y = pygame.mouse.get_pos()
                a, b, c = pygame.mouse.get_pressed()
                # 判断是否伸长绳子
                if flag== 0 and 0<mouse_x<800 and 0< mouse_y<600 and a == 1:
                    flag = 1

                #绳子伸长抓宝藏
                if flag == 1:
                    x_a.append(400 + r * math.cos(angle*math.pi/180))
                    y_a.append(200 + r * math.sin(angle*math.pi/180))
                    r += 1
                    pygame.draw.line(screen, WHITE, (e_x, e_y), (x_a[p], y_a[p]), 5)
                    for j in range(3):
                        if collection(dict_treasure["trea"+str(j)].x,dict_treasure["trea"+str(j)].y,\
                                             dict_treasure["trea"+str(j)].w,dict_treasure["trea"+str(j)].h, \
                                             x_a[p], y_a[p]): #如果有一个宝藏检测到碰撞，则其他所有的碰撞停止检测
                            m = "trea"+str(j)
                            n=1
                            flag = 2
                        if  collection(dict_gold["gold"+str(j)].x,dict_gold["gold"+str(j)].y, \
                                             dict_gold["gold" + str(j)].w,dict_gold["gold"+str(j)].h, \
                                             x_a[p], y_a[p]):
                            m= "gold"+str(j)
                            n=2
                            flag=2
                        if collection(dict_dia["dia"+str(j)].x,dict_dia["dia"+str(j)].y, \
                                             dict_dia["dia" + str(j)].w,dict_dia["dia"+str(j)].h, \
                                             x_a[p], y_a[p]):
                            m="dia"+str(j)
                            n=3
                            flag=2
                    p += 1
                    if r == 400:
                        flag = 3
                        r = 0
                        n = 0
                #绳子没有抓到东西，返回
                if flag ==3:
                    l = len(x_a)
                    pygame.draw.line(screen, WHITE, (e_x, e_y), (x_a[l - 1], y_a[l - 1]), 5)
                    x_a.pop()
                    y_a.pop()
                    if len(x_a) == 0:
                        # l = 0
                        flag = 0
                #绳子缩回拉宝藏，要和伸长分开，不然会伸长推宝藏
                if flag == 2:
                    l=len(x_a)
                    if n == 1:
                        dict_treasure[m].x= x_a[l-1]-dict_treasure[m].w/2
                        dict_treasure[m].y = y_a[l-1]
                        pygame.draw.line(screen, WHITE, (e_x, e_y), (x_a[l-1], y_a[l-1]), 5)
                        l-=1
                        x_a.pop()
                        y_a.pop()

                        if len(x_a) == 0:
                            dict_treasure[m].x = -50
                            dict_treasure[m].y = -50
                            flag = 0
                            l = 0
                            score += 500
                    if n == 2:
                        dict_gold[m].x= x_a[l-1]-dict_gold[m].w/2
                        dict_gold[m].y = y_a[l-1]-10
                        pygame.draw.line(screen, WHITE, (e_x, e_y), (x_a[l - 1], y_a[l - 1]), 5)
                        l-=1
                        x_a.pop()
                        y_a.pop()

                        if len(x_a) == 0:
                            dict_gold[m].x = -50
                            dict_gold[m].y = -50
                            flag = 0
                            l = 0
                            score += 200
                            print(score)
                    if n == 3:
                        dict_dia[m].x= x_a[l-1]-dict_dia[m].w-2
                        dict_dia[m].y = y_a[l-1]
                        pygame.draw.line(screen, WHITE, (e_x, e_y), (x_a[l - 1], y_a[l - 1]), 5)
                        l-=1
                        x_a.pop()
                        y_a.pop()

                        if len(x_a) == 0:
                            dict_dia[m].x = -100
                            dict_dia[m].y = -100
                            flag = 0
                            # l = 0
                            score += 1000
                #绳子没有伸长时的shake
                if flag == 0:
                    screen.blit(stuart, (400, 100))
                    r,b,n,p= 0,0,0,0
                    x = 400 + length * math.cos(angle*math.pi/180)
                    y = 200 + length * math.sin(angle*math.pi/180)
                    if direc == 0:
                        angle += 1
                        if angle >= 170:
                            direc = 1
                    if direc == 1:
                        angle -= 1
                        if angle <= 10:
                            direc = 0
                    pygame.draw.line(screen, WHITE, (e_x, e_y), (x, y), 5)
            pygame.display.update()
    # def jiemian():
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 exit()
    #         loading_j()
    #         pygame.display.update()
    
        
        # jiemian()
    playgame(angle,score,flag,direc,e_x,e_y,n,m,r,p)
