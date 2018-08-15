import pygame
import random

pygame.init()
screen=pygame.display.set_mode((600,1000))
background=pygame.image.load(r"images\background.png")
background=pygame.transform.scale(background,(600,1000))
quanhei=pygame.image.load(r'C:\Users\502teacher\PycharmProjects\untitled\day11\营庄杰\hei.png')
quanhei=pygame.transform.scale(quanhei,(1000,1000))
RED_COLOR=(255,0,0)
hero=pygame.image.load("images\hero.gif")
font=pygame.font.Font("C:\Windows\Fonts\Verdana.ttf",26)
hx=100
hy=100
h_rect=hero.get_rect()
h_width=h_rect.width
h_height=h_rect.height
h_blood=5

bullet1=pygame.image.load(r"images\bullet-1.gif")
b_rect=bullet1.get_rect()
b_width=b_rect.width
b_height=b_rect.height
b_x=[]
b_y=[]
b_speed=12
b_v=10    #发射频率
time=b_v

enemy=pygame.image.load("images\enemy0.png")
enemy_x=[]
enemy_y=[]
enemy_x_speed = []
enemy_y_speed = []

enemy1=pygame.image.load("images\enemy1.png")
enemy1_x=[]
enemy1_y=[]
blood_enemy1=[]
enemy1_x_speed = []
enemy1_y_speed = []

enemy2=pygame.image.load("images\enemy2.png")
enemy2_x=[]
enemy2_y=[]
blood_enemy2=[]
enemy2_x_speed = []
enemy2_y_speed = []

font=pygame.font.Font("C:\Windows\Fonts\Verdana.ttf",20)       #字体
PURPLE_COLOR=(100,100,200)
score=0

kaishijiemian = pygame.image.load(r'C:\Users\502teacher\PycharmProjects\untitled\day11\营庄杰\kaishijiemian.png')  #开始界面
kaishijiemian = pygame.transform.scale(kaishijiemian, (600, 1000))
start_button = pygame.image.load(r'C:\Users\502teacher\PycharmProjects\untitled\day11\营庄杰\youxikaishi.png')
start_button = pygame.transform.scale(start_button, (200, 200))
button_x = 200
button_y = 600
button_rect = start_button.get_rect()
kaishi_x=0
kaishi_y=0
kaishi_speed=0
button_speed=0

for i in range(15):  # 小敌人初始坐标
    a = random.randint(10, 550)
    enemy_x.append(a)
    b = random.randint(-150,-100 )
    enemy_y.append(b)
    enemy_x_speed.append(1)
    enemy_y_speed.append(1)
for i in range(8):  # 中敌人初始坐标
    a = random.randint(10, 550)
    enemy1_x.append(a)
    b = random.randint(-300,-200 )
    enemy1_y.append(b)
    enemy1_x_speed.append(1)
    enemy1_y_speed.append(1)
    blood_enemy1.append(3)
for i in range(5):  # 大敌人初始坐标
        a = random.randint(10, 550)
        enemy2_x.append(a)
        b = random.randint(-600, -500)
        enemy2_y.append(b)
        enemy2_x_speed.append(1)
        enemy2_y_speed.append(1)
        blood_enemy2.append(5)

e_rect=enemy.get_rect()
e_width=e_rect.width
e_height=e_rect.height
e_rect1=enemy1.get_rect()
e_width1=e_rect1.width
e_height1=e_rect1.height
e_rect2=enemy2.get_rect()
e_width2=e_rect2.width
e_height2=e_rect2.height

baozha1=pygame.image.load("images\enemy0_down1.png")                                   #爆炸图片
baozha2=pygame.image.load("images\enemy0_down2.png")
baozha3=pygame.image.load("images\enemy0_down3.png")
baozha4=pygame.image.load("images\enemy0_down4.png")
baozha5=pygame.image.load("images\enemy1_down1.png")
baozha6=pygame.image.load("images\enemy1_down2.png")
baozha7=pygame.image.load("images\enemy1_down3.png")
baozha8=pygame.image.load("images\enemy1_down4.png")
baozha9=pygame.image.load("images\enemy2_down1.png")
baozha10=pygame.image.load("images\enemy2_down2.png")
baozha11=pygame.image.load("images\enemy2_down3.png")
baozha12=pygame.image.load("images\enemy2_down4.png")
baozha13=pygame.image.load("images\enemy2_down5.png")
baozha14=pygame.image.load("images\enemy2_down6.png")
tuichu=pygame.image.load("images\quit_sel.png")
tuichu_rect=tuichu.get_rect()                                                    #退出按钮设定
tuichu_x=230
tuichu_y=700
flag=0

