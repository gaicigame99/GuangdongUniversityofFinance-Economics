import pygame
from math import *
import random
pygame.init()
xbg = 800
ybg = 600
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 50)
fon = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 40)
fon_score = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
blue_button = pygame.image.load("bblue_button.png")
blue_button = pygame.transform.scale(blue_button, (240, 100))
green_button = pygame.image.load("bgreen_button.png")
green_button = pygame.transform.scale(green_button, (240, 100))
tui_blue_button = pygame.image.load("blue_button.png")
tui_blue_button = pygame.transform.scale(tui_blue_button, (240, 100))
tui_green_button = pygame.image.load("green_button.png")
tui_green_button = pygame.transform.scale(tui_green_button, (240, 100))
dapao = pygame.image.load("dapao.png")
jie_bg = pygame.image.load("fengmian2.jpg")
jie_bg = pygame.transform.scale(jie_bg, (xbg, ybg))
dapao = pygame.image.load("dapao.png")
screen = pygame.display.set_mode((xbg, ybg))
bg = pygame.image.load("bg1.jpg")
bg = pygame.transform.scale(bg, (xbg, ybg))
color_pt = (12, 122, 233)
speed = [0, 0]


class ball(object):
    def __init__(self, _screen):
        self.screen = _screen
        self.image = []
        self.width = 30
        self.height = 30
        wid = self.width
        hei = self.height
        # 深度优先搜索辅助列表
        self.dis = [[-wid//2, -hei], [-wid, 0], [-wid//2, hei], [wid//2, -hei], [wid, 0], [wid//2, hei]]
        self.vis = []
        self.x = 0
        self.y = 0
        self.color = 1
        self.balls = []  # 在屏幕上面要被击的球列表
        for i in range(xbg):
            self.vis.append([])
            for j in range(ybg):
                self.vis[i].append(-1)
        for i in range(5):
            ball_t = pygame.image.load(r"ball{}.png".format(i+1))
            ball_t = pygame.transform.scale(ball_t, (self.width, self.height))
            self.image.append([ball_t, i])

    def ball_ad(self,_screen, hang):
        xt = 0
        cuo_kai = 1
        yt = 0
        for i in range(0, hang):
            while xt + self.width <= xbg:
                t = self.image[random.randint(0, 4)]
                self.balls.append([t[0], xt, yt])
                self.vis[xt][yt] = t[1]
                xt += self.width
            if cuo_kai == 1:
                xt = 15
            else:
                xt = 0
            cuo_kai = -cuo_kai
            yt += self.height

    def ball_show(self, _screen):
        for i in range(len(self.balls)):
            if self.vis[int(self.balls[i][1])][int(self.balls[i][2])] >= 0:
                _screen.blit(self.balls[i][0], (self.balls[i][1], self.balls[i][2]))


def mov(_ball, _x, _y):
    if _ball.y <= 0:
        _y = -_y
    _ball.y += _y
    if _ball.x <= 0 or _ball.x >= xbg-30:
        _x = -_x
    _ball.x += _x
    return _x, _y


def show_main(_screen, choice):  #关卡主界面
    y1 = 200
    y2 = 300
    y3 = 450
    ti_3 = "退出游戏"
    flag = 0
    if choice == 1:
        _screen.blit(jie_bg, (0, 0))
        ti_1 = "欢迎进入泡泡龙娱乐场"
        ti_2 = "进入游戏"
    elif choice == 2:
        _screen.blit(jie_bg, (0, 0))
        ti_1 = "      挑战失败      "
        ti_2 = "继续游戏"
    elif choice == 3:
        _screen.blit(jie_bg, (0, 0))
        ti_1 = "        挑战成功     "
        ti_2 = "继续游戏"
    start_text0 = fon.render(ti_1, True, (82, 71, 222))
    _screen.blit(start_text0, (200, y1))
    start_text1 = font.render(ti_2, True, (102, 62, 112))
    start_text2 = font.render(ti_3, True, (222, 23, 233))
    while True:
        _screen.blit(green_button, (300, y2))
        _screen.blit(blue_button, (300, y3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        x, y, z = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if 300 <= mx <= 540 and y2 <= my <= y2+100:
            _screen.blit(blue_button, (300, y2))
            if x:
                break
        if 300 <= mx <= 540 and y3 <= my <= y3+100:
            _screen.blit(green_button, (300, y3))
            if x:
                flag = 1
                break
        _screen.blit(start_text1, (310, y2+20))
        _screen.blit(start_text2, (310, y3 + 20))
        pygame.display.update()
    score = 0
    return flag, score


def dfs(_ball, _x, _y):   #深度优先搜索，消去相连的同颜色的球
    a = [[_x, _y]]
    ans = 0
    tem_list = []
    while len(a) > 0:
        ans += 1
        tem = a.pop(0) #模拟队列进行深搜
        tem_list.append([tem[0], tem[1]])
        for i in range(6):
            nextx = int(tem[0]+_ball.dis[i][0])
            nexty = int(tem[1]+_ball.dis[i][1])
            if 0 <= nextx <= xbg and 0 <= nexty < ybg and _ball.vis[nextx][nexty] == _ball.color and\
            [nextx, nexty] not in tem_list:
                a.append([nextx, nexty])
    return _ball, ans, tem_list


def stock_judge(_ball, xx, yy):  #碰撞检测
    dd = _ball.width*_ball.width+10  #视觉提升
    ans = 0
    xx = int(xx)
    yy = int(yy)
    flag = 0
    t_list = []
    for i in range(len(_ball.balls)):
        if _ball.vis[_ball.balls[i][1]][_ball.balls[i][2]] >= 0:
            td = ((xx-_ball.balls[i][1])**2+(yy-_ball.balls[i][2]))**2
            if td <= dd and 0 <= xx < xbg and 0 <= yy < ybg:
                flag = 1
                if _ball.vis[_ball.balls[i][1]][_ball.balls[i][2]] == _ball.color:
                    _ball, ans, t_list = dfs(_ball, _ball.balls[i][1], _ball.balls[i][2])
                if ans <= 1:
                    for k in range(6):
                        now_x = int(_ball.balls[i][1] + _ball.dis[k][0])
                        now_y = int(_ball.balls[i][2] + _ball.dis[k][1])
                        if 0 <= now_x < xbg and 0 <= now_y < ybg and _ball.vis[now_x][now_y] == -1:
                            _ball.balls.append([_ball.image[_ball.color][0], now_x, now_y])
                            _ball.vis[now_x][now_y] = _ball.color
                            break
                else:
                    _ball.y = ybg + _ball.width
                    for k in range(len(t_list)):
                        _ball.vis[t_list[k][0]][t_list[k][1]] = -1
                break
    return _ball, ans, flag


judge, score = show_main(screen, 1)
if judge == 1:
    exit()
ballx = ball(screen)
start = 0
now_ball = random.randint(0, 4)
next_ball = now_ball
ballx.ball_ad(screen, 6)
agree_text = fon_score.render("酷毙了！", True, (122, 255, 32))
ans = score
while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            exit()
    screen.blit(bg, (0, 0))
    ballx.ball_show(screen)
    if ballx.y > ybg:
        start = 0
    mx, my = pygame.mouse.get_pos()
    pygame.draw.line(screen, color_pt, (400, 600), ((mx+400)//2, (my+600)//2), 20)
    x, y, z = pygame.mouse.get_pressed()
    if z and start == 0:   #右键点击击球
        ballx.x = (mx + 400) // 2-12
        ballx.y = (my + 600) // 2-10
        start = 1
        speed[1] = (my-600)/200  #y方向的速度
        speed[0] = (mx-400)/200  #x方向的速度
        now = next_ball
        ballx.color = now
        print("[", now, "]")
        next_ball = int(random.randint(0, 4))
    screen.blit(ballx.image[next_ball][0], ((mx + 400) // 2 - 12, (my + 600) // 2 - 10))  # 显示准备要击的球
    if start == 1:
        ballx, ans, k = stock_judge(ballx, ballx.x, ballx.y)
        if ans >= 2:
            score += ans+1
        if k == 1:
            start = 0
    if start == 1:
        screen.blit(ballx.image[ballx.color][0], (ballx.x, ballx.y))
        speed[0], speed[1] = mov(ballx, speed[0], speed[1])
    score_text = fon_score.render("得分："+str(score), True, (122, 255, 32))
    if ans >= 4 and start == 0:
        screen.blit(agree_text, (mx, my))
    screen.blit(score_text, (xbg - 150, ybg - 50))
    screen.blit(dapao, (380, ybg - 40))
    pygame.display.update()
