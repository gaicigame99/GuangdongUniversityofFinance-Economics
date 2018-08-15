import numpy
import pygame
import time
import random
pygame.init()


# 算出棋盘中所有有价值的点
def haveValuePoints(vis):

    points = []

    for x in range(15):
        for y in range(15):
            list1 = []  # 存横方向
            list2 = []  # 存竖方向
            list3 = []  # 正对角线
            list4 = []  # 副对角线
            if vis[x][y] == 0:
                for tmp in range(9):
                    i = x + tmp - 4
                    j = y + tmp - 4
                    if i < 0 or i > 14:
                        list1.append(-1)
                    else:
                        list1.append(vis[i][y])
                    if j < 0 or j > 14:
                        list2.append(-1)
                    else:
                        list2.append(vis[x][j])
                    if i < 0 or j < 0 or i > 14 or j > 14:
                        list3.append(-1)
                    else:
                        list3.append(vis[i][j])
                    k = y - tmp + 4
                    if i < 0 or k < 0 or i > 14 or k > 14:
                        list4.append(-1)
                    else:
                        list4.append(vis[i][k])

                playerValue = value_point(2, 1, list1, list2, list3, list4)
                enemyValue = value_point(1, 2, list1, list2, list3, list4)
                # print("人：%d,电脑：%d"%(playerValue, enemyValue))
                if playerValue >= 100000:
                    playerValue -= 5000
                elif playerValue >= 10000:
                    playerValue -= 3000
                elif playerValue >= 2000:
                    playerValue -= 250
                elif playerValue >= 1500:
                    playerValue -= 200
                elif playerValue >= 99:
                    playerValue -= 10
                elif playerValue >= 5:
                    playerValue -= 1
                value = playerValue + enemyValue
                if value > 0:
                    # print("人：%d,电脑：%d" % (playerValue, enemyValue))
                    points.append([x, y, value])
    return points


# 算出每个点的价值
def value_point(player, enemy, list1, list2, list3, list4):

    flag = 0
    flag += willbefive(player, list1)
    flag += willbefive(player, list2)
    flag += willbefive(player, list3)
    flag += willbefive(player, list4)
    flag += willbealive4(player, list1)
    flag += willbealive4(player, list2)
    flag += willbealive4(player, list3)
    flag += willbealive4(player, list4)
    flag += willbesleep4(player, enemy, list1)
    flag += willbesleep4(player, enemy, list2)
    flag += willbesleep4(player, enemy, list3)
    flag += willbesleep4(player, enemy, list4)
    flag += willbealive3(player, list1)
    flag += willbealive3(player, list2)
    flag += willbealive3(player, list3)
    flag += willbealive3(player, list4)
    flag += willbesleep3(player, enemy, list1)
    flag += willbesleep3(player, enemy, list2)
    flag += willbesleep3(player, enemy, list3)
    flag += willbesleep3(player, enemy, list4)
    flag += willbealive2(player, enemy, list1)
    flag += willbealive2(player, enemy, list2)
    flag += willbealive2(player, enemy, list3)
    flag += willbealive2(player, enemy, list4)
    flag += willbesleep2(player, enemy, list1)
    flag += willbesleep2(player, enemy, list2)
    flag += willbesleep2(player, enemy, list3)
    flag += willbesleep2(player, enemy, list4)
    return flag


# 下在这个点将会得到连五
def willbefive(player, checklist):
    if checklist[0] == player and checklist[1] == player and \
            checklist[2] == player and checklist[3] == player:
        return 100000
    elif checklist[5] == player and checklist[6] == player and \
            checklist[7] == player and checklist[8] == player:
        return 100000
    elif checklist[2] == player and checklist[3] == player and \
            checklist[5] == player and checklist[6] == player:
        return 100000
    elif checklist[1] == player and checklist[2] == player and \
            checklist[3] == player and checklist[5] == player:
        return 100000
    elif checklist[3] == player and checklist[5] == player and \
            checklist[6] == player and checklist[7] == player:
        return 100000
    else:
        return 0


