import pygame
import random
import time
pygame.init()
font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",36)
screen = pygame.display.set_mode((495,800))
red = pygame.image.load(r"images\red.png")
green = pygame.image.load(r"images\green.png")
fengmian = pygame.transform.scale(pygame.image.load(r"images\fengmian.jpg"),(495,800))
bg = pygame.transform.scale(pygame.image.load(r"images\background.png"),(495,800))

star_time = 500
x=200
y=600
x_rect = green.get_rect()
mouse_x=0
mouse_y=0
star = 0
fengmian_star = 0
fengmian_x =0
fengmian_y = 0
fengmian_rect = fengmian.get_rect()




bullet = pygame.image.load(r"images\bullet-3.gif")
hero1 = pygame.image.load(r"images\hero_blowup_n3.png")
bullet2 =pygame.image.load(r"images\bullet-1.gif")



#hero的设置
hero = pygame.image.load("images\hero.gif")
hero1 = pygame.image.load(r"images\hero_blowup_n1.png")
hero2 = pygame.image.load(r"images\hero_blowup_n2.png")
hero3 = pygame.image.load(r"images\hero_blowup_n3.png")
hero4 = pygame.image.load(r"images\hero_blowup_n4.png")
hero_blow =[]
hero_blow.append(hero1)
hero_blow.append(hero2)
hero_blow.append(hero3)
hero_blow.append(hero4)
h_width = hero.get_rect().width
h_height = hero.get_rect().height
hx = 200
hy = 700
life_hero = 5
time1=0
time2=0
h_blood=5


#子弹的设置
b_speed = 3
b_v = 20
b_rect = bullet.get_rect()
b_x = []
b_y = []
b_time = b_v
zidan = bullet
list_bullet =[]
list_bullet.append(pygame.image.load(r"images\bullet-3.gif"))
list_bullet.append(pygame.image.load(r"images\bullet-1.gif"))



#物品
prop = []
#0号换枪列表
prop.append(pygame.image.load(r"images\prop_type_0.png"))

prop_rect = pygame.image.load(r"images\prop_type_0.png").get_rect()
prop_prop = []
prop_x=[]
prop_y=[]
#prop_x.append(random.randint(0,485-prop_rect.width))
#prop_y.append(-prop_rect.height)
prop_exist = True

#敌机的设置
enemy = pygame.image.load(r"images\enemy0.png")
enemy_blow = []
enemy1 = pygame.image.load(r"images\enemy0_down1.png")
enemy2 = pygame.image.load(r"images\enemy0_down3.png")
enemy3 = pygame.image.load(r"images\enemy0_down3.png")
enemy4 = pygame.image.load(r"images\enemy0_down4.png")
enemy_blow.append(enemy1)
enemy_blow.append(enemy2)
enemy_blow.append(enemy3)
enemy_blow.append(enemy4)

enemy_rect = enemy.get_rect()
e_x =0
e_y =0
le_x = []
le_y = []
for i in range(5):
    le_x.append(random.randint(0,485-enemy_rect.width))
    le_y.append(random.randint(-100,0))
lbe_x = []
lbe_y = []
lbe_time=[]


#中型敌机boss
enemy_boss =pygame.image.load(r"images\enemy1.png")
enemy_boss1 =pygame.image.load(r"images\enemy1_down1.png")
enemy_boss2 =pygame.image.load(r"images\enemy1_down2.png")
enemy_boss3 =pygame.image.load(r"images\enemy1_down3.png")
enemy_boss4 =pygame.image.load(r"images\enemy1_down4.png")
lenemy_boss = []
lenemy_boss.append(enemy_boss1)
lenemy_boss.append(enemy_boss2)
lenemy_boss.append(enemy_boss3)
lenemy_boss.append(enemy_boss4)
e_b_rect=enemy_boss.get_rect()
e_bx=235
e_by=-e_b_rect.height
e_b_blood = 0
e_bx_blast=[]
e_by_blast=[]
e_btime_blast=[]

