import pygame
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((480, 852))

enemy = pygame.image.load("images\enemy0.png")

hero = pygame.image.load("images\hero.gif")

background = pygame.image.load(r"images\background.png")

bullet = pygame.image.load(r"images\bullet1.png")

bgm = pygame.mixer.Sound("sound\game_music.ogg")

e_bullet = pygame.image.load(r"images\bullet2.png")

font1 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 36)
font2 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 100)


enemy_down1 = pygame.image.load(r"images\enemy0_down1.png")
enemy_down2 = pygame.image.load(r"images\enemy0_down2.png")
enemy_down3 = pygame.image.load(r"images\enemy0_down3.png")
enemy_down4 = pygame.image.load(r"images\enemy0_down4.png")

hero_down1 = pygame.image.load(r"images\hero_blowup_n1.png")
hero_down2 = pygame.image.load(r"images\hero_blowup_n2.png")
hero_down3 = pygame.image.load(r"images\hero_blowup_n3.png")
hero_down4 = pygame.image.load(r"images\hero_blowup_n4.png")

h_x = 100
h_y = 100

score = 0

b_x = []
b_y = []
b_time = 4
b_speed = 1
e_speed = 1
e_b_speed = 1.5
e_b_time = 30
i = 0

enemy_num = random.randint(3, 6)
enemy_posx = []
enemy_posy = []
e_b_posx = []
e_b_posy = []
button_x = 0
button_y = 0

h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height

e_rect = enemy.get_rect()
e_width = e_rect.width
e_height = e_rect.height

b_rect = bullet.get_rect()
b_width = b_rect.width
b_height = b_rect.height


for i in range(enemy_num):
    a = random.randint(0, 430)
    b = random.randint(0, 100)
    enemy_posx.append(a)
    enemy_posy.append(b)


def get_grade(n_font, n_score, n_screen):
    text_score = n_font.render("分数:" + str(n_score), True, (0, 0, 0))
    n_screen.blit(text_score, (330, 46))


def gameover(n_font, n_screen):
    text_score = n_font.render("GAMEOVER!", True, (255, 0, 0))
    n_screen.blit(text_score, (30, 300))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    h_x, h_y = pygame.mouse.get_pos()

    bgm.play()

    if b_time:
        b_time -= 1
    else:
        b_x.append(h_x)
        b_y.append(h_y)
        b_time = 30

    screen.blit(background, (0, 0,))

    screen.blit(hero, (h_x - h_width / 2, h_y - h_height / 2))

    for i in range(len(b_x)):
        screen.blit(bullet, (b_x[i], b_y[i] - h_height / 2))
        b_y[i] -= b_speed
        # 英雄机子弹优化
        if b_x[i] < 0:
            b_x.pop(i - 1)
            b_x.pop(i - 1)

    get_grade(font1, score, screen)

    # 敌机位置
    for j in range(enemy_num):
        e_b_posx.append(enemy_posx[j])
        e_b_posy.append(enemy_posy[j])

        screen.blit(enemy, (enemy_posx[j], enemy_posy[j]))
        enemy_posy[j] += e_speed

        screen.blit(e_bullet, (e_b_posx[j] + e_width / 2, e_b_posy[j] + e_height / 2))
        e_b_posy[j] += e_b_speed
        # 敌机子弹优化
        if e_b_posy[j] > 852:
            e_b_posx.pop(j - 1)
            e_b_posy.pop(j - 1)

        screen.blit(e_bullet, (e_b_posx[j] + e_width / 2, e_b_posy[j] + e_height / 2))

        for t in range(len(b_x)):
            # 英雄机碰撞检测
            if e_b_posx[j] + h_width / 2 > h_x and e_b_posx[j] - h_width / 2 < h_x and \
                    e_b_posy[j] - h_height / 2 < h_y and e_b_posy[j] + h_height / 2 > h_y:
                screen.blit(hero_down1, (h_x - h_width / 2, h_y - h_height / 2))

                screen.blit(hero_down2, (h_x - h_width / 2, h_y - h_height / 2))

                screen.blit(hero_down3, (h_x - h_width / 2, h_y - h_height / 2))

                screen.blit(hero_down4, (h_x - h_width / 2, h_y - h_height / 2))

                gameover(font2, screen)

            # 英雄机碰撞检测
            if enemy_posx[j] + h_width / 2 > h_x and enemy_posx[j] - h_width / 2 < h_x and \
                    enemy_posy[j] - h_height / 2 < h_y and enemy_posy[j] + h_height / 2 > h_y:
                screen.blit(hero_down1, (h_x - h_width / 2, h_y - h_height / 2))

                screen.blit(hero_down2, (h_x - h_width / 2, h_y - h_height / 2))

                screen.blit(hero_down3, (h_x - h_width / 2, h_y - h_height / 2))

                screen.blit(hero_down4, (h_x - h_width / 2, h_y - h_height / 2))

                gameover(font2, screen)

            # 敌机碰撞检测
            if b_x[t] + e_width > enemy_posx[j] and b_x[t] - e_width < enemy_posx[j] and \
                    b_y[t] - e_height < enemy_posy[j] and b_y[t] + e_height > enemy_posy[j]:
                screen.blit(enemy_down1, (enemy_posx[j], enemy_posy[j]))

                screen.blit(enemy_down2, (enemy_posx[j], enemy_posy[j]))

                screen.blit(enemy_down3, (enemy_posx[j], enemy_posy[j]))

                screen.blit(enemy_down4, (enemy_posx[j], enemy_posy[j]))

                score += 1

                enemy_posx[j] = random.randint(0, 430)
                enemy_posy[j] = random.randint(-50, 50)

                e_b_posx[j] = enemy_posx[j]
                e_b_posy[j] = enemy_posy[j]

    pygame.display.update()