# 下在这个点将会形成活四
def willbealive4(player, checklist):
    if checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == player and checklist[3] == player \
            and checklist[5] == 0:
        return 10000
    elif checklist[3] == 0 and checklist[5] == player and \
            checklist[6] == player and checklist[7] == player \
            and checklist[8] == 0:
        return 10000
    elif checklist[1] == 0 and checklist[2] == player and \
            checklist[3] == player and checklist[5] == player \
            and checklist[6] == 0:
        return 10000
    elif checklist[2] == 0 and checklist[3] == player and \
            checklist[5] == player and checklist[6] == player \
            and checklist[7] == 0:
        return 10000
    else:
        return 0


# 下在这个点会形成眠四
def willbesleep4(player, enemy, checklist):
    if checklist[0] == enemy and checklist[1] == player and \
            checklist[2] == player and checklist[3] == player \
            and checklist[5] == 0:
        return 1700
    elif checklist[1] == enemy and checklist[2] == player and \
            checklist[3] == player and checklist[5] == player \
            and checklist[6] == 0:
        return 1700
    elif checklist[2] == enemy and checklist[3] == player and \
            checklist[5] == player and checklist[6] == player \
            and checklist[7] == 0:
        return 1700
    elif checklist[3] == enemy and checklist[5] == player and \
            checklist[6] == player and checklist[7] == player \
            and checklist[8] == 0:
        return 1700
    elif checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == player and checklist[3] == player \
            and checklist[5] == enemy:
        return 1700
    elif checklist[1] == 0 and checklist[2] == player and \
            checklist[3] == player and checklist[5] == player \
            and checklist[6] == enemy:
        return 1700
    elif checklist[2] == 0 and checklist[3] == player and \
            checklist[5] == player and checklist[6] == player \
            and checklist[7] == enemy:
        return 1700
    elif checklist[3] == 0 and checklist[5] == player and \
            checklist[6] == player and checklist[7] == player \
            and checklist[8] == enemy:
        return 1700
    else:
        return 0


# 下在这个点会形成活三
def willbealive3(player, checklist):
    if checklist[0] == 0 and checklist[1] == 0 and \
            checklist[2] == player and checklist[3] == player \
            and checklist[5] == 0:
        return 1900
    elif checklist[1] == 0 and checklist[2] == 0 and \
            checklist[3] == player and checklist[5] == player \
            and checklist[6] == 0:
        return 1900
    elif checklist[2] == 0 and checklist[3] == 0 and \
            checklist[5] == player and checklist[6] == player \
            and checklist[7] == 0:
        return 1900
    elif checklist[1] == 0 and checklist[2] == player and \
            checklist[3] == player and checklist[5] == 0 \
            and checklist[6] == 0:
        return 1900
    elif checklist[2] == 0 and checklist[3] == player and \
            checklist[5] == player and checklist[6] == 0 \
            and checklist[7] == 0:
        return 1900
    elif checklist[3] == 0 and checklist[5] == player and \
            checklist[6] == player and checklist[7] == 0 \
            and checklist[8] == 0:
        return 1900
    elif checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[5] == 0:
        return 1600
    elif checklist[2] == 0 and checklist[3] == player and \
            checklist[6] == player and checklist[5] == 0 \
            and checklist[7] == 0:
        return 1600
    elif checklist[3] == 0 and checklist[5] == player and \
            checklist[7] == player and checklist[6] == 0 \
            and checklist[8] == 0:
        return 1600
    elif checklist[3] == 0 and checklist[5] == 0 and \
            checklist[7] == player and checklist[6] == player \
            and checklist[8] == 0:
        return 1600
    elif checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[6] == 0:
        return 1600
    elif checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[6] == 0:
        return 1600
    else:
        return 0


