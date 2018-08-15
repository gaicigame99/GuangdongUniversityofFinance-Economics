import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.Font("C:\Windows\Fonts\STXINGKA.TTF",40)


begin_p = pygame.image.load("white.png")
button = pygame.image.load("button.png")
fire = pygame.image.load("fire.png")
fire = pygame.transform.scale(fire,(30,45))
game_over = pygame.image.load("gameover.jpg")
background = pygame.image.load("background.png")
background = pygame.transform.scale(background,(800,600))
people = pygame.image.load("people.png")
hat_p = pygame.image.load("hat.png")
hat_p = pygame.transform.scale(hat_p,(60,35))
love_p = pygame.image.load("love.png")
love_p = pygame.transform.scale(love_p,(50,45))


list_drop = []
score = 0
love = 0
speed = 2
page = 0


class drop(object):
    def __init__(self,_x,_y,_name,_weight,_height,_way):
        self.x = _x
        self.y = _y
        self.name = _name
        self.weight = _weight
        self.height = _height
        self.way = _way



def add(num,name,weight,height):
    for i in range(num):
        add = drop(random.randint(0, 740), random.randint(-1200, -200), name, weight, height, 1)
        list_drop.append(add)

add(13,"hat",60,35)
add(2,'love',50,45)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    if page == 0:
        screen.blit(begin_p, (0, 0))
        play_inf = font.render(u"当然是选择原谅她啊！", True, (0, 255, 0))
        screen.blit(play_inf, (250, 200))
        screen.blit(button, (250, 300))
        if event.type == pygame.MOUSEBUTTONDOWN:
            px, py = pygame.mouse.get_pos()
            if px > 250 and px < 250 + 300 and py > 300 and py < 300 + 80:
                page = 1

    if page == 2:

        screen.blit(begin_p, (0, 0))
        screen.blit(button, (250, 450))
        screen.blit(game_over, (250, 100))
        screen.blit(inf, (250, 0))
        score_inf = font.render((u"力量：%d" % (score)), True, (0, 255, 0))
        screen.blit(score_inf, (10, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            px, py = pygame.mouse.get_pos()
            if px > 250 and px < 250 + 300 and py > 450 and py < 450 + 80:
                page = 1
                love = 0
                score = 0
                speed = 2

    if page == 1:
        px, py = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        screen.blit(people, (px-40, 520))

        for j in range(len(list_drop)):
            if list_drop[j].name == 'hat':
                screen.blit(hat_p, (list_drop[j].x, list_drop[j].y))
            else:
                screen.blit(love_p, (list_drop[j].x, list_drop[j].y))
            #撞墙反弹
            if list_drop[j].x > (800-list_drop[j].weight) or (list_drop[j].x <= 0):
                list_drop[j].way = -list_drop[j].way

            list_drop[j].y += speed
            list_drop[j].x += list_drop[j].way * speed
            # 帽子飞出屏幕后重新分配位置
            if list_drop[j].y > 600:
                list_drop[j].x = random.randint(0, 800-list_drop[j].weight)
                list_drop[j].y = random.randint(-600, -50)

        for j in range(len(list_drop)):
            if (list_drop[j].x <= px <= list_drop[j].x + list_drop[j].weight and \
                540<=list_drop[j].y+list_drop[j].height <= 600) or \
                    (list_drop[j].x <= px + 50 <= list_drop[j].x + list_drop[j].weight and \
                     520 <= list_drop[j].y + list_drop[j].height <= 600):
                list_drop[j].x = random.randint(0, 800 - list_drop[j].weight)
                list_drop[j].y = random.randint(-600, -50)
                if list_drop[j].name == 'hat':
                    score += 5
                else:
                    love += 1

        inf = font.render((u"级别：老实人"), True, (0, 255, 0))
        if score >= 1000:
            inf = font.render((u"级别：青青草原(最高级)"), True, (0, 255, 0))
            speed = 10
        elif score >= 650:
            inf = font.render((u"级别：接盘侠"), True, (0, 255, 0))
            speed = 8
        elif score >=250:
            inf = font.render((u"级别：千斤顶"), True, (0, 255, 0))
            speed = 5
        elif score >= 100:
            inf = font.render((u"级别：备胎"), True, (0, 255, 0))
            speed = 3

        if love <= 4:
            screen.blit(fire, (770, 0))
            if love <= 3:
                screen.blit(fire, (740, 0))
                if love <= 2:
                    screen.blit(fire, (710, 0))
                    if love <= 1:
                        screen.blit(fire, (680, 0))
                        if love <= 0:
                            screen.blit(fire, (650, 0))
        if love == 5:
            page = 2
        screen.blit(inf, (250, 0))
        score_inf = font.render((u"力量：%d"%(score)), True, (0, 255, 0))
        screen.blit(score_inf, (10, 0))


    pygame.display.update()