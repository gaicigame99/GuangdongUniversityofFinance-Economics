import pygame
import random
import time
pygame.init()

pygame.mixer.init()
bg_music = pygame.mixer.Sound("game_music.ogg")
bg_music.play()

screen = pygame.display.set_mode((600, 600))
# bg = pygame.transform.scale(pygame.image.load("xingkong.jpg"), (600, 600))
bg = pygame.transform.scale(pygame.image.load("lvse.jpg"), (600, 600))
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)
jiemian = pygame.transform.scale(pygame.image.load("jiemian.jpg"), (600, 600))
button1 = pygame.image.load("1.png")
button2 = pygame.image.load("3.png")
button3 = pygame.image.load("2.png")
over = pygame.transform.scale(pygame.image.load("over.jpg"), (600, 600))
suspend_button = pygame.image.load("zanting.png")
continue_button = pygame.image.load("jixu.png")
shengli = pygame.image.load("shengli.jpg")
nandu1 = pygame.image.load("初级难度.png")
nandu2 = pygame.image.load("中级难度 .png")
nandu3 = pygame.image.load("困难难度.png")


score = 0

# 食物点
r_x =random.randint(105,495)
r_y = random.randint(105,495)

time1 = 0
time2 = 1

# 初始化蛇位置与速度
speed  = 2
ls_x = []
ls_y = []
lx=[220,210,200]
ly=[300,300,300]


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




class interface(object):
    def __init__(self, screen, fengmian):
        self.screen = screen
        self.fengmian = fengmian
        self.x = 0
        self.y = 0
        self.rect = self.fengmian.get_rect()

    def show(self):
        self.screen.blit(self.fengmian, (self.x, self.y))

    def move(self):
        if self.y > -self.rect.height:
            self.y -= 3


jiemian = interface(screen, jiemian)

#功能键
#暂停变量及按钮
suspend = False
suspend_button_rect = suspend_button.get_rect()



