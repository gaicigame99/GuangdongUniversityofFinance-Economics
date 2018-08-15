import pygame
import random
import time

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((500,900))

hero=pygame.image.load("images\hero.gif")
bg=pygame.image.load(r"images\background.png")
name=pygame.image.load(r"images\name.png")

game_loading2=pygame.image.load("game_loading2.png")


bg=pygame.transform.scale(bg,(500,900))
bullet=pygame.image.load(r"images\bullet.png")
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)
font2 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 18)

#背景音乐
back_music=pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()
#子弹音乐
boom=pygame.mixer.Sound("sound\enemy2_down.wav")






score=0
level=0
showscore = font.render("score:"+str(score), True, (255, 255, 255))
showgameover = font.render("gameover", True, (255, 255, 255))

enemy=pygame.image.load(r"images\enemy0.png")
enemy_down1=pygame.image.load(r"images\enemy0_down1.png")
enemy_down2=pygame.image.load(r"images\enemy0_down2.png")
enemy_down3=pygame.image.load(r"images\enemy0_down3.png")
enemy_down4=pygame.image.load(r"images\enemy0_down4.png")

enemy2=pygame.image.load(r"images\enemy1.png")
enemy2_down1=pygame.image.load(r"images\enemy1_down1.png")
enemy2_down2=pygame.image.load(r"images\enemy1_down2.png")
enemy2_down3=pygame.image.load(r"images\enemy1_down3.png")
enemy2_down4=pygame.image.load(r"images\enemy1_down4.png")

hero_boom1=pygame.image.load(r"images\hero_blowup_n1.png")
hero_boom2=pygame.image.load(r"images\hero_blowup_n2.png")
hero_boom3=pygame.image.load(r"images\hero_blowup_n3.png")
hero_boom4=pygame.image.load(r"images\hero_blowup_n4.png")



#道具定义
airdrop1=pygame.image.load(r"images\prop_type_0.png")
x_a1=random.randint(10,450)
y_a1=-1
a_speed=1
ax_speed=1
#是否吃到道具
flag_a=0


hx=200
hy=750
speed=10
speed_e=3
myhp=3
h_rect=hero.get_rect()
h_width=h_rect.width
h_height=h_rect.height
success=0

time1=[]
time2=[]
tx=[]
ty=[]
tx2=[]
ty2=[]


ex=[]
ey=[]

ex2=[]
ey2=[]
e2_hp=[]

enemy1_number=10
enemy2_number=5

a=[]
for i in range(enemy1_number):
    ex.append(random.randint(1,450))
    ey.append(random.randint(-2000,0))

for i in range(enemy2_number):
    ex2.append(random.randint(1,450))
    ey2.append(random.randint(-2000,0))
    #大飞机血量
    e2_hp.append(4)
bx=[]
by=[]
fps=30
def daoju(flag_a):
    if flag_a!=0:
        return flag_a*5
    else:
        return 0
start=0
buttom_start=pygame.image.load("start.png")
buttom_stop=pygame.image.load("stop.png")
buttom_exit=pygame.image.load("exit.png")

start_time=time.time()

jiazai=0
while True:
    if time.time()-start_time<2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(bg,(0,0))
        screen.blit(name, (50, 200))

        if jiazai<200:
            jiazai += 1
        screen.blit(game_loading2,(200+jiazai,500))
        pygame.display.update()
    else:
        break

