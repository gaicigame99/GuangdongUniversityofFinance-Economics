import pygame
import random
pygame.init()
import random
#界面
font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",25)
background=pygame.image.load("background.png")
b1=pygame.image.load("name.png")
b1=pygame.transform.scale(b1,(250,100))
b2=pygame.image.load("11.png")
b2=pygame.transform.scale(b2,(180,50))
b3=pygame.image.load("33.png")
b3=pygame.transform.scale(b3,(180,50))
b4=pygame.image.load("22.png")
b4=pygame.transform.scale(b4,(180,50))
b5=pygame.image.load("game_loading2.png")
b5=pygame.transform.scale(b5,(100,40))
b6=pygame.image.load("game_loading1.png")
b6=pygame.transform.scale(b6,(100,40))
b7=pygame.image.load("bomb-1.gif")
b7=pygame.transform.scale(b7,(100,140))
b8=pygame.image.load("44.png")
b8=pygame.transform.scale(b8,(200,80))
b9=pygame.image.load("55.png")
b9=pygame.transform.scale(b9,(300,80))
b10=pygame.image.load("66.png")
b10=pygame.transform.scale(b10,(100,80))
b11=pygame.image.load("77.png")
b11=pygame.transform.scale(b11,(260,80))
b12=pygame.image.load("88.png")
b12=pygame.transform.scale(b12,(100,80))
b13=pygame.image.load("99.png")
b13=pygame.transform.scale(b13,(300,80))
b14=pygame.image.load("game_pause_nor.png")
b14=pygame.transform.scale(b14,(100,50))
b15=pygame.image.load("game_resume_nor.png")
b15=pygame.transform.scale(b15,(100,50))
b16=pygame.image.load("hong.jpg")
b16=pygame.transform.scale(b16,(140,6))
b16_en=pygame.transform.scale(b16,(40,6))
b16_en1=pygame.transform.scale(b16,(68,6))
b17=pygame.image.load("hui.jpg")
b17_hr1=pygame.transform.scale(b17,(140,6))
b17_hr2=pygame.transform.scale(b17,(110,6))
b17_hr3=pygame.transform.scale(b17,(80,6))
b17_hr4=pygame.transform.scale(b17,(50,6))
b17_hr5=pygame.transform.scale(b17,(20,6))
b17_en1=pygame.transform.scale(b17,(40,6))
b17_en2=pygame.transform.scale(b17,(30,6))
b17_en3=pygame.transform.scale(b17,(20,6))
b17_en4=pygame.transform.scale(b17,(10,6))
b17_en11=pygame.transform.scale(b17,(70,6))
b17_en12=pygame.transform.scale(b17,(50,6))
b17_en13=pygame.transform.scale(b17,(30,6))
b17_en14=pygame.transform.scale(b17,(10,6))
b18=pygame.image.load("hero_blowup_n1.png")
b19=pygame.image.load("hero_blowup_n2.png")
b20=pygame.image.load("hero_blowup_n3.png")
b21=pygame.image.load("hero_blowup_n4.png")
blood1=pygame.image.load("bomb-1.gif")
blood2=pygame.image.load("bomb-2.gif")
blood1_y=random.randint(0,200)
b16_x=0
b16_y=0
b17_x=0
b17_y=0
screen=pygame.display.set_mode((600,800))
background=pygame.transform.scale(background,(600,800))

hero=pygame.image.load("hero.gif")
zidan=pygame.image.load("bullet1.png")
zidan=pygame.transform.scale(zidan,(12,12))
zidan1=pygame.image.load("bullet2.png")
zidan1=pygame.transform.scale(zidan1,(12,12))

#中小战机爆炸图片存成列表
en=[]
en_down1_y=0
en_down3_y=0
en_down4_y=0
en1=[]
en1_down1=[]
en1_down2=[]
en1_down3=[]
en1_down4=[]
#八个小战机都是这个图片以及每个战机爆炸的4张图
enemy=pygame.image.load("enemy0.png")
enemy_down1=pygame.image.load("enemy0_down1.png")
enemy_down3=pygame.image.load("enemy0_down3.png")
enemy_down4=pygame.image.load("enemy0_down4.png")
# for i in range(8):              #enemy0
#     en.append(enemy)
#     en_down1.append(enemy_down1)
#     en_down3.append(enemy_down3)
#     en_down4.append(enemy_down4)
#八个中战机都是这个图片以及每个战机爆炸的4张图
enemy1=pygame.image.load("enemy1.png")
enemy1_down1=pygame.image.load("enemy1_down1.png")
enemy1_down2=pygame.image.load("enemy1_down2.png")
enemy1_down3=pygame.image.load("enemy1_down3.png")
enemy1_down4=pygame.image.load("enemy1_down4.png")
for i in range(8):                  #enemy1
    en1.append(enemy1)
    en1_down1.append(enemy_down1)
    en1_down2.append(enemy1_down2)
    en1_down3.append(enemy1_down3)
    en1_down4.append(enemy1_down4)