# 下在这个点会形成眠三
def willbesleep3(player, enemy, checklist):
    if checklist[1] == enemy and checklist[2] == player and \
            checklist[3] == player and checklist[5] == 0 \
            and checklist[6] == 0:
        return 350
    elif checklist[2] == enemy and checklist[3] == player and \
            checklist[5] == player and checklist[6] == 0 \
            and checklist[7] == 0:
        return 350
    elif checklist[3] == enemy and checklist[5] == player and \
            checklist[6] == player and checklist[7] == 0 \
            and checklist[8] == 0:
        return 350
    elif checklist[0] == 0 and checklist[1] == 0 and \
            checklist[2] == player and checklist[3] == player \
            and checklist[5] == enemy:
        return 350
    elif checklist[1] == 0 and checklist[2] == 0 and \
            checklist[3] == player and checklist[5] == player \
            and checklist[6] == enemy:
        return 350
    elif checklist[2] == 0 and checklist[3] == 0 and \
            checklist[5] == player and checklist[6] == player \
            and checklist[7] == enemy:
        return 350
    elif checklist[0] == enemy and checklist[1] == 0 and \
            checklist[2] == player and checklist[3] == player \
            and checklist[5] == 0 and checklist[6] == enemy:
        return 300
    elif checklist[1] == enemy and checklist[2] == 0 and \
            checklist[3] == player and checklist[5] == player \
            and checklist[6] == 0 and checklist[7] == enemy:
        return 300
    elif checklist[2] == enemy and checklist[3] == 0 and \
            checklist[5] == player and checklist[6] == player \
            and checklist[7] == 0 and checklist[8] == enemy:
        return 300
    elif checklist[0] == enemy and checklist[1] == player and \
            checklist[2] == 0 and checklist[3] == player \
            and checklist[5] == 0 and checklist[6] == enemy:
        return 300
    elif checklist[1] == enemy and checklist[2] == player and \
            checklist[3] == 0 and checklist[5] == player \
            and checklist[6] == 0 and checklist[7] == enemy:
        return 300
    elif checklist[2] == enemy and checklist[3] == player and \
            checklist[5] == 0 and checklist[6] == player \
            and checklist[7] == 0 and checklist[8] == enemy:
        return 300
    elif checklist[0] == enemy and checklist[1] == player and \
            checklist[2] == 0 and checklist[3] == player \
            and checklist[5] == 0 and checklist[6] == enemy:
        return 300
    elif checklist[1] == enemy and checklist[2] == player and \
            checklist[3] == 0 and checklist[5] == player \
            and checklist[6] == 0 and checklist[7] == enemy:
        return 300
    elif checklist[3] == enemy and checklist[5] == 0 and \
            checklist[6] == player and checklist[7] == player \
            and checklist[8] == 0:
        return 300
    elif checklist[0] == enemy and checklist[1] == player and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[5] == 0:
        return 300
    elif checklist[2] == enemy and checklist[3] == player and \
            checklist[5] == 0 and checklist[6] == player \
            and checklist[7] == 0:
        return 300
    elif checklist[3] == enemy and checklist[5] == player and \
            checklist[6] == 0 and checklist[7] == player \
            and checklist[8] == 0:
        return 300
    elif checklist[0] == player and checklist[1] == player and \
            checklist[2] == 0 and checklist[3] == 0 \
            and checklist[5] == enemy:
        return 300
    elif checklist[2] == enemy and checklist[3] == player and \
            checklist[5] == 0 and checklist[6] == 0 \
            and checklist[7] == player:
        return 300
    elif checklist[3] == enemy and checklist[5] == player and \
            checklist[6] == 0 and checklist[7] == 0 \
            and checklist[8] == player:
        return 300
    elif checklist[0] == player and checklist[1] == 0 and \
            checklist[2] == 0 and checklist[3] == player \
            and checklist[5] == enemy:
        return 300
    elif checklist[1] == player and checklist[2] == 0 and \
            checklist[3] == 0 and checklist[5] == player \
            and checklist[6] == enemy:
        return 300
    elif checklist[3] == enemy and checklist[5] == 0 and \
            checklist[6] == 0 and checklist[7] == player \
            and checklist[8] == player:
        return 300
    elif checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[5] == enemy:
        return 30
    elif checklist[2] == 0 and checklist[3] == player and \
            checklist[5] == 0 and checklist[6] == player \
            and checklist[7] == enemy:
        return 300
    elif checklist[3] == 0 and checklist[5] == player and \
            checklist[6] == 0 and checklist[7] == player \
            and checklist[8] == enemy:
        return 300
    elif checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == 0 and checklist[3] == player \
            and checklist[5] == enemy:
        return 300
    elif checklist[1] == 0 and checklist[2] == player and \
            checklist[3] == 0 and checklist[5] == player \
            and checklist[6] == enemy:
        return 300
    elif checklist[3] == 0 and checklist[5] == 0 and \
            checklist[6] == player and checklist[7] == player \
            and checklist[8] == enemy:
        return 300
    elif checklist[0] == player and checklist[1] == 0 and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[5] == enemy:
        return 300
    elif checklist[1] == enemy and checklist[2] == player and \
            checklist[3] == 0 and checklist[5] == 0 \
            and checklist[6] == player:
        return 300
    elif checklist[2] == player and checklist[3] == 0 and \
            checklist[5] == 0 and checklist[6] == player \
            and checklist[7] == enemy:
        return 300
    elif checklist[3] == enemy and checklist[5] == 0 and \
            checklist[6] == player and checklist[7] == 0 \
            and checklist[8] == player:
        return 300
    else:
        return 0