while True:
    # screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        # print(event.type)
        if event.type == pygame.QUIT:
            # print(event.type)
            exit()
    screen.blit(bg, (0, 0))

    #等待开始游戏
    if start==0:
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(event.type)
            mx,my=pygame.mouse.get_pos()
            if 200<=mx and mx<260 and my>=500 and my<560:
                start=4
            if 200<=mx and mx<260 and my>=600 and my<660:
                start=3
        screen.blit(buttom_start, (200, 500))
        screen.blit(name, (40, 200))
        showstart = font2.render("NEW GAME", True, (0, 0, 0))
        screen.blit(showstart, (260, 520))
        showexit = font2.render("EXIT", True, (0, 0, 0))
        screen.blit(showexit, (260, 620))
        screen.blit(buttom_exit, (200, 600))
        pygame.display.update()

    if start == 3:
        exit()






        pygame.display.update()
    #游戏暂停
    elif start==2:

        # screen.blit(buttom_start, (200, 500))
        #
        # screen.blit(name, (40, 200))
        # screen.blit(showcontinue, (260, 520))
        # screen.blit(bg, (0, 0))
        # screen.blit(buttom_start, (200, 500))
        if event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if 200<=mx and mx<260 and my>=500 and my<560:
                start=4
            if 200<=mx and mx<260 and my>=600 and my<660:
                start=3
        showcontinue = font2.render("CONTINUE", True, (0, 0, 0))
        showexit = font2.render("EXIT", True, (0, 0, 0))
        screen.blit(showexit, (260, 620))
        screen.blit(buttom_exit, (200, 600))
        screen.blit(buttom_start, (200,500))
        screen.blit(showcontinue, (260, 520))
        screen.blit(name, (40, 200))
        pygame.display.update()



    #游戏开始
    if start==4:
        ammo_music = pygame.mixer.Sound(r"sound\bullet.wav")
        ammo_music.play()


        fps+=int(daoju(flag_a))
        #道具移动
        y_a1+=a_speed
        x_a1+=ax_speed
        if x_a1>450 or x_a1<=0:
            ax_speed=-ax_speed

        if y_a1>900:
            y_a1=random.randint(-200,0)
        screen.blit(airdrop1, (x_a1, y_a1))
        screen.blit(buttom_stop, (450, 800))
        showlevel = font.render("level:" + str(level), True, (255, 255, 255))
        showscore = font.render("score:" + str(score), True, (255, 255, 255))
        showhp = font.render("HP:" + str(myhp), True, (255, 255, 255))
        showsuccess = font.render("Mission Success!", True, (255, 255, 255))
        screen.blit(showscore,(350,36))
        screen.blit(showlevel,(350,72))
        screen.blit(showhp, (350, 108))
        #我的飞机
        if myhp==3:
            screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))
        if myhp == 2:
            screen.blit(hero_boom1, (hx - h_width / 2, hy - h_height / 2))
        if myhp==1:
            screen.blit(hero_boom2, (hx - h_width / 2, hy - h_height / 2))
        if myhp ==0:
            screen.blit(hero_boom3, (hx - h_width / 2, hy - h_height / 2))
            screen.blit(hero_boom4, (hx - h_width / 2, hy - h_height / 2))




        hx,hy=pygame.mouse.get_pos()
        #吃道具
        if x_a1-50<hx<=x_a1+50 and y_a1-50<hy<=y_a1+150:
            x_a1=random.randint(2,450)
            y_a1=random.randint(-2000,0)
            flag_a=1
        if event.type == pygame.MOUSEBUTTONDOWN:
             mx1, my1 = pygame.mouse.get_pos()
             if 400<= mx1 < 500 and 700 <= my1 <= 850:
                 start = 2
        # screen.blit(bullet, (bx[i],by[i]))
        if fps<30:
            fps+=1
        else:
            bx.append(hx)
            by.append(hy)
            fps=0
        for i in by:
            index=by.index(i)
            if i<0:
                by.pop(index)
                bx.pop(index)
        #子弹发射
        for i in range(len(bx)):
            by[i]-=speed
            if success == 1:
                screen.blit(showsuccess, (150, 300))
                break
            if myhp <= 0:
                screen.blit(showgameover, (200, 250))
                break
            screen.blit(bullet, (bx[i]-10, by[i]-50))
            #撞上敌人小飞机
            for j in range(len(ex)):
                if ex[j]-50<=hx<=ex[j]+100 and ey[j]<hy<=ey[j]+50 :
                    time1.append(time.time())
                    tx.append(ex[j])
                    ty.append(ey[j])
                    ey[j] = random.randint(-2000, -500)
                    ex[j] = random.randint(1, 450)
                    myhp-=1
                if myhp<=0:
                    break
                # 击中敌人飞机
                elif ex[j]<=bx[i]<=ex[j]+50 and ey[j]<by[i]<=ey[j]+50:
                    # boom1()
                    if j>=enemy1_number:
                        bx[j]=-200
                    time1.append(time.time())
                    tx.append(ex[j])
                    ty.append(ey[j])
                    ey[j] = random.randint(-2000, -500)
                    ex[j] = random.randint(1, 450)
                    bx[i]=-999
                    by[i]=-999
                    #加分
                    score += 1
                    boom.play()

            #撞上大飞机
            for k in range(len(ex2)):
                if ex2[k]-50<=hx<=ex2[k]+130 and ey2[k]<hy<=ey2[k]+50:
                    time2.append(time.time())
                    tx2.append(ex2[k])
                    ty2.append(ey2[k])
                    ey2[k] = random.randint(-2000, -500)
                    ex2[k] = random.randint(1, 450)
                    myhp -= 1
                    e2_hp[k] =0
                if myhp <= 0:
                    break
                #集中大飞机
                for k in range(len(ex2)):
                    if ex2[k]<=bx[i]<=ex2[k]+70 and ey2[k]<by[i]<=ey2[k]+50:
                        e2_hp[k]-=1
                        bx[i] = -999
                        by[i] = -999
                        if e2_hp[k]==0:
                            # boom2()
                            time2.append(time.time())
                            tx2.append(ex2[k])
                            ty2.append(ey2[k])
                            ey2[k] = random.randint(-2000, -500)
                            ex2[k] = random.randint(1, 450)
                            e2_hp[k] = 4
                            #加分
                            score += 5
                            e2_hp[k]=4
                            boom.play()

                        if k>=enemy2_number:
                            bx[k]=-200
            if len(time1):
                for i in range(len(time1)):
                    a = time.time() - time1[i]
                    if 0 < a < 0.1:
                        screen.blit(enemy_down1, (tx[i], ty[i]))
                        boom.play()
                    if 0.1 <= a < 0.2:
                        screen.blit(enemy_down2, (tx[i], ty[i]))
                    if 0.2 <= a < 0.3:
                        screen.blit(enemy_down3, (tx[i], ty[i]))
                    if 0.3 <= a < 0.4:
                        screen.blit(enemy_down4, (tx[i], ty[i]))
            if len(time2):
                for i in range(len(time2)):
                    a = time.time() - time2[i]
                    if 0 < a < 0.1:
                        screen.blit(enemy2_down1, (tx2[i], ty2[i]))
                        boom.play()
                    if 0.1 <= a < 0.2:
                        screen.blit(enemy2_down2, (tx2[i], ty2[i]))
                    if 0.2 <= a < 0.3:
                        screen.blit(enemy2_down3, (tx2[i], ty2[i]))
                    if 0.3 <= a < 0.4:
                        screen.blit(enemy2_down4, (tx2[i], ty2[i]))
        for i in range(len(ex)):
            screen.blit(enemy,(ex[i],ey[i]))
            ey[i]+=speed_e
            if ey[i]>900:
                ey[i]=random.randint(-2000,-500)
                ex[i] = random.randint(1, 850)
        for i in range(len(ex2)):
            if  3<e2_hp[i]<=4:
                pygame.draw.line(screen, (0, 0, 0), (ex2[i], ey2[i]), (ex2[i] + 70, ey2[i]), 5)
                pygame.draw.line(screen, (0, 255, 0), (ex2[i], ey2[i]), (ex2[i] + 70, ey2[i]), 5)
                screen.blit(enemy2,(ex2[i],ey2[i]))
            if 2<e2_hp[i]<=3:
                pygame.draw.line(screen, (0, 0, 0), (ex2[i], ey2[i]), (ex2[i] + 70, ey2[i]), 5)
                pygame.draw.line(screen, (0, 255, 0), (ex2[i], ey2[i]), (ex2[i] + 50, ey2[i]), 5)
                screen.blit(enemy2_down1,(ex2[i],ey2[i]))
            if 0<=e2_hp[i]<=2:
                pygame.draw.line(screen, (0, 0, 0), (ex2[i], ey2[i]), (ex2[i] + 70, ey2[i]), 5)
                pygame.draw.line(screen, (0, 255, 0), (ex2[i], ey2[i]), (ex2[i] + 25, ey2[i]), 5)
                screen.blit(enemy2_down2,(ex2[i],ey2[i]))
            # show_hp2 = font.render("hp:" + str(e2_hp[i]), True, (255, 255, 255))
            #
            # screen.blit(show_hp2, (ex2[i], ey2[i]-20))
            ey2[i]+=speed_e
            if ey2[i]>900:
                ey2[i]=random.randint(-2000,-500)
                ex2[i] = random.randint(1, 450)
                e2_hp[i]=4
        for i in range(21):
            if score>10*i:
                speed_e = 3+i
                level=i
            if level==20:
                success=1
                break




        pygame.display.update()