import pygame
from math import *
import random

pygame.init()
screen=pygame.display.set_mode((800,700))
bg = pygame.image.load("bg.jpg")
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)

missile=pygame.image.load('circle.png').convert_alpha()
x1,y1=100,600
x2,y2 = 100, 600
x3,y3 = 100,600
x4,y4 = 100,600#导弹的初始发射位置
velocity=800            #导弹速度
time=1/100             #每个时间片的长度
clock=pygame.time.Clock()
old_angle=0
old_angle2 = 0
old_angle3 = 0
old_angle4 = 0
score = 0

# 砖块
brick = pygame.image.load("brickcaise.png")
brick = pygame.transform.scale(brick, (96, 96))
brick_rect = brick.get_rect()
brick_y = []
brick_x = []
# 蛇头
snakehead = pygame.image.load("circlehead.png")
a = 240
b = 350
snakehead_rect = snakehead.get_rect()
# 蛇身
snakebody = pygame.image.load("circle.png")
snakebody = pygame.transform.scale(snakebody, (48, 40))
snakebody_rect = snakebody.get_rect()
# 火花
fire = pygame.image.load("fire.png")

count2 = 0
count3 = 0
count4 = 0
for i in range(3):
        brick_x.append(random.randint(0, 15) * 48)
        brick_y.append(random.randint(-100, -48))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.blit(bg, (0, 0))
    x, y = pygame.mouse.get_pos()
    score_letter = font.render("score:" + str(score), True, (50, 255, 255))
    screen.blit(score_letter, (660, 50))

    clock.tick(60)          #获取鼠标位置，鼠标就是需要打击的目标
    distance=sqrt(pow(x1-x,2)+pow(y1-y,2))      #两点距离公式
    section=velocity*time               #每个时间片需要移动的距离
    sina=(y1-y)/distance
    cosa=(x-x1)/distance
    angle=atan2(y-y1,x-x1)              #两点线段的弧度值
    x1,y1=(x1+section*cosa, y1-section*sina)
    d_angle = degrees(angle)        #弧度转角度
    screen.blit(missile, (x1-missile.get_width(), y1-missile.get_height()/2))
    dis_angle = d_angle-old_angle          #dis_angle就是到下一个位置需要改变的角度
    old_angle = d_angle                    #更新初始角度

    # 砖块动态
    for i in range(len(brick_y)):
        brick_y[i] += 4
        screen.blit(brick, (brick_x[i], brick_y[i]))
        if brick_y[i] > 700:
            brick_y[i] = random.randint(-100, -96)
            brick_x[i] = random.randint(0, 5) * 96
            score -= 1

    if count2 >= 1000:
        # screen.blit(snakebody, (x1-missile.get_width(), y1-missile.get_height()/2+snakebody_rect.height))
        distance2 = sqrt(pow(x2 - x, 2) + pow(y2 - y, 2))  # 两点距离公式
        section2 = velocity * time * 1.92  # 每个时间片需要移动的距离
        sina2 = (y2 - y) / distance2
        cosa2 = (x - x2) / distance2
        angle2 = atan2(y - y2, x - x2)  # 两点线段的弧度值
        x2, y2 = (x2 + section2 * cosa2, y2 - section2 * sina2)
        d_angle2 = degrees(angle2)  # 弧度转角度
        # screen.blit(missile, (x1 - missile.get_width(), y1 - missile.get_height() / 2))
        dis_angle2 = d_angle2 - old_angle2  # dis_angle就是到下一个位置需要改变的角度
        old_angle2 = d_angle2
        count2 = 0
        # 鼠标定位蛇身
    count2 += 500

    if count3 >= 1000:
        # screen.blit(snakebody, (x1-missile.get_width(), y1-missile.get_height()/2+snakebody_rect.height))
        distance3 = sqrt(pow(x3 - x, 2) + pow(y3 - y, 2))  # 两点距离公式
        section3 = velocity * time * 1.82  # 每个时间片需要移动的距离
        sina3 = (y3 - y) / distance3
        cosa3 = (x - x3) / distance3
        angle3 = atan2(y - y3, x - x3)  # 两点线段的弧度值
        x3, y3 = (x3 + section3 * cosa3, y3 - section3 * sina3)
        d_angle3 = degrees(angle3)  # 弧度转角度
        # screen.blit(missile, (x1 - missile.get_width(), y1 - missile.get_height() / 2))
        dis_angle3 = d_angle3 - old_angle3  # dis_angle就是到下一个位置需要改变的角度
        old_angle3 = d_angle3
        count3 = 0
        # 鼠标定位蛇身
    count3 += 500

    if count4 >= 1000:
        # screen.blit(snakebody, (x1-missile.get_width(), y1-missile.get_height()/2+snakebody_rect.height))
        distance4 = sqrt(pow(x4 - x, 2) + pow(y4 - y, 2))  # 两点距离公式
        section4 = velocity * time * 1.6  # 每个时间片需要移动的距离
        sina4 = (y4 - y) / distance4
        cosa4 = (x - x4) / distance4
        angle4 = atan2(y - y4, x - x4)  # 两点线段的弧度值
        x4, y4 = (x4 + section4 * cosa4, y4 - section4 * sina4)
        d_angle4 = degrees(angle4)  # 弧度转角度
        dis_angle4 = d_angle4 - old_angle4  # dis_angle就是到下一个位置需要改变的角度
        old_angle4 = d_angle4
        count4 = 0
        # 鼠标定位蛇身
    count4 += 500

    screen.blit(snakehead, (x1 - missile.get_width(), y1 - missile.get_height() / 2))
    screen.blit(snakebody, (x2 - missile.get_width(), y2 - missile.get_height() / 2 + snakebody_rect.height))
    screen.blit(snakebody, (x3 - missile.get_width(), y3 - missile.get_height() / 2 + snakebody_rect.height*2))
    screen.blit(snakebody, (x4 - missile.get_width(), y4 - missile.get_height() / 2 + snakebody_rect.height*3))
    # 碰撞砖块检测
    for i in range(len(brick_x)):
        if (x1 + missile.get_width())>brick_x[i] and\
                (x1 - missile.get_width())<(brick_x[i]+brick_rect.width) and\
                (y1 - missile.get_height() / 2)<(brick_y[i]+brick_rect.height):
            for j in range(100):
                screen.blit(fire, (brick_x[i]+brick_rect.width/4, brick_y[i]))
            brick_y[i] = random.randint(-100, -96)
            brick_x[i] = random.randint(0, 480-96)
            score += 1

    pygame.display.update()