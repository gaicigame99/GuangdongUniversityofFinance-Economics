from pygame.locals import *
import pygame
import random
import time
pygame.init()


bigin=pygame.image.load(r"kk\bigin.png")
bigin=pygame.transform.scale(bigin,(500,800))


pygame.mixer.init()
game_music=pygame.mixer.Sound(r"dadisou\jimia.ogg")




screen = pygame.display.set_mode((500,800))#屏幕

start_num = 0
fx = []
fy = []
for i in range(5):
    fx.append(230)
    fy.append(800-32)

#显示开始游戏封面
def start_cover(screen):
    cover = pygame.image.load(r"kk\cover.jpg")#封面
    screen.blit(cover, (0, 0))
    flower = pygame.image.load(r"kk\flower.png")  # 花朵
    for i in range(5):
        if fx[i] <= 0 or fx[i] >= 500 or fy[i] <= 0:
            fx[i] = 230
            fy[i] = 800-32
        screen.blit(flower, (fx[i],fy[i]))
        fx[0] -= 0.5
        fy[0] -= 1
        fx[1] -= 0.5
        fy[1] -= 2.5
        fy[2] -= 1.5
        fx[3] += 0.5
        fy[3] -= 2
        fx[4] += 0.5
        fy[4] -= 1


    font_0 = pygame.font.Font("C:\windows\Fonts\SimHei.ttf", 25)  # 文字
    f_0 = font_0.render("请点击相应按钮开始游戏：", True, (255, 255, 255))
    screen.blit(f_0, (30, 70))
    font = pygame.font.Font("C:\windows\Fonts\SimHei.ttf", 40)
    f_1 = font.render("1.打地鼠", True, (255, 255, 255))
    screen.blit(f_1, (120, 180))
    f_1 = font.render("2.欢乐跳一跳",True,(255,255,255))
    screen.blit(f_1, (120,250))
    f_1 = font.render("3.泡泡龙", True, (255, 255, 255))
    screen.blit(f_1, (120, 320))

    button_start_1 = pygame.image.load(r"kk\button_start_1.png")  # 开始按钮1
    screen.blit(button_start_1, (330, 180))
    button_start_2 = pygame.image.load(r"kk\button_start_1.png")  # 开始按钮2
    screen.blit(button_start_2, (400,255))
    button_start_3 = pygame.image.load(r"kk\button_start_1.png")  # 开始按钮3
    screen.blit(button_start_3, (330, 325))

    x, y = pygame.mouse.get_pos()#获取鼠标位置
    pressed_array = pygame.mouse.get_pressed()
    for index in range(len(pressed_array)):
        if pressed_array[index]:
            if index == 0:
                if x >= 330 and x <= 330 + 32 and y >= 180 and y <= 180 + 32:  # 选择游戏
                    return 1
                if x >= 400 and x <= 400 + 32 and y >= 255 and y <= 255 + 32:
                    return 2
                if x >= 330 and x <= 330 + 32 and y >= 325 and y <= 325 + 32:
                    return 3


def func():
    pygame.display.set_caption("解压游戏平台")
    game_music.play()
    screen = pygame.display.set_mode((500, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        start_num = start_cover(screen)#开始页面

        if start_num == 1:#选择第一个游戏
            game_music.stop()
            import 打地鼠
            打地鼠.func( )
        if start_num == 2:#选择第二个游戏
            game_music.stop()
            import 跳一跳
            跳一跳.tyt()
        if start_num == 3:#选择第三个游戏
            game_music.stop()
            import 泡泡龙
            泡泡龙.func()
        pygame.display.update()

func()