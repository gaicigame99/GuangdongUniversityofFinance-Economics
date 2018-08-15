import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((600,600))
bg = pygame.transform.scale(pygame.image.load("xingkong.jpg"),(600,600))
font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",36)
jiemian = pygame.transform.scale(pygame.image.load("jiemian.jpg"),(600,600))
button1 = pygame.image.load("1.png")
button2 = pygame.image.load("3.png")
button3 = pygame.image.load("2.png")


class interface(object):
    def __init__(self,screen,fengmian):
        self.screen = screen
        self.fengmian = fengmian
        self.x = 0
        self.y = 0
        self.rect = self.fengmian.get_rect()
    def show(self):
        self.screen.blit(self.fengmian,(self.x,self.y))
    def move(self):
        if self.y > -self.rect.height:
            self.y -=3

jiemian = interface(screen,jiemian)
start_game = False
isjiemian = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(bg,(0,0))
    jiemian.show()

    if start_game==False:
        screen.blit(button1, (80, 130))
        screen.blit(button2, (80, 230))
        screen.blit(button3, (100, 330))
        a,b,c =pygame.mouse.get_pressed()
        x,y= pygame.mouse.get_pos()
        print(x,y)
        if 220<x<360 and 276<y<310 and a:#开始游戏
            isjiemian =True

        if 220 < x < 360 and 480 < y < 520 and a:#结束游戏
            exit()


        if isjiemian:
            jiemian.move()

            if jiemian.y <= -jiemian.rect.height:
                print("2")
                start_game = True
    if start_game:
        print("1")






    pygame.display.update()