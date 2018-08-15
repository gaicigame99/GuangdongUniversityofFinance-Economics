import pygame
import random
from pygame.locals import *

def begin():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load(r"images\bg5.jpg")
    car = pygame.transform.rotate(pygame.image.load(r"images\car.png"), 270)
    t_truck = pygame.transform.rotate(pygame.image.load(r"images\truck.png"), 270)
    truck = pygame.transform.scale(t_truck, (128, 128))
    line = pygame.transform.scale(pygame.image.load(r"images\line.jpeg"), (24, 80))
    road = pygame.transform.scale(pygame.image.load(r"images\road.jpg"),  (800, 1200))
    gold = pygame.image.load(r"images\gold.png")
    tree = pygame.image.load(r"images\tree.png")
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 28)
    white = (255, 255, 255)
    start_button = pygame.image.load(r"images\start_button.png")


    # 是否点击想点击的按钮
    def collision(_x, _y, tx, ty):
        if tx < mouse_x < tx + start_button.get_rect().width and \
                ty < mouse_y < ty + start_button.get_rect().height and\
                pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


    # def collection(carx, cary, _car_width,_car_height,  g_x, g_y, _gold_width, _gold_height):
    #     if g_x + _gold_width > carx or \
    #             g_x < carx + _car_width or \
    #             g_y < cary + _car_height or \
    #             g_y + _gold_height > cary:
    #         print("发生碰撞")
    #         return True
    #     else:
    #         return False


    # 汽车初始位置
    car_x = 300
    car_y = 349
    # 开始按钮的位置
    st_x = 600
    st_y = 400

    # 道路路障的位置
    sx = 0
    sy = 0

    # 获取金币的随机位置
    gx = []
    gy = []
    for i in range(10):
        gx.append(random.randint(200, 600))
        gy.append(random.randint(0, 350))

    # 斑马线的位置
    x = []
    y = []
    for j in range(3):
        x.append(200 + 200 * j)
        y.append(80 + 200 * j)

    # 获取卡车的随即位置
    tr_x = []
    tr_y = []
    for i in range(4):
        tr_x.append(50 + 180 * i)
        tr_y.append(100 + 150 * i)

    # 获取树木的位置
    ly = []
    ry = []
    for i in range(4):
        ly.append(20 + 140 * i)
        ry.append(50 + 140 * i)


    start = 0
    time = 50
    move_x = 0
    move_y = 0
    _score = 0
    speed = 0

    car_width = 45
    # car.get_rect().width
    truck_width = 45
    # truck.get_rect().width
    car_height = 120
    # car.get_rect().height
    truck_height = 120
    # truck.get_rect().height
    print(car_width,truck_width,car_width,truck_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        if event.type == pygame.KEYDOWN:  # 键被按下
            if event.key == pygame.K_LEFT:
                move_x = -3
            elif event.key == pygame.K_RIGHT:
                move_x = 3
            elif event.key == pygame.K_UP:
                move_y = -3
                speed = -1
            # 如果用户放开了键盘，图就不要动了
            elif event.type == pygame.KEYUP:
                move_x = 0
                move_y = 0
            # 根据按键来调节汽车的移动
        zu = pygame.key.get_pressed()
        if zu[pygame.K_LEFT]:
            # 按下的是左方向键的话，把x坐标减一
            move_x = -3
            car_x += move_x
        elif zu[pygame.K_RIGHT]:
            # 右方向键则加一
            move_x = 3
            car_x += move_x
        elif zu[pygame.K_UP]:
            move_y = 3
            speed = 1

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        screen.blit(start_button, (st_x, st_y))
        if collision(mouse_x, mouse_y, st_x, st_y):
            start = 1
        if start == 1:
            screen.blit(road, (0, 0))

            # move
            for i in range(4):
                ly[i] += move_y
                ry[i] += move_y
                tr_y[i] -= speed

                if tr_y[i] > 600 or tr_y[i] < 0:
                    tr_y[i] = random.randint(600, 900)
                if ly[i] > 600 or ly[i] < 0:
                    ly[i] = 20
                if ry[i] > 600 or ry[i] < 0:
                    ry[i] = 70
                screen.blit(tree, (0, ly[i]))
                screen.blit(tree, (730, ry[i]))
                screen.blit(truck, (tr_x[i], tr_y[i]))

                # 判断碰撞
                if car_x + car_width > tr_x[i] and \
                        car_x < tr_x[i] + truck_width and \
                        car_y < tr_y[i] + truck_height and \
                        car_y + car_height > tr_y[i]:
                    # print("车子的左边是%d,右边是%d,上边是%d,下边是%d" % (car_x, car_x + car_width, car_y, car_y+car_height))
                    # print("卡车[%d]的左边是%d,右边是%d,上边是%d,下边是%d" % (i, tr_x[i], tr_x[i] + truck_width, tr_y[i], tr_y[i] + truck_height))
                    _score += 1
                    tr_x[i], tr_y[i] = (-100, -100)

            score = font.render("score:" + str(_score), True, white)
            screen.blit(score, (100, 50))
            for i in range(3):
                for j in range(3):
                    screen.blit(line, (x[i], y[j]))
                    y[i] += move_y
                    r = line.get_rect().height
                    if y[i] > 600:
                        y[i] = -30

            screen.blit(car, (car_x, car_y))
            if car_y < 0:
                car_y += 5

        pygame.display.update()