baozha1_x=[]
baozha1_y=[]
baozha2_x=[]
baozha2_y=[]
baozha3_x=[]
baozha3_y=[]
chixushijian1=[]
chixushijian2=[]
chixushijian3=[]

back_music=pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()
d=1
game_start=165
game_start_speed=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    if(game_start>0):                                                              #开始封面
        screen.blit(background, (0, 0))
    game_start-=game_start_speed
    kaishi_y -= kaishi_speed
    button_y -= button_speed
    screen.blit(kaishijiemian, (kaishi_x, kaishi_y))
    screen.blit(start_button, (button_x, button_y))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click, b, c = pygame.mouse.get_pressed()
    if (mouse_x > button_x and mouse_x < button_x + button_rect.width and
            mouse_y > button_y and mouse_y < button_y + button_rect.height):
        if (click == 1):
            kaishi_speed = 15
            button_speed = 15
            game_start_speed=2
    if(game_start<=0):
        screen.blit(background, (0, 0))
        defen = font.render('Score: ', True, PURPLE_COLOR)
        screen.blit(defen, (10, 10))
        hx,hy=pygame.mouse.get_pos()
        if time:                                                                 #装填子弹
            time-=1
        else:
            b_x.append(hx-b_rect.width/2+2)
            b_y.append(hy-h_height/2-b_rect.height)
            time=b_v
        for i in range(len(b_x)):                                                #子弹移动
            screen.blit(bullet1, (b_x[i],b_y[i]))
            b_y[i]-=b_speed
            if(b_y[i]<0-b_rect.height):
                del b_y[i]
                del b_x[i]
                break
            for j in range(len(enemy_y)):
                if (b_y[i] < enemy_y[j] + e_rect.height and b_x[i] + b_rect.width > enemy_x[j]      #子弹碰到小敌人
                    and b_x[i] < enemy_x[j] + e_rect.width and b_y[i]+ b_height>enemy_y[j]):
                    b_y[i] = -1500
                    b_x[i] = -1500
                    score+=1
                    baozha1_x.append(enemy_x[j])
                    baozha1_y.append(enemy_y[j])
                    chixushijian1.append(40)
                    del enemy_y[j]
                    del enemy_x[j]
                    del enemy_x_speed[j]
                    del enemy_y_speed[j]
                    break

            for j in range(len(enemy1_y)):
                if (b_y[i] < enemy1_y[j] + e_rect1.height and b_x[i] + b_rect.width > enemy1_x[j]      # 子弹碰到中敌人
                        and b_x[i] < enemy1_x[j] + e_rect1.width and b_y[i] + b_height > enemy1_y[j]):
                    score += 1
                    b_y[i] = -1500
                    b_x[i] = -1500
                    blood_enemy1[j]=blood_enemy1[j]-1
                    if(blood_enemy1[j]<=0):
                        baozha2_x.append(enemy1_x[j])
                        baozha2_y.append(enemy1_y[j])
                        chixushijian2.append(40)
                        del enemy1_y[j]
                        del enemy1_x[j]
                        del blood_enemy1[j]
                        del enemy1_x_speed[j]
                        del enemy1_y_speed[j]
                        break

            for j in range(len(enemy2_y)):
                if (b_y[i] < enemy2_y[j] + e_rect2.height and b_x[i] + b_rect.width > enemy2_x[j]      # 子弹碰到大敌人
                        and b_x[i] < enemy2_x[j] + e_rect2.width and b_y[i] + b_height > enemy2_y[j]):
                    b_y[i] = -1500
                    b_x[i] = -1500
                    score += 1
                    blood_enemy2[j]=blood_enemy2[j]-1
                    if(blood_enemy2[j]<=0):
                        baozha3_x.append(enemy2_x[j])
                        baozha3_y.append(enemy2_y[j])
                        chixushijian3.append(60)
                        del enemy2_y[j]
                        del enemy2_x[j]
                        del blood_enemy2[j]
                        del enemy2_x_speed[j]
                        del enemy2_y_speed[j]
                        break

        if (d==1):                                                                      # 小敌人爆炸效果
            if(len(baozha1_x)!=0):
                for i in range(len(baozha1_x)):
                    if(41>chixushijian1[i]>30):
                        screen.blit(baozha1, (baozha1_x[i], baozha1_y[i]))
                        chixushijian1[i] -= 1
                    if (30>=chixushijian1[i]>20):
                        screen.blit(baozha2, (baozha1_x[i], baozha1_y[i]))
                        chixushijian1[i] -= 1
                    if (20 >= chixushijian1[i] > 10):
                        screen.blit(baozha3, (baozha1_x[i], baozha1_y[i]))
                        chixushijian1[i] -= 1
                    if (10 >= chixushijian1[i] > 0):
                        screen.blit(baozha4, (baozha1_x[i], baozha1_y[i]))
                        chixushijian1[i]-=1

        if (d==1):                                                                      # 中敌人爆炸效果
            if(len(baozha2_x)!=0):
                for i in range(len(baozha2_x)):
                    if(41>chixushijian2[i]>30):
                        screen.blit(baozha5, (baozha2_x[i], baozha2_y[i]))
                        chixushijian2[i] -= 1
                    if (30>=chixushijian2[i]>20):
                        screen.blit(baozha6, (baozha2_x[i], baozha2_y[i]))
                        chixushijian2[i] -= 1
                    if (20 >= chixushijian2[i] > 10):
                        screen.blit(baozha7, (baozha2_x[i], baozha2_y[i]))
                        chixushijian2[i] -= 1
                    if (10 >= chixushijian2[i] > 0):
                        screen.blit(baozha8, (baozha2_x[i], baozha2_y[i]))
                        chixushijian2[i]-=1

        if (d==1):                                                                      # 大敌人爆炸效果
            if(len(baozha3_x)!=0):
                for i in range(len(baozha3_x)):
                    if(61>chixushijian3[i]>50):
                        screen.blit(baozha9, (baozha3_x[i], baozha3_y[i]))
                        chixushijian3[i] -= 1
                    if (50>=chixushijian3[i]>40):
                        screen.blit(baozha10, (baozha3_x[i], baozha3_y[i]))
                        chixushijian3[i] -= 1
                    if (40 >= chixushijian3[i] > 30):
                        screen.blit(baozha11, (baozha3_x[i], baozha3_y[i]))
                        chixushijian3[i] -= 1
                    if (30 >= chixushijian3[i] > 20):
                        screen.blit(baozha12, (baozha3_x[i], baozha3_y[i]))
                        chixushijian3[i]-=1
                    if (20 >= chixushijian3[i] > 10):
                        screen.blit(baozha13, (baozha3_x[i], baozha3_y[i]))
                        chixushijian3[i]-=1
                    if (10 >= chixushijian3[i] > 0):
                        screen.blit(baozha14, (baozha3_x[i], baozha3_y[i]))
                        chixushijian3[i]-=1

        defen1 = font.render(str(score), True, PURPLE_COLOR)
        screen.blit(defen1, (80, 10))
        for i in range(len(enemy_y)):                              #小敌人飞行
            if(enemy_x[i]+e_rect.width>600 or enemy_x[i]-e_rect.width<0):
                enemy_x_speed[i]=-enemy_x_speed[i]
            if (enemy_y[i] > 1000):
                h_blood -= 1
                enemy_y[i] = random.randint(-100, -60)
            enemy_y[i]+=enemy_y_speed[i]
            enemy_x[i]+=enemy_x_speed[i]
            screen.blit(enemy, (enemy_x[i], enemy_y[i]))

        for i in range(len(enemy1_y)):                             #中敌人飞行
            if(enemy1_x[i]+e_rect1.width>600 or enemy1_x[i]-e_rect1.width<0):
                enemy1_x_speed[i]=-enemy1_x_speed[i]
            if(enemy1_y[i]>1000):
                h_blood-=1
                enemy1_y[i]=random.randint(-100,-60)
            enemy1_y[i]+=enemy1_y_speed[i]
            enemy1_x[i]+=enemy1_x_speed[i]
            screen.blit(enemy1, (enemy1_x[i], enemy1_y[i]))


        for i in range(len(enemy2_y)):                            #大敌人飞行
            if(enemy2_x[i]+e_rect2.width>600 or enemy2_x[i]-e_rect2.width<0):
                enemy2_x_speed[i]=-enemy2_x_speed[i]
            if (enemy2_y[i] > 1000):
                h_blood -= 1
                enemy2_y[i] = random.randint(-250, -150)

            enemy2_y[i]+=enemy2_y_speed[i]
            enemy2_x[i]+=enemy2_x_speed[i]
            screen.blit(enemy2, (enemy2_x[i], enemy2_y[i]))

        for i in range(len(enemy1_x)):                                 #中敌人血量显示
            pygame.draw.line(screen,PURPLE_COLOR,(enemy1_x[i],enemy1_y[i]+e_height1+2),
                             (enemy1_x[i]+blood_enemy1[i]*23,
                            enemy1_y[i]+e_height1+2),5)
            pygame.draw.line(screen,RED_COLOR,(enemy1_x[i]+3*23, enemy1_y[i]+e_height1+2),
                             (enemy1_x[i]+3*23 - (3-blood_enemy1[i])*23,
                            enemy1_y[i]+e_height1+2),5)

        for i in range(len(enemy2_x)):                                 #大敌人血量显示
            pygame.draw.line(screen, PURPLE_COLOR, (enemy2_x[i], enemy2_y[i] + e_height2 + 2),
                             (enemy2_x[i] + blood_enemy2[i] * 23,
                              enemy2_y[i] + e_height2 + 2), 5)
            pygame.draw.line(screen, RED_COLOR, (enemy2_x[i] + 5 * 23, enemy2_y[i] + e_height2 + 2),
                             (enemy2_x[i] + 5 * 23 - (5 - blood_enemy2[i]) * 23,
                              enemy2_y[i] + e_height2 + 2), 5)

        pygame.draw.line(screen, PURPLE_COLOR, (hx-55, hy + h_height-60),    #自己血量
                         (hx-55 + h_blood * 23,
                          hy + h_height-60), 5)
        pygame.draw.line(screen, RED_COLOR, (hx-55 + 5 * 23, hy + h_height-60),
                         (hx-55 + 5 * 23 - (5 - h_blood) * 23,
                          hy + h_height -60), 5)

        if(len(enemy_x)==0 and len(enemy1_x)==0 and len(enemy2_x)==0):           #游戏结束条件—击杀全部
            screen.blit(tuichu,(tuichu_x,tuichu_y))
            end1 = font.render('Penta Kill! Congratuiation!', True, PURPLE_COLOR)
            screen.blit(end1, (tuichu_x-80, tuichu_y + 30))
            if (mouse_x > tuichu_x and mouse_x < tuichu_x + tuichu_rect.width and
                    mouse_y > tuichu_y and mouse_y < tuichu_y + tuichu_rect.height):
                if(click==1):
                    exit()

        if(h_blood<=0):
            while(True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                click, b, c = pygame.mouse.get_pressed()
                screen.blit(tuichu, (tuichu_x, tuichu_y))
                end1 = font.render('Try More! You Will Win Next Time  ', True, PURPLE_COLOR)
                screen.blit(end1, (tuichu_x - 110, tuichu_y + 30))
                if (mouse_x > tuichu_x and mouse_x < tuichu_x + tuichu_rect.width and
                        mouse_y > tuichu_y and mouse_y < tuichu_y + tuichu_rect.height):
                    if (click == 1):
                        exit()
                pygame.display.update()
        screen.blit(hero,(hx-h_width/2,hy-h_height/2))

        pygame.display.update()
    pygame.display.update()