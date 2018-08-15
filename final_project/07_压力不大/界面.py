from pygame.locals import *
import pygame
import random
import time
pygame.init()
pygame.mixer.init()
game_music=pygame.mixer.Sound(r"dadisou\jimia.ogg")

screen = pygame.display.set_mode((500, 800))
bigin=pygame.image.load(r"kk\bigin.png")

bigin=pygame.transform.scale(bigin,(500,800))
logo=pygame.image.load(r"kk\logo.png")
logo=pygame.transform.scale(logo,(150,200))
font = pygame.font.Font("C:\windows\Fonts\SimHei.ttf", 30)
font1 = pygame.font.Font("C:\windows\Fonts\SimHei.ttf", 50)
font2=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",17)

game_music.play()
while True:
    pygame.display.set_caption("解压游戏平台")
    screen.blit(bigin,(0,0))
    screen.blit(font.render("压力不大工作室", True, (255, 255, 255)),(20,20))
    screen.blit(font1.render("解压游戏平台", True, (255, 100, 100)), (100,200))
    screen.blit(logo, (170,250))
    screen.blit(font2.render("抵制不良游戏，拒绝盗版游戏。 注意自我保护，谨防受骗上当。", True, (0, 0, 0)), (10, 690))
    screen.blit(font2.render("适度游戏益脑，沉迷游戏伤身。 合理安排时间，享受健康生活。", True, (0, 0, 0)), (10, 710))
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 170<=x<=1750+150 and 250<=y<=450:
                game_music.stop()
                import 封面.py
                封面.func()
    pygame.display.update()