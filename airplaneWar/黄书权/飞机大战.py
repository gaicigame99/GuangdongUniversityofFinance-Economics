import pygame
import random
pygame.init()
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)
screen = pygame.display.set_mode((500,800))
bj = pygame.image.load(r"images\background.png")
bj = pygame.transform.scale(bj, (500, 800))

h_plane = pygame.image.load(r"images\hero2.png")
h_rect = h_plane.get_rect()
h_width = h_rect.width
h_height = h_rect.height

h_d = pygame.image.load(r"images\bullet.png")
hd_rect = h_d.get_rect()
hd_width = hd_rect.width


e_x = list()
e_y = list()
e_d = pygame.image.load(r"images\enemy1.png")
ed_rect = e_d.get_rect()
ed_x = ed_rect.width
ed_y = ed_rect.height

se_x = list()
se_y = list()
se_d = pygame.image.load(r"images\enemy0.png")
sed_rect = se_d.get_rect()
sed_x = sed_rect.width
sed_y = sed_rect.height

e_db = pygame.image.load(r"images\enemy1_down3.png")
se_db = pygame.image.load(r"images\enemy0_down3.png")

e_coun = 2
for i in range(e_coun):
    e_x.append(random.randint(0, 480))
    e_y.append(random.randint(-70, 0))
    se_x.append(random.randint(0, 480))
    se_y.append(random.randint(-60, 0))

l_x = list()
l_y = list()
el_x = list()
el_y = list()
speed = 20
e_speed = 0.01
p_l = 2
p_time = p_l
score = 0
blood_value = 5
blood = blood_value
if score % 5 == 0:
    e_speed += 0.01
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    h_x, h_y = pygame.mouse.get_pos()
    if p_time:
        p_time -= 1
    else:
        l_x.append(h_x-hd_width/2)
        l_y.append(h_y-h_height/2)
        p_time = p_l
    screen.blit(bj, (0, 0))
    score1 = font.render("score:" + str(score), True, (255, 255, 255))
    screen.blit(h_plane, (h_x-h_width/2, h_y-h_height/2))
    for i in range(len(l_x)):
        screen.blit(h_d, (l_x[i], l_y[i]))
        l_y[i] -= speed
        for j in range(e_coun):
            if e_x[j] < l_x[i] < e_x[j] + ed_x and \
                e_y[j] < l_y[i] < e_y[j] + ed_y:
                if blood:
                    blood -= 1
                    l_x[i] = -100
                    l_y[i] = -100
                else:
                    score = score + 1
                    screen.blit(e_db, (e_x[j], e_y[j]))
                    e_x[j] = random.randint(0, 400)
                    e_y[j] = -100
                    l_x[i] = -100
                    l_y[i] = -100
                    blood = blood_value
            elif e_y[j] > 800:
                e_x[j] = random.randint(0, 400)
                e_y[j] = -100
            elif se_x[j] < l_x[i] < se_x[j] + sed_x and \
                se_y[j] < l_y[i] < se_y[j] + sed_y:
                score = score + 1
                screen.blit(se_db, (se_x[j], se_y[j]))
                se_x[j] = random.randint(0, 480)
                se_y[j] = -100
                # 子弹消失
                l_x[i] = -100
                l_y[i] = -100
            elif se_y[j] > 800:
                se_x[j] = random.randint(0, 480)
                se_y[j] = -100
            else:
                screen.blit(e_d, (e_x[j], e_y[j]))
                e_y[j] += e_speed
                screen.blit(se_d, (se_x[j],se_y[j]))
                se_y[j] += e_speed
    screen.blit(score1, (0, 20))

    pygame.display.update()