xuanze_nandu = False
start_game = False
move_jiemian = False
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==273 and ls_y[0]!= speed  :#按键进行方向改变并且不可为反方向
                ls_y[0] = -speed
                ls_x[0] = 0
                isfangxiang = True
            if event.key ==274 and ls_y[0]!=-speed  :
                ls_y[0] = speed
                ls_x[0] = 0
                isfangxiang = True
            if event.key == 275 and ls_x[0]!=-speed :
                ls_y[0] = 0
                ls_x[0] = speed
                isfangxiang = True
            if event.key == 276 and ls_x[0]!=speed :
                ls_y[0] = 0
                ls_x[0] = -speed
                isfangxiang = True
            if isfangxiang == True:
                ji_x.append(lx[0])
                ji_y.append(ly[0])
                ji_sx.append(ls_x[0])
                ji_sy.append(ls_y[0])
                isfangxiang = False
    # 判断蛇身的点坐标是否与改变方向点坐标相同及改变方向
    for i in range(len(lx)):
        for j in range(len(ji_x)):
            if lx[i] == ji_x[j] and ly[i] == ji_y[j]:
                ls_x[i] = ji_sx[j]
                ls_y[i] = ji_sy[j]
        # 去除改变方向点
    for i in range(len(ji_x)):
        if lx[len(lx) - 1] == ji_x[i] and ly[len(lx) - 1] == ji_y[i]:
            ji_x.pop(i)
            ji_y.pop(i)
            ji_sx.pop(i)
            ji_sy.pop(i)
            break



    #开始界面
    if start_game == False:

        screen.blit(bg, (0, 0))
        jiemian.show()
        screen.blit(button1, (80, 130))
        screen.blit(button2, (80, 230))
        screen.blit(button3, (100, 330))

        #获取点坐标及点击鼠标
        a, b, c = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        # print(x,y)

        #退出游戏按钮
        if 220 < x <360 and 480 < y < 520 and a:
            exit()

        #难度选择按钮
        if 220<x<360 and 383<y<417 and a:
            xuanze_nandu = True
        if xuanze_nandu:
            screen.blit(nandu1,(230,200))
            screen.blit(nandu2, (250, 240))
            screen.blit(nandu3, (250, 300))
            if  395<x<482 and 333<y<361 and a:
                speed = 2
                xuanze_nandu = False
            if 395 < x < 482 and 385 < y < 411 and a:
                speed = 5
                xuanze_nandu = False
            if 395 < x < 482 and 437 < y < 459 and a:
                speed = 10
                xuanze_nandu = False

        #开始游戏按钮
        if 220 < x < 360 and 276 < y < 310 and a:
            ls_x = [speed, speed, speed]
            ls_y = [0, 0, 0]
            move_jiemian = True
        if move_jiemian:
            jiemian.move()
            if jiemian.y <= -jiemian.rect.height:
                start_game = True

    #游戏开始
    if start_game:
        a, b, c = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        time2 = time.time()

        if time2 - time1 >= 0.02:

            #显示图标
            screen.blit(bg, (0, 0))
            #食物
            pygame.draw.circle(screen, (255, 255, 255), (r_x, r_y), 5)
            #边界
            pygame.draw.line(screen, (255, 255, 255), (100, 100), (100, 500))
            pygame.draw.line(screen, (255, 255, 255), (500, 100), (500, 500))
            pygame.draw.line(screen, (255, 255, 255), (100, 100), (500, 100))
            pygame.draw.line(screen, (255, 255, 255), (100, 500), (500, 500))
            #分数+速度
            screen.blit(font.render("score:" + str(score), True, (255, 255, 255)), (0, 0))
            screen.blit(font.render("speed:" + str(speed), True, (255, 255, 255)), (0, 40))

            # 暂停与开始按钮
            if suspend == False:
                screen.blit(suspend_button, (30, 520))
                # a, b, c = pygame.mouse.get_pressed()
                # x, y = pygame.mouse.get_pos()
                if 30 < x < 30 + suspend_button_rect.width and 520 < y < 520 + suspend_button_rect.height and a:
                    suspend = True
            else:
                screen.blit(continue_button, (30, 520))
                if 30 < x < 30 + suspend_button_rect.width and 520 < y < 520 + suspend_button_rect.height and a:
                    suspend = False
            # x+=s_x
            # y+=s_y
            #坐标改变即移动
            if suspend == False:
                for i in range(len(ls_x)):
                    lx[i] += ls_x[i]
                    ly[i] += ls_y[i]

            for i in range(len(lx)):
                pygame.draw.circle(screen, (255, 255, 255), (lx[i], ly[i]), 5)
            time1 = time.time()
            if pengzhuangceshi(lx[0], r_x, ly[0], r_y):
                r_x = random.randint(105, 495)
                r_y = random.randint(105, 495)
                score += 1
                if ls_x[len(lx) - 1] == speed :  # 根据最后一个点的速度方向增加新的点的速度方向
                    lx.append(lx[len(lx) - 1] - 10)
                    ly.append(ly[len(ly) - 1])
                    ls_x.append(ls_x[len(ls_x) - 1])
                    ls_y.append(ls_y[len(ls_y) - 1])
                if ls_x[len(lx) - 1] == -speed :
                    lx.append(lx[len(lx) - 1] + 10)
                    ly.append(ly[len(ly) - 1])
                    ls_x.append(ls_x[len(ls_x) - 1])
                    ls_y.append(ls_y[len(ls_y) - 1])
                if ls_y[len(ly) - 1] == speed :
                    lx.append(lx[len(lx) - 1])
                    ly.append(ly[len(ly) - 1] - 10)
                    ls_x.append(ls_x[len(ls_x) - 1])
                    ls_y.append(ls_y[len(ls_y) - 1])
                if ls_y[len(ly) - 1] == -speed :
                    lx.append(lx[len(lx) - 1])
                    ly.append(ly[len(ly) - 1] + 10)
                    ls_x.append(ls_x[len(ls_x) - 1])
                    ls_y.append(ls_y[len(ls_y) - 1])
        # 游戏失败结束判断
        if 495 < lx[0] or lx[0] < 105 or 495 < ly[0] or ly[0] < 105:
            game_over = True

        for i in range(len(lx)):
            if i != 0 and i != 1:  # 第一个点与第二个点不会发现碰撞所以无需判断
                if pengzhuangceshi(lx[0], lx[i], ly[0], ly[i]):
                    game_over =True

    if game_over:
        screen.blit(over, (0, 0))
        screen.blit(font.render("score:" + str(score), True, (25, 25, 25)), (250, 100))
        screen.blit(button3, (100, 330))
        # a, b, c = pygame.mouse.get_pressed()
        # x, y = pygame.mouse.get_pos()
        if 220 < x < 360 and 480 < y < 520 and a:  # 结束游戏
            exit()

    #游戏胜利结束判断
    if suspend ==2:
        if score > 100:
            screen.blit("shengli",(0,0))
            suspend = True
    elif suspend == 5:
        if score > 200:
            screen.blit("shengli", (0, 0))
            suspend = True
    elif suspend ==10:
        if score > 300:
            screen.blit("shengli", (0, 0))
            suspend = True



    pygame.display.update()