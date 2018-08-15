import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((600,600))
bg = pygame.transform.scale(pygame.image.load("xingkong.jpg"),(600,600))
font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",36)

score = 0

# 食物点
r_x =random.randint(0,600)
r_y = random.randint(0,600)

time1 = 0
time2 = 1

# 初始化蛇位置与速度
ls_x = [2,2,2]
ls_y = [0,0,0]
lx=[220,210,200]
ly=[300,300,300]
s =2

# 存储改变方向的坐标及方向
ji_x = []
ji_y = []
ji_sx = []
ji_sy = []
isfangxiang = False

#检测碰撞
def pengzhuangceshi(x1,x2,y1,y2):
    if -10<x1-x2<10 and -10<y1-y2<10:
        return True
    else:
        return False





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==273 and ls_y[0]!= s :#按键进行方向改变并且不可为反方向
                ls_y[0] = -s
                ls_x[0] = 0
                isfangxiang = True
            if event.key ==274 and ls_y[0]!=-s :
                ls_y[0] = s
                ls_x[0] = 0
                isfangxiang = True
            if event.key == 275 and ls_x[0]!=-s:
                ls_y[0] = 0
                ls_x[0] = s
                isfangxiang = True
            if event.key == 276 and ls_x[0]!=s:
                ls_y[0] = 0
                ls_x[0] = -s
                isfangxiang = True

            if isfangxiang == True:
                ji_x.append(lx[0])
                ji_y.append(ly[0])
                ji_sx.append(ls_x[0])
                ji_sy.append(ls_y[0])
                isfangxiang = False

    #判断蛇身的点坐标是否与改变方向点坐标相同及改变方向
    for i in range(len(lx)):
        for j in range(len(ji_x)):
            if lx[i] ==ji_x[j] and ly[i] == ji_y[j]:
                ls_x[i]=ji_sx[j]
                ls_y[i]=ji_sy[j]

    #去除改变方向点
    for i in range(len(ji_x)):
        if lx[len(lx)-1] ==ji_x[i] and ly[len(lx)-1] == ji_y[i]:
            ji_x.pop(i)
            ji_y.pop(i)
            ji_sx.pop(i)
            ji_sy.pop(i)
            break

    time2 = time.time()
    pygame.draw.circle(screen,(255,255,255),(r_x,r_y),5)
    if time2 - time1>=0.02:
        screen.blit(bg, (0, 0))
        # x+=s_x
        # y+=s_y
        for i in range(len(ls_x)):
            lx[i]+=ls_x[i]
            ly[i]+=ls_y[i]
        for i in range(len(lx)):
            pygame.draw.circle(screen, (255, 255, 255), (lx[i], ly[i]), 5)
        time1 = time.time()
        if pengzhuangceshi(lx[0],r_x,ly[0],r_y):
            r_x = random.randint(0, 600)
            r_y = random.randint(0, 600)
            score+=1
            if ls_x[len(lx)-1] ==s:#根据最后一个点的速度方向增加新的点的速度方向
                lx.append(lx[len(lx)-1]-10)
                ly.append(ly[len(ly)-1])
                ls_x.append(ls_x[len(ls_x)-1])
                ls_y.append(ls_y[len(ls_y) - 1])
            if ls_x[len(lx)-1] == -s:

                lx.append(lx[len(lx)-1]+10)
                ly.append(ly[len(ly)-1])
                ls_x.append(ls_x[len(ls_x)-1])
                ls_y.append(ls_y[len(ls_y) - 1])
            if ls_y[len(ly)-1] ==s:

                lx.append(lx[len(lx)-1])
                ly.append(ly[len(ly)-1]-10)
                ls_x.append(ls_x[len(ls_x)-1])
                ls_y.append(ls_y[len(ls_y) - 1])
            if ls_y[len(ly)-1]==-s:

                lx.append(lx[len(lx)-1])
                ly.append(ly[len(ly)-1]+10)
                ls_x.append(ls_x[len(ls_x)-1])
                ls_y.append(ls_y[len(ls_y) - 1])
    #游戏结束判断
    if 600<lx[0] or lx[0]<0 or 600<ly[0] or ly[0]<0:
        print("over")
    for i in range(len(lx)):
        if i!=0 and i!=1:#第一个点与第二个点不会发现碰撞所以无需判断
            if pengzhuangceshi(lx[0],lx[i],ly[0],ly[i]):
                print("over2")

    screen.blit(font.render(str(score),True,(255,255,255)),(0,0))
    pygame.display.update()