# 下在这个点会形成活二
def willbealive2(player, enemy, checklist):
    if checklist[1] == 0 and checklist[2] == 0 and \
            checklist[3] == player and checklist[5] == 0 \
            and checklist[6] == 0:
        return 99
    elif checklist[2] == 0 and checklist[3] == 0 and \
            checklist[5] == player and checklist[6] == 0 \
            and checklist[7] == 0:
        return 99
    elif checklist[0] == 0 and checklist[1] == 0 and \
            checklist[2] == 0 and checklist[3] == player \
            and checklist[5] == 0 and checklist[6] == enemy:
        return 99
    elif checklist[1] == 0 and checklist[2] == 0 and \
            checklist[3] == 0 and checklist[5] == player \
            and checklist[6] == 0 and checklist[7] == enemy:
        return 99
    elif checklist[1] == enemy and checklist[2] == 0 and \
            checklist[3] == player and checklist[5] == 0 \
            and checklist[6] == 0 and checklist[7] == 0:
        return 99
    elif checklist[2] == enemy and checklist[3] == 0 and \
            checklist[5] == player and checklist[6] == 0 \
            and checklist[7] == 0 and checklist[8] == 0:
        return 99
    else:
        return 0


# 下在这个点会形成眠二
def willbesleep2(player, enemy, checklist):
    if checklist[2] == enemy and checklist[3] == player and \
            checklist[5] == 0 and checklist[6] == 0 \
            and checklist[7] == 0:
        return 5
    elif checklist[3] == enemy and checklist[5] == player and \
            checklist[6] == 0 and checklist[7] == 0 \
            and checklist[8] == 0:
        return 5
    elif checklist[0] == 0 and checklist[1] == 0 and \
            checklist[2] == 0 and checklist[3] == player \
            and checklist[5] == enemy:
        return 5
    elif checklist[1] == 0 and checklist[2] == 0 and \
            checklist[3] == 0 and checklist[5] == player \
            and checklist[6] == enemy:
        return 5
    elif checklist[1] == enemy and checklist[2] == 0 and \
            checklist[3] == player and checklist[5] == 0 \
            and checklist[6] == 0 and checklist[7] == enemy:
        return 5
    elif checklist[2] == enemy and checklist[3] == 0 and \
            checklist[5] == player and checklist[6] == 0 \
            and checklist[7] == 0 and checklist[8] == enemy:
        return 5
    elif checklist[0] == enemy and checklist[1] == 0 and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[5] == 0 and checklist[6] == enemy:
        return 5
    elif checklist[2] == enemy and checklist[3] == 0 and \
            checklist[5] == 0 and checklist[6] == player \
            and checklist[7] == 0 and checklist[8] == enemy:
        return 5
    elif checklist[0] == enemy and checklist[1] == 0 and \
            checklist[2] == 0 and checklist[3] == player \
            and checklist[5] == 0 and checklist[6] == enemy:
        return 5
    elif checklist[1] == enemy and checklist[2] == 0 and \
            checklist[3] == 0 and checklist[5] == player \
            and checklist[6] == 0 and checklist[7] == enemy:
        return 5
    elif checklist[0] == 0 and checklist[1] == player and \
            checklist[2] == 0 and checklist[3] == 0 \
            and checklist[5] == enemy:
        return 5
    elif checklist[3] == 0 and checklist[5] == 0 and \
            checklist[6] == 0 and checklist[7] == player \
            and checklist[8] == enemy:
        return 5
    elif checklist[0] == 0 and checklist[1] == 0 and \
            checklist[2] == player and checklist[3] == 0 \
            and checklist[5] == enemy:
        return 5
    elif checklist[2] == 0 and checklist[3] == 0 and \
            checklist[5] == 0 and checklist[6] == player \
            and checklist[7] == enemy:
        return 5
    elif checklist[1] == enemy and checklist[2] == player and \
            checklist[3] == 0 and checklist[5] == 0 \
            and checklist[6] == 0:
        return 5
    elif checklist[3] == enemy and checklist[5] == 0 and \
            checklist[6] == player and checklist[7] == 0 \
            and checklist[8] == 0:
        return 5
    elif checklist[0] == enemy and checklist[1] == player and \
            checklist[2] == 0 and checklist[3] == 0 \
            and checklist[5] == 0:
        return 5
    elif checklist[3] == enemy and checklist[5] == 0 and \
            checklist[6] == 0 and checklist[7] == player \
            and checklist[8] == 0:
        return 5
    else:
        return 0


