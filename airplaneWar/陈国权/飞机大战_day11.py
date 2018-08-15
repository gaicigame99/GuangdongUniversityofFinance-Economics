import pygame
import random
import time

pygame.init()

screen=pygame.display.set_mode((495,800))
font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",25)
font1=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",35)
bg=pygame.image.load(r"images\background.png")
bg=pygame.transform.scale(bg,(495,800))


#开始界面
game_name=pygame.image.load("images\\name.png")
start1=pygame.image.load("images\game_loading1.png")
start2=pygame.image.load("images\game_loading2.png")
start3=pygame.image.load("images\game_loading3.png")
start4=pygame.image.load("images\game_loading4.png")
start_but=pygame.image.load("images\game_resume_nor.png")
start_but1=pygame.image.load("images\game_resume_pressed.png")
exit_but=pygame.image.load("images\exit.png")
start_judge=0
start_x=0

#游戏暂停
pause_0=pygame.image.load("images\game_pause_nor.png")
pause_1=pygame.image.load("images\game_pause_pressed.png")
pause_resume=pygame.image.load("images\\resume_game.png")
pause_judge=0#游戏暂停判断变量

hero=pygame.image.load("images\hero.gif")
h_rect=hero.get_rect()
h_width=h_rect.width
h_height=h_rect.height

#分数、生命
s_num="0"
score=font.render("Score:",True,(255,255,255))
life=pygame.image.load("images\prop_type_0.png")
l_num=3


#子弹
bullet=pygame.image.load(r"images\bullet2.png")
bx=[]
by=[]
b_speed=5
b_v=15
b_rect=bullet.get_rect()


#enemy0
enemy_0=pygame.image.load("images\enemy0.png")
bomm0_1=pygame.image.load("images\enemy0_down1.png")
bomm0_2=pygame.image.load("images\enemy0_down2.png")
bomm0_3=pygame.image.load("images\enemy0_down3.png")
bomm0_4=pygame.image.load("images\enemy0_down4.png")
e_0x=[]
e_0y=[]
for i in range(3):
    x=random.randint(10,495-39)
    y=random.randint(-200,-51)
    e_0x.append(x)
    e_0y.append(y)
shoot0=0
t0=[]
t0_x=[]
t0_y=[]
condition=enemy_0


#enemy1
enemy_1=pygame.image.load("images\enemy1.png")
bomm1_1=pygame.image.load("images\enemy1_down1.png")
bomm1_2=pygame.image.load("images\enemy1_down2.png")
bomm1_3=pygame.image.load("images\enemy1_down3.png")
bomm1_4=pygame.image.load("images\enemy1_down4.png")
e_1x=[]
e_1y=[]
hit_num=[]
t1=[]
t1_x=[]
t1_y=[]

for i in range(2):
    x=random.randint(10,495-39)
    y=random.randint(-152,-51)
    e_1x.append(x)
    e_1y.append(y)
    hit_num.append(0)
shoot1=0
hit_point=0
#hit_num击中次数，enemy1需击中10次才可消灭


