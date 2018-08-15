import pygame
import time
import random

pygame.init()
pygame.mixer.init()
back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()

screen = pygame.display.set_mode((495,800))

font=pygame.font.Font("C:\windows\Fonts\SimHei.ttf",36)#文字

fengmian = pygame.image.load(r"images\fengmian.jpg")#封面
fengmian = pygame.transform.scale(fengmian,(495,800))

button_start = pygame.image.load(r"images\button_start.png")#开始按钮
x=0
y=0
x1=0
y1=0
start_num = 0

button_pause = pygame.image.load(r"images\button_stop.png")#暂停按钮
button_continue = pygame.image.load(r"images\button_pause.png")#游戏继续按钮

bg = pygame.image.load(r"images\background.png")#原样显示
bg = pygame.transform.scale(bg,(495,800))
#放入飞机
hero = pygame.image.load("images\hero.gif")
h_rect = hero.get_rect()#得到图片的长宽
h_width = h_rect.width
h_height = h_rect.height
hx = 100
hy = 100
flag = True
#子弹
bullet = pygame.image.load(r"images\bullet.png")
bx=[]#子弹位置
by=[]
b_speed=3#速度
b_v=10#频率
time1 = b_v

e_bullet = pygame.image.load("ball.png")#敌人子弹
e_bx=[]#子弹位置
e_by=[]
e_b_speed=1#速度
e_b_v=10#频率
e_time = e_b_v

#添加敌机
enemy = pygame.image.load(r"images\enemy0.png")
ex=[]
ey=[]
e_rect = enemy.get_rect()#得到图片的长宽
e_width = e_rect.width
e_height = e_rect.height

for i in range(3):
    ex.append(random.randint(0,495))
    ey.append(random.randint(-100,0))

hit_x = 0
hit_y = 0
down_1 = pygame.image.load(r"images\enemy0_down1.png")
down_2 = pygame.image.load(r"images\enemy0_down2.png")
down_3 = pygame.image.load(r"images\enemy0_down3.png")
down_4 = pygame.image.load(r"images\enemy0_down4.png")

mark = True
hit_num = 0
start_time = 0
end_time = 0
another_flag = True

prop = pygame.image.load(r"images\prop_type_1.png")
p_rect = prop.get_rect()#得到图片的长宽
p_width = p_rect.width
p_height = p_rect.height
px = random.randint(0,495)#补血
py = random.randint(-100,0)

