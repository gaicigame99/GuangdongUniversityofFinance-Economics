import random
import sys
import time

import pygame

from gameRole import *

# Initialize the pygame module
pygame.init()
size = width, height = 480, 852
screen = pygame.display.set_mode(size)
# load the background
bg = pygame.image.load('./images/background.png')
# load the gameover images
gameover = pygame.image.load('./images/gameover.png')
gameover = pygame.transform.scale(gameover, size)
# load the font
font = pygame.font.Font('C:/Windows/Fonts/Arial.ttf', 36)

# create a plane
src = './images/hero.gif'
plane = Plane(src)
# create the bullet
bullet_src = './images/bullet-1.gif'
bullets = []
bullet_time_seed = 0
# create the enemy
enemy_src = './images/enemy-1.gif'
time_seed = 0
enemys = []
enemy_x = 25
enemy_y = -40
enemy = Enemy(enemy_src, enemy_x, enemy_y)
enemys.append(enemy)

#
name = pygame.image.load('./images/name.png')
name_rect = name.get_rect()
namex = 50
namey = 0
life = pygame.image.load('./images/hero.gif')
lifex = 190
lifey = 450
enemy1 = pygame.image.load('./images/enemy-1.gif')
enemy1x = 215
enemy1y = 200
blue_bullet = pygame.image.load('./images/bullet-2.gif')
bullet_x = 236
bullet_y = 250
# load the enemy blow image
enemy_blow1 = pygame.image.load('./images/enemy0_down1.png')
enemy_blow2 = pygame.image.load('./images/enemy0_down2.png')
enemy_blow3 = pygame.image.load('./images/enemy0_down3.png')
enemy_blow4 = pygame.image.load('./images/enemy0_down4.png')
# load the plane blow images
plane_blow1 = pygame.image.load('./images/hero_blowup_n1.png')
plane_blow2 = pygame.image.load('./images/hero_blowup_n2.png')
plane_blow3 = pygame.image.load('./images/hero_blowup_n3.png')
plane_blow4 = pygame.image.load('./images/hero_blowup_n4.png')

# hte position that enemy blow
enemys_blow = []

# the score
score = 0
# the plane crudh single
crush = False
plane_hit_postion = 0, 0
# start the game tag
start_tag = False
while True:

    screen.blit(bg, (0, 0))

    # when bullet hit the enemy plane
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_tag = True
    if start_tag:
        current_time = time.time()
        for enemy in enemys_blow:
            time_zone = current_time - enemy[2]
            if time_zone < 0.5:
                if time_zone > 0.4:
                    screen.blit(enemy_blow4, (enemy[0], enemy[1]))
                    enemys_blow.remove(enemy)
                elif time_zone > 0.3:
                    screen.blit(enemy_blow3, (enemy[0], enemy[1]))
                elif time_zone > 0.2:
                    screen.blit(enemy_blow2, (enemy[0], enemy[1]))
                else:
                    screen.blit(enemy_blow1, (enemy[0], enemy[1]))
        # print(len(enemys_blow))
        # generate the enemys
        if bullet_time_seed == 15:
            # create the bullet
            x, y = pygame.mouse.get_pos()
            bullet = Bullet(bullet_src, x, y)
            bullets.append(bullet)
            bullet_time_seed = 0
        bullet_time_seed += 1
        if time_seed == 25:
            # create the enemy
            enemy_x = random.randint(0, width - 51)
            enemy_y = -40
            enemy = Enemy(enemy_src, enemy_x, enemy_y)
            enemys.append(enemy)
            time_seed = 0
            # print(len(enemys),'\n')
        time_seed += 1

        if not crush:
            # draw the plane object
            x, y = pygame.mouse.get_pos()
            plane.set_x(x)
            plane.set_y(y)
            screen.blit(plane.plane, (plane.x, plane.y))
            # draw the enemy
            for enemy in enemys:
                screen.blit(enemy.enemy, (enemy.x, enemy.y))
                enemy.y += 1
                # print(len(enemys))
                if enemy.y > height:
                    enemys.remove(enemy)
                if enemy.y + enemy.width > plane.y and \
                    enemy.x > plane.x and \
                        (enemy.x + enemy.width) < (plane.x + plane.plane_rect.width):
                    # print('hit the plane')
                    plane_hit_time = time.time()
                    crush = True
                    plane_hit_postion = plane.x, plane.y
                    # exit()
                # test the enemy crash plane
                # print(len(enemys))

            for bullet in bullets:
                tag = False
                for enemy in enemys:
                    # bullet and enemy test
                    # if bullet hit the enemy. the enemy blow
                    if bullet.y < (enemy.y + enemy.height) and \
                            enemy.x < bullet.x < (enemy.x + enemy.width - bullet.width) and \
                            enemy.y < plane.y:
                        bullets.remove(bullet)
                        enemys_blow.append((bullet.x, bullet.y, time.time()))
                        # print(enemys_blow)
                        enemys.remove(enemy)
                        score += 1
                        tag = True
                        break

                screen.blit(bullet.bullet, (bullet.x, bullet.y))
                bullet.y -= 5
                if bullet.y < 0 and not tag:
                    bullets.remove(bullet)

        else:
            # when the plane blow
            time_zone = current_time - plane_hit_time
            # print(time_zone)
            if time_zone < 0.4:
                if time_zone > 0.3:
                    screen.blit(plane_blow4, plane_hit_postion)
                elif time_zone > 0.2:
                    screen.blit(plane_blow3, plane_hit_postion)
                elif time_zone > 0.1:
                    screen.blit(plane_blow2, plane_hit_postion)
                else:
                    screen.blit(plane_blow1, plane_hit_postion)
            else:
                exit()
        score_text = font.render('Score:{}'.format(score), True, (0, 0, 255))
        screen.blit(score_text, (0, 0))
    else:
        screen.blit(name, (namex, namey))
        screen.blit(life, (lifex, lifey))
        screen.blit(enemy1, (enemy1x, enemy1y))
        screen.blit(blue_bullet, (bullet_x, bullet_y))
        start_text = font.render("Press the Mouse", True, (0, 0, 255))
        screen.blit(start_text, (105, 700))
        second_text = font.render("and Start the Game", True, (0, 0, 255))
        screen.blit(second_text, (80, 740))
    pygame.display.flip()