mark=b_v
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(bg,(0,0))
    #进入开始界面
    if start_judge==0:
        screen.blit(game_name, (30, 180))
        if start_x<100-48:
            screen.blit(start1,(start_x,400))
            start_x+=1
        elif start_x<200:
            screen.blit(start2,(start_x,400))
            start_x+=1
        elif start_x <220:
            screen.blit(start3,(start_x,400))
            start_x+=1
        elif start_x<495:
            screen.blit(start4,(start_x,400))
            start_x+=1
        elif start_x>=495:
            screen.blit(game_name,(30,180))
            screen.blit(start_but,(150,300))
            ts_start= font1.render("START", True, (255, 255, 255))
            screen.blit(ts_start,(200,300))
            screen.blit(exit_but,(150,400))
            ts_exit= font1.render("EXIT GAME", True, (255, 255, 255))
            screen.blit(ts_exit,(200,400))
        a,b,c=pygame.mouse.get_pressed()
        mx,my=pygame.mouse.get_pos()
        if mx>150 and mx<150+38 and my>300 and my<300+41 and a:
            screen.blit(start_but1,(250,300))
            start_judge=1
        if mx>150 and mx<150+38 and my>400 and my<400+41 and a:
            exit()
    #进入游戏界面
    if start_judge==1:
        # 游戏中.......
        if pause_judge == 0:
            hx,hy=pygame.mouse.get_pos()
            if mark:
                mark-=1
                print(bx)
            else:
                bx.append(hx-b_rect.width/2)
                by.append(hy-h_height/2-b_rect.height)
                mark=b_v
            screen.blit(bg, (0, 0))
            screen.blit(pause_0, (445,750))
            screen.blit(hero,(hx-h_width/2,hy-h_height/2))
            #删除炸弹多余列表元素
            if len(bx)>20:
                del bx[0:11]
                del by[0:11]
            for i in range(len(bx)):
                screen.blit(bullet,(bx[i],by[i]))
                by[i]-=b_speed

            #enemy0碰撞
            if shoot0 == 0:
                for i in range(len(e_0x)):
                    screen.blit(condition, (e_0x[i], e_0y[i]))
                    e_0y[i] += 2
            if shoot0 == 1:
                shoot0 = 0
                pass
            for i in range(len(bx)):
                for j in range(len(e_0x)):
                    if bx[i]>e_0x[j] and bx[i]<e_0x[j]+51 and by[i]>e_0y[j] and by[i]<e_0y[j]+39:
                        t0.append(time.time())
                        t0_x.append(e_0x[j])
                        t0_y.append(e_0y[j])
                        shoot0 = 1
                        bx[i] -= 800
                        by[i] -= 800
                        s_num = str(int(s_num) + 1)
                        e_0x.pop(j)
                        e_0y.pop(j)
                        e_0x.append(random.randint(10, 495 - 39))
                        e_0y.append(random.randint(-200, -51))
                        break
            if t0:
                for i in range(len(t0)):
                    n_t=time.time()
                    if 0<n_t-t0[i]<0.2:
                        screen.blit(bomm0_1,(t0_x[i],t0_y[i]))
                    if 0.2<n_t-t0[i]<0.5:
                        screen.blit(bomm0_2,(t0_x[i],t0_y[i]))
                    if 0.5<n_t-t0[i]<0.8:
                        screen.blit(bomm0_3,(t0_x[i],t0_y[i]))
                    if 0.8<n_t-t0[i]<1.2:
                        screen.blit(bomm0_4,(t0_x[i],t0_y[i]))


            #enemy1碰撞
            if shoot1 == 0:
                for i in range(len(e_1x)):
                    screen.blit(enemy_1, (e_1x[i], e_1y[i]))
                    e_1y[i] += 1
            if shoot1 == 1 :
                shoot1 = 0
                pass
            for i in range(len(bx)):
                for j in range(len(e_1x)):
                    if bx[i] > e_1x[j] and bx[i] < e_1x[j] + 51 and by[i] > e_1y[j] and by[i] < e_1y[j] + 39:
                        hit_point=1
                        hit_num[j]+=1
                        by[i]-=800
                        if hit_num[j]==5:
                            t1.append(time.time())
                            t1_x.append(e_1x[j])
                            t1_y.append(e_1y[j])
                            screen.blit(bomm1_1, (e_1x[j], e_1y[j]))
                            screen.blit(bomm1_2, (e_1x[j], e_1y[j]))
                            screen.blit(bomm1_3, (e_1x[j], e_1y[j]))
                            screen.blit(bomm1_4, (e_1x[j], e_1y[j]))
                            shoot1 = 1
                            s_num = str(int(s_num) + 2)
                            hit_num[j]=0
                            temp1=j
                            e_1x.pop(j)
                            e_1y.pop(j)
                            e_1x.append(random.randint(10, 495 - 39))
                            e_1y.append(random.randint(-152, -51))
            if t1:
                for i in range(len(t1)):
                    n_t = time.time()
                    if 0 < n_t - t1[i] < 0.2:
                        screen.blit(bomm1_1, (t1_x[i], t1_y[i]))
                    if 0.2 < n_t - t1[i] < 0.5:
                        screen.blit(bomm1_2, (t1_x[i], t1_y[i]))
                    if 0.5 < n_t - t1[i] < 0.8:
                        screen.blit(bomm1_3, (t1_x[i], t1_y[i]))
                    if 0.8 < n_t - t1[i] < 1.2:
                        screen.blit(bomm1_4, (t1_x[i], t1_y[i]))

            #暂停按钮判断
            a, b, c = pygame.mouse.get_pressed()
            if hx>445 and hx<445+42 and hy>750 and hy<750+45 and a:
                screen.blit(pause_1,(445,750))
                pause_judge=1
        #游戏暂停
        if pause_judge==1:
            screen.blit(start_but, (150, 300))
            ts_continue= font1.render("CONTINUE", True, (255, 255, 255))
            screen.blit(ts_continue, (200, 300))
            screen.blit(exit_but, (150, 500))
            ts_exit = font1.render("EXIT GAME", True, (255, 255, 255))
            screen.blit(ts_exit, (200, 500))
            hx, hy = pygame.mouse.get_pos()
            a, b, c = pygame.mouse.get_pressed()
            if hx>150 and hx<150+38 and hy>300 and hy<300+41 and a:
                pause_judge=0
            elif hx > 150 and hx < 150 + 38 and hy > 500 and hy < 500 + 41 and a:
                exit()

        ts_num = font.render(s_num, True, (255, 255, 255))
        screen.blit(score, (350, 10))
        screen.blit(ts_num, (430, 10))
    pygame.display.update()