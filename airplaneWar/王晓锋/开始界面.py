import pygame

screen = pygame.display.set_mode((500, 800))

background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background, (500, 800))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