# 五子棋盘
def qipan():
    screen.blit(BG, (0, 0))
    screen.blit(background, (50, 50))
    screen.blit(anniu, (875, 500))
    te = zw.render("悔棋", True, (0, 0, 0))
    screen.blit(te, (885, 505))
    screen.blit(anniu, (875, 600))
    te = zw.render("重开", True, (0, 0, 0))
    screen.blit(te, (885, 605))
    screen.blit(anniu, (875, 700))
    te = zw.render("退出", True, (0, 0, 0))
    screen.blit(te, (885, 705))
    for i in range(15):
        text_A = font.render(chr(65 + i), True, (0, 0, 0))
        screen.blit(text_A, (lc[i] - 10, 50))

        text_number = font.render(str(i + 1), True, (0, 0, 0))
        screen.blit(text_number, (50, lc[i] - 16))
        start_P = (100, lc[i])
        end_P = (800, lc[i])
        if lc[i] == 800 or lc[i] == 100:
            pygame.draw.line(screen, WHITE_COLOR, start_P, end_P, 3)
        else:
            pygame.draw.line(screen, WHITE_COLOR, start_P, end_P, 1)
        start_P = (lr[i], 100)
        end_P = (lr[i], 800)
        if lr[i] == 800 or lr[i] == 100:
            pygame.draw.line(screen, WHITE_COLOR, start_P, end_P, 3)
        else:
            pygame.draw.line(screen, WHITE_COLOR, start_P, end_P, 1)
    y = 50
    for i in range(3):
        y += 200
        x = 250
        for j in range(3):
            pygame.draw.circle(screen, WHITE_COLOR, (x, y), 5, 5)
            x += 200


