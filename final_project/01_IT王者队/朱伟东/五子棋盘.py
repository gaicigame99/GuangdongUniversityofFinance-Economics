import pygame
import math
from 朱伟东.Computer import computer
def judge(x,y):
    now = 0
    counter = 0
    if y<0 or y >14 or x < 0 or x > 14:
        return
    for i in range(15):
        if process[i][y] == now:
            if now == 0:
                continue
            else:
                counter += 1
                if counter == 4:
                    return now
        else:
            now = process[i][y]
            counter = 0
    now = 0
    counter = 0
    for i in range(15):
        if process[x][i] == now:
            if now == 0:
                continue
            else:
                counter += 1
                if counter == 4:
                    return now
        else:
            now = process[x][i]
            counter = 0
    now = 0
    counter = 0
    if y > x:
        a = 0
        b = y - x
    else:
        b = 0
        a = x - y
    while a <=14 and b <=14:
        if process[a][b] == now:
            if now == 0:
                pass
            else:
                counter += 1
                if counter == 4:
                    return now
        else:
            now = process[a][b]
            counter = 0
        b += 1
        a += 1
    now = 0
    counter = 0
    if y - 0 > 14 - x:
        b = 14
        a = (y - 0) - (14 - x)
    else:
        a = 0
        b = 14 - ((14 - x) - (y - 0))
    while b >= 0 and a <= 14:
        if process[b][a] == now:
            if now == 0:
                pass
            else:
                counter += 1
                if counter == 4:
                    return now
        else:
            now = process[b][a]
            counter = 0
        b -= 1
        a += 1
def size_count(a,b,x,y,clickx,clicky):
    result = [0,0]
    if clickx < a - 21 or clicky < b - 21 or clickx >x + 21 or clicky > y + 21:
        return [-1,-1]
    i = int((clicky-b)/45) + 1
    j = int((clickx-a)/45) + 1
    i1 = math.fabs(clicky-b)%45
    j1 = math.fabs(clickx-a)%45
    if i1 <= 21:
        result[0] = i - 1
    else:
        result[0] = i
    if j1 <= 21:
        result[1] = j - 1
    else:
        result[1] = j
    return result

def drawRectabgle(a,b,x,y):
    pygame.draw.line(screen, BLACK, (a, b), (a, y), 2)
    pygame.draw.line(screen, BLACK, (a, b), (x, b), 2)
    pygame.draw.line(screen, BLACK, (a, y), (x, y), 2)
    pygame.draw.line(screen, BLACK, (x, b), (x, y), 2)

    pygame.draw.line(screen, BLACK, (a-25, b-25), (a-25, y+25), 3)
    pygame.draw.line(screen, BLACK, (a-25, b-25), (x+25, b-25), 3)
    pygame.draw.line(screen, BLACK, (a-25, y+25), (x+25, y+25), 3)
    pygame.draw.line(screen, BLACK, (x+25, b-25), (x+25, y+25), 3)
    l = x-a
    w = y-b
    l_list = l/14
    w_list = w/14

    for i in range(1,14):
        pygame.draw.line(screen, BLACK, (a+ l_list*i, b ), (a+ l_list*i, y), 2)
    for i in range(1,14):
        pygame.draw.line(screen, BLACK, (a, b+ w_list*i ), (x, b+ l_list*i), 2)
    screen.blit(pon,(a + l_list * 3 - 7, b + l_list * 3 - 8))
    screen.blit(pon, (a + l_list * 11 - 7, b + l_list * 3 - 8))
    screen.blit(pon, (a + l_list * 3 - 7, b + l_list * 11 - 8))
    screen.blit(pon, (a + l_list * 11 - 7, b + l_list * 11 - 8))
    screen.blit(pon, (a + l_list * 7 - 7, b + l_list * 7 - 8))
    # screen.blit(bq, (a + l_list * 7 - 24, b + l_list * 7 - 24))
def printText(a,b,x,y):
    l = x - a
    w = y - b
    l_list = l / 14
    w_list = w / 14
    font = pygame.font.Font("C:\windows\Fonts\Arial.ttf",15)
    for i in range(15):
        text1 = font.render(chr(65+i),True,(0,0,0))
        text2 = font.render(str(i+1),True,(0,0,0))
        screen.blit(text1,(a + l_list*i-5,b-20))
        screen.blit(text2, (a - 20, b - 5+ w_list * i))
def putchress(a,b,x,y,count):
    l = 715 - a
    w = 665 - b
    l_list = l / 14
    w_list = w / 14
    if x < 0 or y < 0:
        pass
    else:
        try:
            if process[x][y] == 0:
                pass
            else:
                process[16][16] = 0
        except IndexError:
            pass
        else:
            if count % 2 == 0:
                screen.blit(bq, (a + l_list * y - 25, b + w_list * x - 25))
                process[x][y] = 2
                # j = judge(y,x)
                # if j == 1:
                #     print("白旗胜")
                count += 1
            else:
                screen.blit(hq, (a + l_list * y - 16, b + w_list * x - 16))
                process[x][y] = 1
                # j = judge(y, x)
                # if j == 2:
                #     print("黑旗胜")
                count += 1
    return count
    # print(process)

count = 1
pygame.init()
font2 = pygame.font.Font("C:\windows\Fonts\simhei.ttf",30)
screen = pygame.display.set_mode((800,700))
pon = pygame.image.load("pon.png")
bq = pygame.image.load("wq2.png")
bq = pygame.transform.scale(bq,(50,50))
hq = pygame.image.load("hq.png")
hq = pygame.transform.scale(hq,(32,32))
process = [([0] * 15) for i in range(15)]
star = True
BLACK = (0,0,0)
bgColor = (227, 168, 105)
WHITE = (255,255,255)
dian = (0,255,255)
screen.fill(bgColor)
drawRectabgle(85,35,715,665)
printText(85,35,715,665)
AI = computer()
print()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # for i in process:
            #     print(i)
            exit()
    #pygame.draw.line(screen, BLACK, (0, 0), (800, 600), 3)
    # drawRectabgle(85,35,715,665)
        if star:
            if event.type == pygame.MOUSEBUTTONDOWN:
                zb = pygame.mouse.get_pos()
                zb = size_count(85,35,715,665,zb[0],zb[1])
                count = putchress(85,35,zb[0],zb[1],count)
                pygame.display.update()
                j = judge(zb[0], zb[1])
                if j == 1:
                    print("黑棋胜")
                    text = font2.render("黑棋胜", True, (0, 0, 0))
                    screen.blit(text, (350, 300))
                    star = False
                    continue
                elif j == 2:
                    print("白棋胜")
                    text = font2.render("白棋胜", True, (255, 255, 255))
                    screen.blit(text, (350, 300))
                    star = False
                    continue
                zb = AI.get_result(process)
                count = putchress(85, 35, zb[0], zb[1], count)
                # print(process)
                j = judge(zb[0], zb[1])
                if j == 1:
                    print("黑棋胜")
                    text = font2.render("黑棋胜", True, (0, 0, 0))
                    screen.blit(text,(350,300))
                    star = False
                elif j == 2:
                    print("白棋胜")
                    text = font2.render("白棋胜", True, (255, 255, 255))
                    screen.blit(text, (350, 300))
                    star = False

    pygame.display.update()


