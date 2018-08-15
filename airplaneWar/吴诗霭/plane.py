import pygame
import random

pygame.init()
pygame.mixer.init()

bgm = pygame.mixer.Sound("sound\game_music.ogg")
bgm.play()

screen = pygame.display.set_mode((495, 800))

font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",24)
WHITE = (255,255,255)# 元组

hero = pygame.image.load("images\hero.gif")
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))
bullet = pygame.image.load(r"images\bullet.png")

enemy0 = pygame.image.load(r"images\enemy0.png")
enemy0_down1 = pygame.image.load(r"images\enemy0_down1.png")
enemy0_down2 = pygame.image.load(r"images\enemy0_down2.png")
enemy0_down3 = pygame.image.load(r"images\enemy0_down3.png")
enemy0_down4 = pygame.image.load(r"images\enemy0_down4.png")


h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height
hx = 100
hy = 100

bl_rect = bullet.get_rect()
bl_r = bl_rect.width / 2
bl_x = []
bl_y = []
bl_speed = 3
bl_v = 50
bl_time = bl_v

e_rect = enemy0.get_rect()
e_w = e_rect.width
e_h = e_rect.height
e_x = []
e_y = []
e_blood = [] # 生命值为3
e_p = []
e_n = 4
e_speed = 1
enemy0_photos = [enemy0_down4,enemy0_down3,enemy0_down2,enemy0_down1,enemy0]
while True:
    if len(e_y) == e_n:
        break
    e_y.append(random.randint(-40,-10) * 10)
while True:
    if len(e_x) == e_n:
        break
    e_x.append(random.randint(5,45) * 10)
#   敌机添加血槽
while True:
    if len(e_blood) == e_n:
        break
    e_blood.append((len(enemy0_photos) - 1))
#   敌机添加默认图片
while True:
    if len(e_p) == e_n:
        break
    e_p.append(enemy0)

score = 0

while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # pressed_keys= pygame.key.get_pressed()
        # if pressed_keys[pygame.K_SPACE]:
        #     bl_x.append(hx - bl_r)
        #     bl_y.append(hy - h_height / 2 - bl_r)
        #     print(bl_y)

    # for i in range(len(bl_x)):
    #     if bl_y[i] <= -100:
    #         bl_y[i] = -100
    #     else:
    #         bl_y[i] -= bl_speed
    #     screen.blit(bullet, (bl_x[i], bl_y[i] ))
    hx, hy = pygame.mouse.get_pos()

    #   子弹发射
    if bl_time:
        bl_time -= 1
    else:
        bl_x.append(hx - bl_r)
        bl_y.append(hy - h_height / 2 - bl_r)
        bl_time = bl_v
    for i in range(len(bl_x)):
        screen.blit(bullet, (bl_x[i], bl_y[i]))
        bl_y[i] -= bl_speed

    #   敌机
    for i in range(e_n):
        e_y[i] += e_speed
        if e_y[i] >= 800:
            e_y[i] = random.randint(-20,-10) * 10
            e_x[i] = random.randint(5,45) * 10

        e_p[i] = enemy0_photos[e_blood[i]]
        pygame.draw.line(screen, (255,0,0), (e_x[i], e_y[i] + e_h + 6),(e_x[i] + e_blood[i] * 15, e_y[i] + e_h + 6) , 6)
        pygame.draw.line(screen, WHITE, (e_x[i] + e_blood[i] * 15, e_y[i] + e_h + 6), (e_x[i] + 4 * 15, e_y[i] + e_h + 6), 6)

        if e_blood[i] == 0:
            e_p[i] = enemy0_photos[e_blood[i]]
            screen.blit(e_p[i], (e_x[i], e_y[i]))
            e_y[i] = random.randint(-200, -100)
            e_x[i] = random.randint(5, 45) * 10
            e_blood[i] = 4
            score += 1
            print(e_blood)

        for j in range(len(bl_x)):
            if (e_x[i] - bl_r) <= bl_x[j] <= (e_x[i] + e_w + bl_r) and e_y[i] <= bl_y[j] <= (e_y[i] + e_h + bl_r):
                e_blood[i] -= 1
                bl_y[j] = -100

        screen.blit(e_p[i], (e_x[i], e_y[i]))

    # 得分 & 关卡

    screen.blit(hero, (hx - h_width/2, hy - h_height/2))
    use_score ="    Score:" + str(score)
    text1 = font.render(use_score, True, (255, 255, 255))
    screen.blit(text1, (0, 750))
    pygame.display.update()