#大型boss
e_boss = pygame.image.load(r"images/enemy2.png")
le_boss = []
le_boss.append(pygame.image.load(r"images/enemy2_down1.png"))
le_boss.append(pygame.image.load(r"images/enemy2_down2.png"))
le_boss.append(pygame.image.load(r"images/enemy2_down3.png"))
le_boss.append(pygame.image.load(r"images/enemy2_down4.png"))
le_boss.append(pygame.image.load(r"images/enemy2_down5.png"))
le_boss.append(pygame.image.load(r"images/enemy2_down6.png"))
e_boss_rect = e_boss.get_rect()
e_boss_x = 200
e_boss_y = - e_boss_rect.height
e_boss_blood = 0
e_boss_blast_x = []
e_boss_blast_y = []
e_boss_blast_time=[]



#子弹消失参数

n=0

#分数
fenshu=0

def jiancepengzhuang(a_x,a_y,a_width,a_height,b_x,b_y,b_width,b_height):
    if a_x + a_width > b_x and \
            a_x < b_x + b_width and \
            a_y < b_y + b_height and \
            a_y + a_height > b_y:
        return True
    else:
        return False

def h_blood(a_x,a_y,a_width,a_height,a_life):

    pygame.draw.line(screen,(255,0,0),(a_x,a_y+a_height+10),(a_x+a_width//5*a_life,a_y+a_height+10),2)
    pygame.draw.line(screen, (55, 55, 55), (a_x+a_width//5*a_life, a_y + a_height + 10), (a_x + a_width, a_y + a_height + 10), 2)

def e_blood(a_x,a_y,a_width,a_height,a_life):
    pygame.draw.line(screen,(255,0,0),(a_x,a_y-10),(a_x+a_width*(a_life/10),a_y-10),2)
    pygame.draw.line(screen, (55, 55, 55), (a_x+a_width*(a_life/10), a_y -10),(a_x + a_width, a_y - 10), 2),

def be_blood(a_x,a_y,a_width,a_height,a_life):
    pygame.draw.line(screen,(255,0,0),(a_x,a_y-10),(a_x+a_width*(a_life/20),a_y-10),2)
    pygame.draw.line(screen, (55, 55, 55), (a_x+a_width*(a_life/20), a_y -10),(a_x + a_width, a_y - 10), 2),

def blast(time2,time1,a_x,a_y,a_tupian):
    if 0.2 > time2 - time1 > 0.1:
        screen.blit(a_tupian[0], (a_x, a_y ))
    elif 0.3 > time2 - time1 > 0.2:
        screen.blit(a_tupian[1], (a_x , a_y ))
    elif 0.4 > time2 - time1 > 0.3:
        screen.blit(a_tupian[2], (a_x , a_y ))
    elif 1 > time2 - time1 > 0.4:
        screen.blit(a_tupian[3], (a_x , a_y ))

def be_blast(time2,time1,a_x,a_y,a_tupian):
    if 0.2 > time2 - time1 > 0.1:
        screen.blit(a_tupian[0], (a_x, a_y ))
    elif 0.3 > time2 - time1 > 0.2:
        screen.blit(a_tupian[1], (a_x , a_y ))
    elif 0.4 > time2 - time1 > 0.3:
        screen.blit(a_tupian[2], (a_x , a_y ))
    elif 0.5 > time2 - time1 > 0.4:
        screen.blit(a_tupian[3], (a_x , a_y ))
    elif 0.6 > time2 - time1 > 0.5:
        screen.blit(a_tupian[4], (a_x , a_y ))
    elif 0.7 > time2 - time1 > 0.6:
        screen.blit(a_tupian[5], (a_x , a_y ))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(bg, (0, 0))

    if star ==0:
        screen.blit(fengmian,(fengmian_x,fengmian_y))
        screen.blit(red, (x, y))
        mouse_x,mouse_y = pygame.mouse.get_pos()
        z,n,m=pygame.mouse.get_pressed()
        if fengmian_star ==1:
            y-=5
            fengmian_y -= 5
            if fengmian_y < -fengmian_rect.height:
                star = 1

        if x<mouse_x<x_rect.width+x and y<mouse_y<y+x_rect.height and z:
            screen.blit(green, (x, y))
            fengmian_star = 1

    if star ==1:
        if life_hero:
            if b_time:
                b_time -= 1
            else:
                b_x.append(hx - b_rect.width / 2 + 2)
                b_y.append(hy - h_height / 2 - b_rect.height)
                b_time = b_v

        # 子弹出现及消失以及敌机消失
        for i in range(len(b_x)):
            # screen.blit(bullet,(b_x[i],b_y[i]))
            screen.blit(zidan, (b_x[i], b_y[i]))
            b_y[i] -= b_speed
            if b_y[i] < 0:
                n = 0
                b_x.pop(i)
                b_y.pop(i)
                break
            # 小敌机
            for j in range(len(le_x)):
                if le_x[j] < b_x[i] < le_x[j] + enemy_rect.width and le_y[j] - enemy_rect.height < b_y[i] < le_y[j] and \
                        le_y[j] > 0:
                    lbe_x.append(le_x[j])
                    lbe_y.append(le_y[j])
                    lbe_time.append(time.time())
                    le_y[j] = -100
                    le_x[j] = random.randint(0, 495 - enemy_rect.width)
                    b_x.pop(i)
                    b_y.pop(i)
                    n = 1
                    fenshu += 1
                    break
            if n == 1:
                n = 0
                break
            # 中型boss
            if jiancepengzhuang(b_x[i], b_y[i], b_rect.width, b_rect.height, e_bx, e_by, e_b_rect.width,
                                e_b_rect.height):
                b_x.pop(i)
                b_y.pop(i)
                e_b_blood -= 1
                if e_b_blood <= 0:
                    prop_exist = True
                    fenshu += 5
                    e_bx_blast.append(e_bx)
                    e_by_blast.append(e_by)
                    e_btime_blast.append(time.time())
                break
            # 大型boss碰撞
            if jiancepengzhuang(b_x[i], b_y[i], b_rect.width, b_rect.height, e_boss_x, e_boss_y, e_boss_rect.width,
                                e_boss_rect.height):
                b_x.pop(i)
                b_y.pop(i)
                e_boss_blood -= 1
                if e_boss_blood <= 0:
                    fenshu += 10
                    e_boss_blast_x.append(e_boss_x)
                    e_boss_blast_y.append(e_boss_y)
                    e_boss_blast_time.append(time.time())
                break
        # 小敌机爆炸设置
        if len(lbe_y):
            for i in range(len(lbe_y)):
                # if 0.2 > time2 - lbe_time[i] > 0.1:
                #     screen.blit(enemy1, (lbe_x[i] , lbe_y[i]))
                # elif 0.3 > time2 - lbe_time[i] > 0.2:
                #     screen.blit(enemy2, (lbe_x[i], lbe_y[i] ))
                # elif 0.4 > time2 - lbe_time[i] > 0.3:
                #     screen.blit(enemy3, (lbe_x[i] , lbe_y[i]))
                # elif 1 > time2 - lbe_time[i] > 0.4:
                #     screen.blit(enemy4, (lbe_x[i], lbe_y[i] ))
                blast(time2, lbe_time[i], lbe_x[i], lbe_y[i], enemy_blow)
                if time2 - lbe_time[i] > 1:
                    lbe_y.pop(i)
                    lbe_x.pop(i)
                    lbe_time.pop(i)
                    break
        # 中型boss出现
        if fenshu > 0 and fenshu % 15 == 0:
            e_b_blood = 10
        if e_b_blood > 0:
            screen.blit(enemy_boss, (e_bx, e_by))
            e_by += 1
            e_blood(e_bx, e_by, e_b_rect.width, e_b_rect.height, e_b_blood)
        else:
            e_by = -e_b_rect.height
        if len(e_bx_blast):
            for i in range(len(e_bx_blast)):
                blast(time2, e_btime_blast[i], e_bx_blast[i], e_by_blast[i], enemy_blow)
                if time2 - e_btime_blast[i] > 1:
                    e_by_blast.pop(i)
                    e_bx_blast.pop(i)
                    e_btime_blast.pop(i)
        # 大型boss出现
        if fenshu > 0 and fenshu % 40 == 0:
            e_boss_blood = 20
        if e_boss_blood > 0:
            screen.blit(e_boss, (e_boss_x, e_boss_y))
            e_boss_y += 1
            be_blood(e_boss_x, e_boss_y, e_boss_rect.width, e_boss_rect.height, e_boss_blood)
        else:
            e_boss_y = -e_boss_rect.height
        if len(e_boss_blast_x):
            print("b")
            for i in range(len(e_boss_blast_x)):
                print("a")
                be_blast(time2, e_boss_blast_time[i], e_boss_blast_x[i], e_boss_blast_y[i], le_boss)
                if time2 - e_boss_blast_time[i] > 1:
                    e_boss_blast_x.pop(i)
                    e_boss_blast_y.pop(i)
                    e_boss_blast_time.pop(i)
        # hero与敌机碰撞
        for j in range(len(le_x)):
            if jiancepengzhuang(le_x[j], le_y[j], enemy_rect.width, enemy_rect.height, hx, hy, h_width, h_height):
                lbe_x.append(le_x[j])
                lbe_y.append(le_y[j])
                lbe_time.append(time.time())
                le_y[j] = -100
                le_x[j] = random.randint(0, 495 - enemy_rect.width)
                if life_hero:
                    life_hero -= 1
                    if life_hero == 0:
                        time1 = time.time()
        # hero爆炸
        time2 = time.time()
        if life_hero == 0:
            blast(time2, time1, hx - h_width / 2, hy - h_height / 2, hero_blow)
        # hero移动设置
        if life_hero:
            hx, hy = pygame.mouse.get_pos()
            screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))
            h_blood(hx - h_width / 2, hy - h_height / 2, h_width, h_height, life_hero)
        # 出现敌机
        for i in range(5):
            screen.blit(enemy, (le_x[i], le_y[i]))
            le_y[i] += 1
            if le_y[i] > 800:
                le_y[i] = -100


        #物品
        if prop_exist:
            prop_prop.append(prop[random.randint(0,len(prop)-1)])
            prop_x.append(random.randint(0,485-prop_rect.width))
            prop_y.append(-prop_rect.height)
            prop_exist = False
            # screen.blit(prop, (prop_x, prop_y))
            # prop_y += 1
            # if jiancepengzhuang(prop_x, prop_y, prop_rect.width, prop_rect.height, hx, hy, h_width, h_height):
            #     zidan = bullet2
            #     prop_y = 900


        if len(prop_prop):
            for i in range(len(prop_prop)):
                screen.blit(prop_prop[i], (prop_x[i], prop_y[i]))
                prop_y[i]+=1
                if jiancepengzhuang(prop_x[i], prop_y[i], prop_rect.width, prop_rect.height, hx, hy, h_width, h_height):

                    #zidan = list_bullet[random.randint(0,len(list_bullet)-1)]
                    zidan=bullet2
                    prop_y.pop(i)
                    prop_x.pop(i)
                    prop_prop.pop(i)
                    break


        # print(life_hero)
        # e_x+=1
        # e_y+=1
        print(life_hero)

    screen.blit(font.render(str(fenshu), True, (255, 255, 255)), (0, 0))
    pygame.display.update()