score = 0
customs_num = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:

    pressed_array = pygame.mouse.get_pressed()
    for index in range(len(pressed_array)):
        if pressed_array[index]:
            if index == 0 and x >= 350 and x <= 350 + 72 and y >= 600 and y <= 600 + 72 or \
                    index == 0 and x1 >= 350 and x1 <= 350 + 72 and y1 >= 600 and y1 <= 600 + 72:#左击键盘
                start_num = 1
            if index == 2 and hx>= 400 and hx<= 400+72 and hy>= 700 and hy<=700+72:#右击键盘
                start_num = 2

    if start_num == 1:
        screen.blit(bg, (0, 0))#背景
        screen.blit(button_pause, (400,700))#暂停按钮
        f1_1 = font.render("得分： "+str(score), True, (0, 0, 0))
        screen.blit(f1_1, (50, 90))

        if flag == True:
            hx,hy = pygame.mouse.get_pos() #鼠标移动飞机

        if time1:#根据自己设置的时间变量，设置当前子弹的添加频率
            time1 -= 1
        else:
            bx.append(hx-h_width/15)
            by.append(hy-h_height/2)
            time1= b_v#重置 添加频率

        screen.blit(hero,(hx-h_width/2,hy-h_height/2))#飞机,使飞机与鼠标位置有一点差别

        for i in range(len(bx)):#子弹绘制
            screen.blit(bullet, (bx[i], by[i]))
            by[i] -= b_speed#子弹移动

        for i in range(len(by)):#敌机消失
            for j in range(3):#三辆机
                if bx[i] >= ex[j] and bx[i] <= ex[j]+e_width and by[i] == ey[j]:
                    another_flag = False
                    start_time = time.time()
                    hit_x = ex[j]
                    hit_y = ey[j]
                    score += 1#得分
                    ex[j] = random.randint(0, 495)
                    ey[j] = random.randint(-100, 0)

                if ey[j] > 800:#敌机下落到底部，就回到屏幕上方
                    ex[j] = random.randint(0, 495)
                    ey[j] = random.randint(-100, 0)

        if score > 3:
            customs_num = 2

        if another_flag == False:
            end_time = time.time()
            if str(end_time -start_time)[0:3] == "0.2":#敌机爆炸过程
                screen.blit(down_1,(hit_x,hit_y))
            if str(end_time - start_time)[0:3] == "0.4":
                screen.blit(down_2, (hit_x, hit_y))
            if str(end_time - start_time)[0:3] == "0.6":
                screen.blit(down_3, (hit_x, hit_y))
            if str(end_time - start_time)[0:3] == "0.8":
                screen.blit(down_4, (hit_x, hit_y))

        for i in range(3):# 敌机发射子弹
            e_bx.append(ex[i] + e_width / 3)
            e_by.append(ey[i])
            screen.blit(e_bullet, (e_bx[i], e_by[i]))
            e_by[i] += 7  # 敌人子弹移动
            if e_by[i] > 800:
                e_bx[i] = ex[i]+ e_width / 3
                e_by[i] = ey[i]
                screen.blit(e_bullet, (e_bx[i], e_by[i]))
                e_by[i] += 7  # 敌人子弹移动

        for i in range(3):#我机被击中
            if e_bx[i] >= hx-h_width/2 and e_bx[i] <= hx + h_width/2 and hy+h_height>e_by[i] > hy:
                hit_num += 1
                mark = False
                e_by[i] = -100


        screen.blit(prop,(px,py))#补血
        py += 0.05
        if px >= hx-h_width/2 and px <= hx + h_width/2 and hy-h_height/2 <= py+p_height and hit_num >=2 and hit_num <= 3:
            hit_num -= 1
            px = random.randint(0, 495)
            py = random.randint(-200,-100)
        if px >= hx-h_width/2 and px <= hx + h_width/2 and hy-h_height/2 <= py+p_height and hit_num == 1:
            hit_num -= 1
            px = random.randint(0, 495)
            py = random.randint(-200,-100)

        for i in range(len(by)):#我机血量
            if mark == True:
                pygame.draw.line(screen,(255,0,0),(hx,hy+50),(hx+60,hy+50),3)
            else:
                if hit_num == 0:
                    pygame.draw.line(screen, (255, 0, 0), (hx, hy + 50), (hx + 60, hy + 50), 3)
                if hit_num == 1:
                    pygame.draw.line(screen, (255, 0, 0), (hx,hy+50),(hx+40,hy+50), 3)
                    pygame.draw.line(screen, (102,139,139), (hx+40,hy+50),( hx + 60,hy+50), 3)

                if hit_num == 2:
                    pygame.draw.line(screen, (255, 0, 0), (hx,hy+50),(hx+20,hy+50), 3)
                    pygame.draw.line(screen, (102,139,139), (hx+20,hy+50),( hx + 60,hy+50), 3)
                if hit_num == 3:
                    pygame.draw.line(screen, (102,139,139), (hx,hy+50),(hx + 60,hy+50), 3)
                if hit_num == 4:
                    hy = -500
                    flag = False
                    f_text = font.render("游戏结束！", True, (0, 0, 0))
                    screen.blit(f_text, (180, 350))

        for i in range(3):#敌机下落
            screen.blit(enemy, (ex[i], ey[i]))
            ey[i] += 1

        if customs_num == 1:
            f1 = font.render("关卡一 ", True, (0, 0, 0))
            screen.blit(f1, (50, 50))
        if customs_num == 2:
            f2 = font.render("关卡二 ", True, (0, 0, 0))
            screen.blit(f2, (50, 50))

    if start_num == 2:
        screen.blit(fengmian, (0, 0))
        screen.blit(button_continue, (350, 600))
        font_text = font.render("游戏暂停中",True,(0,0,0))
        font_text1 = font.render("点击右下角按钮继续游戏",True,(0,0,0))
        screen.blit(font_text,(150,500))
        screen.blit(font_text1, (50, 540))
        x1,y1 = pygame.mouse.get_pos()
        # print(x1)
        # print(y1)

    if start_num == 0:
        x,y = pygame.mouse.get_pos()
        screen.blit(fengmian, (0,0))
        screen.blit(button_start, (350,600))



    pygame.display.update()