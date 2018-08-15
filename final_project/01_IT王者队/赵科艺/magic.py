import pygame
import random
import time
from pygame.locals import *
import os
from sys import exit


pygame.init()
# 屏幕
screen = pygame.display.set_mode((1200, 900))
# 字体
# font = pygame.font.Font(r'C:\Windows\Fonts\Arial.ttf', 25)
# WHILE_COLOR = (255, 255, 255)

# 开始界面
start_pitcure = pygame.image.load(r'image\开始界面.jpg')
start_pitcure = pygame.transform.scale(start_pitcure, (600, 900))
m_start = start_pitcure.get_rect()
print(m_start.width)
print(m_start.height)

# 结束界面
end_pitcure = pygame.image.load('image\end.jpg')
end_pitcure = pygame.transform.scale(end_pitcure, (1200, 900))
m_end = start_pitcure.get_rect()

# 敌人1图片
enemy_1_w = 130
enemy_1_h = 150
enemy_1 = pygame.image.load(r'image\enemy1.png')
enemy_1 = pygame.transform.scale(enemy_1, (enemy_1_w, enemy_1_h))
m_enemy_1 = enemy_1.get_rect()
enemy_1_x = 1500
enemy_1_y = 100
# 敌人2图片
enemy_2_w = -300
enemy_2_h = 130
enemy_2 = pygame.image.load(r'image\enemy2.png')
enemy_2 = pygame.transform.scale(enemy_2, (enemy_1_w, enemy_1_h))
m_enemy_2 = enemy_2.get_rect()
enemy_2_x = -400
enemy_2_y = 100
# 敌人3图片
enemy_3_w = 200
enemy_3_h = 200
enemy_3 = pygame.image.load(r'image\enemy3.png')
enemy_3 = pygame.transform.scale(enemy_3, (enemy_3_w, enemy_3_h))
m_enemy_3 = enemy_3.get_rect()
enemy_3_x = 600 - m_enemy_3.width/2
enemy_3_y = -700
# 英雄图片
hero = pygame.image.load(r'image\hero.png')
hero = pygame.transform.scale(hero, (120, 200))
m_hero = hero.get_rect()
hero_x = 600 - m_hero.width/2
hero_y = 580
# print(m_hero.width)
# print(m_hero.height)
# 英雄势力范围
hero_power1 = pygame.image.load(r'image\水晶_right.png')
hero_power1 = pygame.transform.scale(hero_power1, (400, 200))
m_hero_power1 = hero_power1.get_rect()
hero_power2 = pygame.image.load('image\水晶_left.png')
hero_power2 = pygame.transform.scale(hero_power2, (400, 200))
m_hero_power2 = hero_power2.get_rect()
hero_power3 = pygame.image.load(r'image\水晶_mid.png')
hero_power3 = pygame.transform.scale(hero_power3, (400, 300))
m_hero_power3 = hero_power3.get_rect()
# 背景图片
background = pygame.image.load(r'image\background.png')


e_1_x = []
e_1_y = []
e_2_x = []
e_2_y = []
e_3_x = []
e_3_y = []

speed = []

etime = 50
# 字体
score = 0
font = pygame.font.Font("C:\Windows\Fonts\Verdana.ttf", 80)
PURPLE_COLOR = (100, 100, 200)

T = 0
page = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if page == 1:
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 500 < mouse_x < 1100:
                page = 2


        screen.blit(background, (0, 0))
        screen.blit(start_pitcure, (300, 0))
        pygame.display.update()
    if page == 2:
        # 敌人出现频率
        if etime:
            etime -= 1
        else:
            e_1_x.append(1500)
            e_1_y.append(100)
            e_2_x.append(-300)
            e_2_y.append(100)
            e_3_x.append(600-m_enemy_3.width/2)
            e_3_y.append(-400)
            speed.append(random.randint(2, 4))
            etime = 50
        screen.blit(background, (0, 0))
        screen.blit(hero, (hero_x, hero_y))
        #     敌人1的碰撞检测
        for i in range(len(e_1_y)):
            screen.blit(enemy_1, (e_1_x[i], e_1_y[i]))
            # i = random.randint(3, 7)
            # l = random.randint(2, 5)
            # j = random.randint(0, 4)
            e_1_x[i] -= speed[i]
            e_1_y[i] += 1.5
            print(e_1_y)
            key_d = pygame.key.get_pressed()
            if key_d[K_d]:
                screen.blit(hero_power1, (600 - m_hero_power1.width/2, 520))
                if hero_x + m_hero.width <= e_1_x[i] < 600 + m_hero_power1.width/2:
                    e_1_x.pop(i)
                    e_1_y.pop(i)
                    score += 1
                    break
            if e_1_x[i] < hero_x + m_hero.width:
                hero_y = 1000
                page = 3
        #     敌人2的碰撞检测
        for i in range(len(e_2_y)):
            screen.blit(enemy_2, (e_2_x[i], e_2_y[i]))
            e_2_x[i] += speed[i]
            e_2_y[i] += 1.5
            print(e_2_y)
            # for j in range(len(e_2_y)):
            key_s = pygame.key.get_pressed()
            if key_s[K_s]:
                screen.blit(hero_power2, (600 - m_hero_power2.width/2, 520))
                if hero_x >= e_2_x[i] + m_enemy_2.width > 600 - m_hero_power2.width/2:
                    e_2_x.pop(i)
                    e_2_y.pop(i)
                    score += 1
                    break
            if e_2_x[i] > hero_x:
                hero_y = 1000
                page = 3
        #     敌人3的碰撞检测
        for i in range(len(e_3_y)):
            screen.blit(enemy_3, (e_3_x[i], e_3_y[i]))
            e_3_x[i] += 0
            e_3_y[i] += 5.5
            print(e_3_y)
            key_space = pygame.key.get_pressed()
            if key_space[K_SPACE]:
                screen.blit(hero_power3, (600 - m_hero_power3.width/2, 520))
                if 580 >= e_3_y[i] > 280:
                    e_3_x.pop(i)
                    e_3_y.pop(i)
                    score += 1
                    break
            if e_3_y[i] > 480:
                hero_y = 1000
                page = 3

        for i in range(len(e_3_y)):
            defen1 = font.render('score:' + str(score), True, PURPLE_COLOR)
            screen.blit(defen1, (80, 10))
            level = font.render('level:' + str(score//10), True, PURPLE_COLOR)
            screen.blit(level, (84, 100))
    if page == 3:
        screen.blit(background, (0, 0))
        screen.blit(end_pitcure, (0, 0))
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 200 < mouse_x < 1100:
                score = 0
                e_1_x.clear()
                e_1_y.clear()
                e_2_x.clear()
                e_2_y.clear()
                e_3_x.clear()
                e_3_y.clear()
                page = 1

    pygame.display.update()