# 判断是否赢了
def isOK(vis):
    for i in range(15):
        for j in range(11):
             if vis[i][j] == 1 and vis[i][j+1] == 1 and vis[i][j+2] == 1 and vis[i][j+3] == 1 and vis[i][j+4] == 1:
                 return 1
             elif  vis[i][j] == 2 and vis[i][j+1] == 2 and vis[i][j+2] == 2 and vis[i][j+3] == 2 and vis[i][j+4] == 2:
                 return 2
    for i in range(11):
        for j in range(15):
            if vis[i][j] == 1 and vis[i+1][j] == 1 and vis[i+2][j] == 1 and vis[i+3][j] == 1 and vis[i+4][j] == 1:
                return 1
            elif vis[i][j] == 2 and vis[i+1][j] == 2 and vis[i+2][j] == 2 and vis[i+3][j] == 2 and vis[i+4][j] == 2:
                return 2
    for i in range(4,15):
        for j in range(11):
            if vis[i][j] == 1 and vis[i-1][j+1] == 1 and vis[i-2][j+2] == 1 and vis[i-3][j+3] == 1 and vis[i-4][j+4] == 1:
                return 1
            elif vis[i][j] == 2 and vis[i-1][j+1] == 2 and vis[i-2][j+2] == 2 and vis[i-3][j+3] == 2 and vis[i-4][j+4] == 2:
                return 2
    for i in range(11):
        for j in range(11):
            if vis[i][j] == 1 and vis[i+1][j+1] == 1 and vis[i+2][j+2] == 1 and vis[i+3][j+3] == 1 and vis[i+4][j+4] == 1:
                return 1
            elif vis[i][j] == 2 and vis[i+1][j+1] == 2 and vis[i+2][j+2] == 2 and vis[i+3][j+3] == 2 and vis[i+4][j+4] == 2:
                return 2
    return 0


# 初始化一些变量
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)
zw = pygame.font.SysFont('SimHei', 40)
zw1 = pygame.font.SysFont('SimHei', 20)
vis = numpy.zeros([15, 15])  # 相当于一个15*15的数组并初始化


lc = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
lr = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
screen = pygame.display.set_mode((1000, 850))  # 屏幕大小
# line(Surface, color, start_pos, end_pos, width = 1)
WHITE_COLOR = (0, 0, 0)
# RGB 0~255
background_str = "图.jpg"
background = pygame.image.load(background_str)
background = pygame.transform.scale(background, (800, 800))  # 棋盘背景
anniu = pygame.image.load("长条按钮.png")
anniu = pygame.transform.scale(anniu, (100, 50))  # 按钮
BG = pygame.image.load("BG.jpg")
BG = pygame.transform.scale(BG, (1000, 850))  # 背景


wh = []  # 存白棋
bl = []  # 存黑棋
cnt = 0  # 判断到谁下棋
ff = 0  # 判断棋盘是否要重画
hb_flag = 0  # 黑白棋标志
hm = 0  # 画面标志
win = 1  # 判断是否赢了

