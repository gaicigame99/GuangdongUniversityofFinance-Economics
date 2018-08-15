import pygame
import random
pygame.init()
pygame.mixer.init()
back_music=pygame.mixer.Sound("game_music.ogg")
back_music.play()
screen=pygame.display.set_mode((495,800))
hero=pygame.image.load("hero1.png")
background=pygame.image.load("background.png")
background=pygame.transform.scale(background,(495,800))
move_list={}
mv_bg=pygame.image.load("name.png")
# mv_bg=pygame.transform.scale(mv_bg,(495,800))
bgx=50
bgy=100
move_list["背景位置"]=[bgx,bgy]

btn_1=pygame.image.load("button_nor.png")
btn_1=pygame.transform.scale(btn_1,(247,600))
btn_1_rect=btn_1.get_rect()
btn_1x=124
btn_1y=480
move_list["按钮1位置"]=[btn_1x,btn_1y]


btn_2=pygame.image.load("button_p.png")
btn_2=pygame.transform.scale(btn_2,(247,80))
btn_2_rect=btn_2.get_rect()
btn_2x=124
btn_2y=480
move_list["按钮2位置"]=[btn_2x,btn_2y]

font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",30)
start_text=font.render("开始游戏",True,(0,0,0,150))
stx=63+124
sty=25+480
move_list["文字位置"]=[stx,sty]


bullet=pygame.image.load("bullet.png")
enemy=pygame.image.load("enemy1.png")

h_rect=hero.get_rect()
b_rect=bullet.get_rect()
e_rect=enemy.get_rect()

hx=100
hy=100

b_v=20
time=b_v
game_start=0
game_start_time=150


b_x=[]
b_y =[]
b_speed=2


e_x=[]
e_y=[]
# e_x_speed=[]
e_y_speed=1

speedx=0
speedy=0


def collection(b_x,b_y,e_x,e_y,b_rect,e_rect):
    if b_x+b_rect.width>e_x and \
            b_x<e_x+e_rect.width and \
            b_y<e_y+e_rect.height:
        print("发生碰撞")
        return True
    else:
        return False

for i in range(3):
    e_x.append(random.randint(0,495))
    e_y.append(random.randint(-200,0))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(background, (0, 0))
    screen.blit(mv_bg, (move_list["背景位置"][0], move_list["背景位置"][1]))
    a,b,c=pygame.mouse.get_pressed()
    hx,hy=pygame.mouse.get_pos()
    if hx>btn_1x and hx<btn_1x+btn_1_rect.width and hy>btn_1y and hy<btn_1y+btn_1_rect.height and a:
        screen.blit(btn_1 ,(move_list["按钮1位置"][0],move_list["按钮1位置"][1]))
        speedx=0
        speedy=-30
        game_start=1
    else:
        screen.blit(btn_2,(move_list["按钮2位置"][0],move_list["按钮2位置"][1]))
    for i in move_list:
        move_list[i][0]+=speedx
        move_list[i][0]+=speedy

    screen.blit(start_text,(move_list["文字位置"][0],move_list["文字位置"][1]))
    if game_start:
        game_start_time-=1

    if game_start and game_start_time<0:
        screen.blit(enemy,(e_x[j],e_y[j]))
        if e_x[j]<800:
            e_y[j]+=1
        else:
            e_x=random.randint(0,495-e_rect.width)
            e_y=-e_rect.height


    screen.blit(hero,(hx-h_rect.height/2+2,hy-h_rect.height/2))
    if time:
        time -= 1
    else:
        b_x.append(hx - b_rect.width / 2)
        b_y.append(hy - h_rect.height / 2 - b_rect.height)
        time = b_v


        for i in b_y:
            index=b_y.index(i)
            if i <0:
                b_y.pop(index)
                b_x.pop(index)
    for i in range(len(b_x)):
        screen.blit(bullet,(b_x[i],b_y[i]))
        b_y[i]-=b_speed
        # print(b_x[i],b_y[i])
        for j in range(3):
            screen.blit(enemy, (e_x[j], e_y[j]))
            e_y[j] += e_y_speed
            # print(e_x[j],e_y[j])
        if collection(b_x[i],b_y[i],e_x[j],e_y[j],b_rect,e_rect):
            e_x[j]=random.randint(0,495-e_rect.width)
            e_y[j]=-200
            b_y[i]=-100
    pygame.display.update()