import pygame

pygame.init()


class Plane(object):
    def __init__(self, src):
        self.plane = pygame.image.load(src)
        self.plane_rect = self.plane.get_rect()
        self.x = 0
        self.y = 0


    def set_x(self, new_x):
        self.x = new_x - self.plane_rect.width / 2

    def set_y(self, new_y):
        self.y = new_y - self.plane_rect.height / 2


class Enemy(object):
    def __init__(self, src, x, y):
        self.enemy = pygame.image.load(src)
        self.enemy_rect = self.enemy.get_rect()
        self.x = x
        self.y = y
        self.width = self.enemy_rect.width
        self.height = self.enemy_rect.height


class Bullet(object):
    def __init__(self, src, x, y):
        self.bullet = pygame.image.load(src)
        self.bullet_rect = self.bullet.get_rect()
        self.x = x - self.bullet_rect.width / 2
        self.y = y - self.bullet_rect.height
        self.width = self.bullet_rect.width