#最后的大boss以及爆炸的6张图片
enemy2=pygame.image.load("enemy2.png")
enemy2_down1=pygame.image.load("enemy2_down1.png")
enemy2_down2=pygame.image.load("enemy2_down2.png")
enemy2_down3=pygame.image.load("enemy2_down3.png")
enemy2_down4=pygame.image.load("enemy2_down4.png")
enemy2_down5=pygame.image.load("enemy2_down5.png")
enemy2_down6=pygame.image.load("enemy2_down6.png")
#获得小战机的宽和高
enemy_rect=enemy.get_rect()
enemy_width=enemy_rect.width
enemy_height=enemy_rect.height
#获得中战机的宽和高
enemy1_rect=enemy1.get_rect()
enemy1_width=enemy1_rect.width
enemy1_height=enemy1_rect.height
#获得大战机的宽和高
enemy2_rect=enemy2.get_rect()
enemy2_width=enemy2_rect.width
enemy2_height=enemy2_rect.height
#获得英雄的宽和高
hero_rect=hero.get_rect()
hero_width=hero_rect.width
hero_height=hero_rect.height
#获得八个小战机的随机坐标
en_x=random.randint(50,500)
en_y=random.randint(0,300)
en1_x=random.randint(50,500)
en1_y=random.randint(0,300)
# en_down1_y=[]
# en_down3_y=[]
# en_down4_y=[]
# for i in range(8):
#     x=random.randint(100,500)
#     y=random.randint(50,300)
#     en_x.append(x)
#     en_y.append(y)
#获得八个中战机的随机坐标
# en1_x=[]
# en1_y=[]
# en1_down1_y=
# en1_down3_y=
# en1_down4_y=
b1_y=100
b2_y=380
b3_y=480
b4_y=580
b5_y=180
b6_y=280
b7_y=540
b8_y=200
b9_y=290
b10_y=290
b14_y=20
speed_y=0
flag=0
game_start=0
zi_x=[]
zi_y=[]
zi1_x=[]
zi1_y=[]
zi2_x=[]
zi2_y=[]
zi_speed=50
time=5
score=0
bb=0
flag1=0
flag2=0
flag3=0
flag4=0
flag5=0
flag22=0
flag33=0
flag_hero=0
flag_en=0
flag_en1=0
flag3_hero=0
blood=0
zi1=[]
zi2=[]
# for i in range(8):
#     x=random.randint(100,500)
#     y=random.randint(50,300)
#     en1_x.append(x)
#     en1_y.append(y)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(background, (0, 0))
    a, b, c = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse1_x, mouse1_y = pygame.mouse.get_pos()
    b1_y -= speed_y
    b2_y -= speed_y
    b3_y -= speed_y
    b4_y -= speed_y
    b5_y -= speed_y
    b6_y -= speed_y
    b7_y -= speed_y
    screen.blit(b1, (170, b1_y))
    screen.blit(b2, (220, b2_y))
    screen.blit(b3, (220, b3_y))
    screen.blit(b4, (220, b4_y))
    screen.blit(b5, (90, b5_y))
    screen.blit(b6, (390, b6_y))
    screen.blit(b7, (120, b7_y))
    if mouse_x > 220 and mouse_x < 220+180 and mouse_y> 380 and mouse_y < 380 + 50 and a:
        speed_y=50
        game_start=1
    # if mouse_x > 220 and mouse_x < 220+180 and mouse_y> 480 and mouse_y < 480 + 50 and a and bb==0:
    #     speed_y = 50
    #     flag=1
    # if flag==1:
    #     screen.blit(b8, (200, 200))
    #     screen.blit(b9, (100, 290))
    #     screen.blit(b10, (400, 290))
    #     screen.blit(b14, (500, 20))
    # if mouse_x > 220 and mouse_x < 220 + 180 and mouse_y > 580 and mouse_y < 580 + 50 and a and bb==0:
    #     speed_y = 50
    #     flag = 2
    # if flag==2:
    #     screen.blit(b11, (190, 209))
    #     screen.blit(b12, (400, 290))
    #     screen.blit(b13, (100, 290))
    #     screen.blit(b14,(500,20))
    if game_start==1:
        bb=1
        font1=font.render("Score="+str(score),True,(0,0,0))
        screen.blit(hero, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
        if flag_hero==0:
            screen.blit(b16,(mouse_x-hero_width+30,mouse_y+hero_height/2-18))
        if flag_en==0:
            screen.blit(b16_en, (en_x+6, en_y-5))
        if flag_en1==0:
            screen.blit(b16_en1, (en1_x - 1, en1_y - 5))
        screen.blit(font1, (20, 20))
        if time:
            time -= 1  # 循环5次才发射一颗子弹
        else:  # 当time为0时执行
            zi_x.append(mouse_x - 3)
            zi_y.append(mouse_y - hero_height / 2)
            zi1_x.append(en_x+18)
            zi1_y.append(en_y+15)
            zi2_x.append(en1_x + 28)
            zi2_y.append(en1_y + 29)
            time = 5
        for i in range(len(zi_x)):
            if flag_hero==0:
                screen.blit(zidan,(zi_x[i],zi_y[i]))
            if flag_en==0:
                screen.blit(zidan1, (zi1_x[i], zi1_y[i]))
            if flag_en1==0:
                screen.blit(zidan1, (zi2_x[i], zi2_y[i]))
            if flag1==0:
                screen.blit(enemy,(en_x,en_y))
                # screen.blit(b17,(en_x+6,en_y-5))
            if flag1==1:
                screen.blit(enemy_down1, (en_x, en_y))
                screen.blit(b17_en4, (en_x+6, en_y-5))
            if flag1==2:
                screen.blit(enemy_down3, (en_x, en_y))
                screen.blit(b17_en3, (en_x+6, en_y-5))
            if flag1==3:
                screen.blit(enemy_down4, (en_x, en_y))
                screen.blit(b17_en2, (en_x+6, en_y-5))
            if 400<mouse_x<430 and blood1_y<mouse_y-50<blood1_y+30:
                screen.blit(blood1,(200,-blood1_y))
                blood=1
                screen.blit(b17_hr5,(-500,-900))
                flag2=0
                flag3=0
                flag33=0
                # screen.blit()
            if blood==0:
                screen.blit(blood1, (400, blood1_y))
            blood1_y+=0.01
            en_y += 0.01
            en1_y+=0.02
            zi_y[i] -= zi_speed
            zi1_y[i]+=30
            zi2_y[i]+=30
            if en_x < zi_x[i] < en_x + enemy_width and en_y < zi_y[i] < en_y + enemy_height:  # 子弹碰到小战机条件
                zi_y[i]=random.randint(-1500,-1200)
                flag+= 1  # 随着循环逐渐增加子弹射中的次数
                print("flag=%d" % flag)
                if 2 < flag< 5:
                    flag1 = 1
                    screen.blit(enemy, (200, -180))
                elif 5 < flag < 10:
                    flag1 = 2
                    screen.blit(enemy_down1, (200, -180))
                elif 10 < flag< 20:
                    flag1 = 3
                    screen.blit(enemy_down3, (200, -180))
                if flag == 20:
                    flag1= 4
                    screen.blit(enemy_down4, (200, -180))
                    screen.blit(enemy, (200, -100))
                if flag > 20:
                    flag_en=1


            if flag3==0:
                screen.blit(hero,(mouse_x - hero_width / 2,mouse_y - hero_height / 2))
            if flag3==1:
                if blood == 0:
                    screen.blit(b17_hr5,(mouse_x-hero_width+30,mouse_y+hero_height/2-18))
                    screen.blit(b18, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                if blood==1:
                    screen.blit(b18, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr5, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if flag3==2:
                if blood==0:
                    screen.blit(b19, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr4, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
                if blood==1:
                    screen.blit(b19, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr4, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if flag3==3:
                if blood==0:
                    screen.blit(b20, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr3, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
                if blood==1:
                    screen.blit(b20, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr3, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if flag3 == 4:
                if blood==0:
                    screen.blit(b21, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr2, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
                if blood==1:
                    screen.blit(b21, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr2, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if mouse_x - 30 < zi1_x[i] < mouse_x - 30 + hero_width and mouse_y - hero_height / 2 < zi1_y[i] < mouse_y - hero_height / 2 + hero_height:  # 子弹碰到小战机条件
                zi1_y[i]=random.randint(1200,1800)
                flag2+= 1  # 随着循环逐渐增加子弹射中的次数
                print("flag2=%d" % flag2)
                if 20 < flag2< 100:
                    flag3 = 1
                    screen.blit(hero, (200, -180))
                elif 100 < flag2 < 200:
                    flag3 = 2
                    screen.blit(b18, (200, -180))
                elif 200 < flag2< 400:
                    flag3 = 3
                    screen.blit(b19, (200, -180))
                elif 400 < flag2 < 600:
                    flag3 = 4
                    screen.blit(b20, (200, -180))
                if flag2 == 600:
                    flag3= 5
                    screen.blit(b21, (200, -180))
                    screen.blit(hero, (200, -200))
                if flag > 600:
                    flag_hero=1

            if flag4==0:
                screen.blit(enemy1,(en1_x,en1_y))
                # screen.blit(b17,(en_x+6,en_y-5))
            if flag4==1:
                screen.blit(enemy1_down1, (en1_x, en1_y))
                screen.blit(b17_en14, (en1_x-2, en1_y-5))
            if flag4==2:
                screen.blit(enemy1_down3, (en1_x, en1_y))
                screen.blit(b17_en13, (en1_x-2, en1_y-5))
            if flag4==3:
                screen.blit(enemy1_down4, (en1_x, en1_y))
                screen.blit(b17_en12, (en1_x-2, en1_y-5))
            if en1_x < zi_x[i] < en1_x + enemy1_width and en1_y < zi_y[i] < en1_y + enemy1_height:  # 子弹碰到小战机条件
                zi_y[i]=random.randint(-1500,-1200)
                flag5+= 1  # 随着循环逐渐增加子弹射中的次数
                print("flag5=%d" % flag5)
                if 2 < flag5< 10:
                    flag4 = 1
                    screen.blit(enemy1, (200, -180))
                elif 10 < flag5 < 20:
                    flag4 = 2
                    screen.blit(enemy1_down1, (200, -180))
                elif 20 < flag5< 38:
                    flag4 = 3
                    screen.blit(enemy1_down3, (200, -180))
                if flag5 == 38:
                    flag4= 4
                    screen.blit(enemy1_down4, (200, -180))
                    screen.blit(enemy1, (200, -100))
                if flag5 > 38:
                    flag_en1=1

            if flag33==0:
                screen.blit(hero,(mouse_x - hero_width / 2,mouse_y - hero_height / 2))
            if flag33==1:
                if blood==0:
                    screen.blit(b17_hr5,(mouse_x-hero_width+30,mouse_y+hero_height/2-18))
                    screen.blit(b18, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                if blood==1:
                    screen.blit(b18, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr5, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if flag33==2:
                if blood==0:
                    screen.blit(b19, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr4, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
                if blood==1:
                    screen.blit(b19, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr4, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if flag33==3:
                if blood==0:
                    screen.blit(b20, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr3, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
                if blood==1:
                    screen.blit(b20, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr3, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if flag33 == 4:
                if blood==0:
                    screen.blit(b21, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr2, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
                if blood==1:
                    screen.blit(b21, (mouse_x - hero_width / 2, mouse_y - hero_height / 2))
                    screen.blit(b17_hr2, (mouse_x - hero_width + 30, mouse_y + hero_height / 2 - 18))
            if mouse_x - 30 < zi2_x[i] < mouse_x - 30 + hero_width and mouse_y - hero_height / 2 < zi2_y[i] < mouse_y - hero_height / 2 + hero_height:  # 子弹碰到小战机条件
                zi2_y[i]=random.randint(1200,1800)
                flag2+= 1  # 随着循环逐渐增加子弹射中的次数
                print("flag2=%d" % flag2)
                if 20 < flag2< 100:
                    flag33 = 1
                    screen.blit(hero, (200, -180))
                elif 100 < flag2 < 200:
                    flag33 = 2
                    screen.blit(b18, (200, -180))
                elif 200 < flag2< 400:
                    flag33 = 3
                    screen.blit(b19, (200, -180))
                elif 400< flag2 < 600:
                    flag33 = 4
                    screen.blit(b20, (200, -180))
                if flag2 == 600:
                    flag33= 5
                    screen.blit(b21, (200, -180))
                    screen.blit(hero, (200, -200))
                if flag2 > 3000:
                    flag_hero=1






    pygame.display.update()