while True:
    if hm == 0:  #开始画面
        # screen = pygame.display.set_mode((1000, 800))
        startgame = pygame.image.load("开始画面.jpeg")
        startgame = pygame.transform.scale(startgame, (1000, 850))
        screen.blit(startgame, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if pressed_array[0]:
                    xx, yy = pygame.mouse.get_pos()
                    # print(xx, yy)
                    if xx >= 240 and xx <= 760 and yy >= 265 and yy <= 330:
                        hm = 1
                    elif xx >= 240 and xx <= 760 and yy >= 200 and yy <= 255:
                        hm = 2
                    elif xx >= 240 and xx <= 760 and yy >= 330and yy <= 400:
                        hm = 3
                    elif xx >= 240 and xx <= 760 and yy >= 410 and yy <= 470:
                        hm = 4
    elif hm == 1:  # 人机对战
        if ff == 0:
            qipan()
            ff = 1
        if hb_flag == 1:
            p = haveValuePoints(vis)
            length = len(p)
            # print(p)
            a = 0
            b = 0
            mm = -1
            gg = 0
            for i in range(length):
                if p[i][2] > mm and gg == 0:
                    mm = p[i][2]
                    a = p[i][0]
                    b = p[i][1]
                    if mm >= 100000:
                        gg = 1
                elif p[i][2] < mm and p[i][2] >= 100000 and gg == 1:
                    mm = p[i][2]
                    a = p[i][0]
                    b = p[i][1]

            # print(a, b)
            if win == 1:
                st = time.time()
                while time.time() - st < 0.6:
                    pygame.draw.circle(screen, (random.randint(0,100), random.randint(0,100), random.randint(0,100)), (100 + a * 50, 100 + b * 50), 20, 20)
                    pygame.display.update()
                pygame.draw.circle(screen, (0, 0, 0), (100 + a * 50, 100 + b * 50), 20, 20)
                vis[a][b] = 1
                bl.append([a, b])
                hb_flag = 0
            if isOK(vis) == 1:
                te = zw.render("黑棋胜！！！", True, (255, 0, 0))
                screen.blit(te, (400, 400))
                win = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and hb_flag == 0:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            # print('Pressed LEFT Button!')
                            xx, yy = pygame.mouse.get_pos()
                            xx = (xx + 25) // 50 * 50
                            yy = (yy + 25) // 50 * 50
                            if xx >= 875 and xx <= 975 and yy >= 500 and yy <= 550:
                                qipan()
                                if len(bl) != 0:
                                    aa = bl.pop()
                                    vis[aa[0]][aa[1]] = 0
                                if len(wh) != 0:
                                    bb = wh.pop()
                                    vis[bb[0]][bb[1]] = 0
                                for i in range(15):
                                    for j in range(15):
                                        if vis[i][j] == 1:
                                            pygame.draw.circle(screen, (0, 0, 0), (100+i*50, 100+j*50), 20, 20)
                                        elif vis[i][j] == 2:
                                            pygame.draw.circle(screen, (255, 255, 255), (100 + i * 50, 100 + j * 50), 20, 20)
                                win = 1
                            elif xx >= 875 and xx <= 975 and yy >= 600 and yy <= 650:
                                cnt = 0
                                ff = 0
                                hb_flag = 0
                                vis = numpy.zeros([15, 15])
                                wh.clear()
                                bl.clear()
                                win = 1
                            elif xx >= 875 and xx <= 975 and yy >= 670 and yy <= 750:
                                hm = 0
                                cnt = 0
                                ff = 0
                                hb_flag = 0
                                vis = numpy.zeros([15, 15])
                                wh.clear()
                                bl.clear()
                                win = 1
                            if xx < 100 or xx > 800 or yy < 100 or yy > 800:
                                break
                            if vis[(xx - 100) // 50][(yy - 100) // 50] == 0:
                                if win == 1:
                                    pygame.draw.circle(screen, (255, 255, 255), (xx, yy), 20, 20)
                                    vis[(xx - 100) // 50][(yy - 100) // 50] = 2
                                    wh.append([(xx - 100) // 50,(yy - 100) // 50])
                                    hb_flag = 1
                            if isOK(vis) == 2:
                                te = zw.render("白棋胜！！！", True, (255, 0, 0))
                                screen.blit(te, (400, 400))
                                win = 0
                                hb_flag = 0
                                bl.append([(-100, -100)])
                        # elif index == 1:
                        #     print('The mouse wheel Pressed!')
                        # elif index == 2:
                        #     print('Pressed RIGHT Button!')
    elif hm == 2:  # 人人对战
        if ff == 0:
            qipan()
            ff = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            xx, yy = pygame.mouse.get_pos()
                            xx = (xx + 25) // 50 * 50
                            yy = (yy + 25) // 50 * 50
                            if xx >= 875 and xx <= 975 and yy >= 500 and yy <= 550:
                                qipan()
                                if len(bl) != 0:
                                    cnt -= 1
                                    aa = bl.pop()
                                    vis[aa[0]][aa[1]] = 0
                                if len(wh) != 0:
                                    cnt -= 1
                                    bb = wh.pop()
                                    vis[bb[0]][bb[1]] = 0
                                for i in range(15):
                                    for j in range(15):
                                        if vis[i][j] == 1:
                                            pygame.draw.circle(screen, (0, 0, 0), (100+i*50, 100+j*50), 20, 20)
                                        elif vis[i][j] == 2:
                                            pygame.draw.circle(screen, (255, 255, 255), (100 + i * 50, 100 + j * 50), 20, 20)
                                win = 1
                            elif xx >= 875 and xx <= 975 and yy >= 600 and yy <= 650:
                                cnt = 0
                                ff = 0
                                hb_flag = 0
                                vis = numpy.zeros([15, 15])
                                wh.clear()
                                bl.clear()
                                win = 1
                            elif xx >= 875 and xx <= 975 and yy >= 670 and yy <= 750:
                                hm = 0
                                cnt = 0
                                ff = 0
                                hb_flag = 0
                                vis = numpy.zeros([15, 15])
                                wh.clear()
                                bl.clear()
                                win = 1
                            if xx < 100 or xx > 800 or yy < 100 or yy > 800:
                                break
                            if cnt % 2 and vis[(xx - 100) // 50][(yy - 100) // 50] == 0:
                                cnt += 1
                                if win == 1:
                                    st = time.time()
                                    while time.time() - st < 0.6:
                                        pygame.draw.circle(screen, (random.randint(0,100), random.randint(0,100),random.randint(0,100)), (xx, yy), 20, 20)
                                        pygame.display.update()
                                    pygame.draw.circle(screen, WHITE_COLOR, (xx, yy), 20, 20)
                                    vis[(xx - 100) // 50][(yy - 100) // 50] = 1
                                    bl.append([(xx - 100) // 50,(yy - 100) // 50])
                            elif cnt % 2 == 0 and vis[(xx - 100) // 50][(yy - 100) // 50] == 0:
                                cnt += 1
                                if win == 1:
                                    st = time.time()
                                    while time.time() - st < 0.6:
                                        pygame.draw.circle(screen, (
                                        random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)),
                                                           (xx, yy), 20, 20)
                                        pygame.display.update()
                                    pygame.draw.circle(screen, (255, 255, 255), (xx, yy), 20, 20)
                                    vis[(xx - 100) // 50][(yy - 100) // 50] = 2
                                    wh.append([(xx - 100) // 50, (yy - 100) // 50])
                            if isOK(vis) == 1:
                                te = zw.render("黑棋胜！！！", True, (255, 0, 0))
                                screen.blit(te, (400, 400))
                                win = 0
                            elif isOK(vis) == 2:
                                te = zw.render("白棋胜！！！", True, (255, 0, 0))
                                screen.blit(te, (400, 400))
                                win = 0
    elif hm == 3:  # 帮助画面
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(BG, (0, 0))
        screen.blit(background, (50, 50))
        screen.blit(anniu, (0, 0))
        te = zw.render("返回", True, (0, 0, 0))
        ss = zw1.render("    五子棋是世界智力运动会竞技项目之一，是一种两人对弈的纯策略型棋类游戏，", True, (0, 0, 0))
        screen.blit(ss, (100, 100))
        ss = zw1.render("是世界智力运动会竞技项目之一，通常双方分别使用黑白两色的棋子，", True, (0, 0, 0))
        screen.blit(ss, (100, 130))
        ss = zw1.render("下在棋盘直线与横线的交叉点上，先形成5子连线者获胜。", True, (0, 0, 0))
        screen.blit(ss, (100, 160))
        ss = zw1.render("    棋具与围棋通用，起源于中国上古时代的传统黑白棋种之一。主要流行", True, (0, 0, 0))
        screen.blit(ss, (100, 190))
        ss = zw1.render("于华人和汉字文化圈的国家以及欧美一些地区，是世界上最古老的棋。", True, (0, 0, 0))
        screen.blit(ss, (100, 220))
        ss = zw1.render("    容易上手，老少皆宜，而且趣味横生，引人入胜；不仅能增强思维能力，", True, (0, 0, 0))
        screen.blit(ss, (100, 250))
        ss = zw1.render("提高智力，而且富含哲理，有助于修身养性。已在各个游戏平台有应用。", True, (0, 0, 0))
        screen.blit(ss, (100, 280))
        screen.blit(te, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if index == 0:
                        xx, yy = pygame.mouse.get_pos()
                        if xx >=0 and xx <= 100 and yy >= 0 and yy <= 50:
                            hm = 0
    elif hm == 4:  # 退出
        exit()
    pygame.display.update()