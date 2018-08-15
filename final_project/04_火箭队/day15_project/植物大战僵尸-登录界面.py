import pygame
import random

pygame.init()

# 文字
# font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 20)
# str = """
#       健康游戏忠告
# 抵制不良游戏，拒绝盗版游戏。
# 注意自我保护，谨防受骗上当。
# 适度游戏益脑，沉迷游戏伤身。
# 合理安排时间，享受健康生活。
# """
# print(str)
# heath_text = font.render(str, True, (255, 255, 255, 255))

# 游戏背景
screen = pygame.display.set_mode((850, 600))
game_background = pygame.image.load("background.jpg")
#game_background = pygame.transform.scale(game_background, (850, 600))

move_list = {}

mv_bg = pygame.image.load("bg1.png")
mv_bg = pygame.transform.scale(mv_bg, (850, 600))
bgx = 0
bgy = 0
move_list["背景位置"] = [bgx, bgy]

# 摆放按钮
# 冒险模式
star1_btn = pygame.image.load("star1.png")
star1_btn = pygame.transform.scale(star1_btn, (267, 80))
star1_rect = star1_btn.get_rect()
# 点击变亮
star2_btn = pygame.image.load("star2.png")
star2_btn = pygame.transform.scale(star2_btn, (267, 80))
star2_rect = star2_btn.get_rect()
# 退出按钮
game_quit_btn = pygame.image.load("quit_sel.png")
#game_quit_btn = pygame.transform.scale(game_quit_btn, (267, 80))
game_quit_rect = game_quit_btn.get_rect()
# # 点击变亮
# star4_btn = pygame.image.load("star4.png")
# star4_btn = pygame.transform.scale(star4_btn, (267, 80))
# star4_rect = star4_btn.get_rect()
# # 生存模式
# star5_btn = pygame.image.load("star5.png")
# star5_btn = pygame.transform.scale(star5_btn, (267, 80))
# star5_rect = star5_btn.get_rect()
# # 点击变亮
# star6_btn = pygame.image.load("star6.png")
# star6_btn = pygame.transform.scale(star6_btn, (267, 80))
# star6_rect = star6_btn.get_rect()

# 按钮1的位置
btx1 = 488
bty1 = 85
move_list["按钮1位置"] = [btx1, bty1]

# 按钮2的位置
btx2 = 488
bty2 = 85
move_list["按钮2位置"] = [btx2, bty2]

# 退出按钮的位置
btx3 = 700
bty3 = 520
move_list["退出按钮位置"] = [btx3, bty3]

speedx = 0
speedy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(game_background, (0, 0))
    screen.blit(mv_bg, (move_list["背景位置"][0], move_list["背景位置"][1]))
    # screen.blit(heath_text, (100, 300))
    # screen.blit(star1_btn, (btx1, bty1))
    # screen.blit(star3_btn, (btx1, bty1 + star1_rect.height))
    # screen.blit(star5_btn, (btx1, bty1 + star1_rect.height + star3_rect.height))

    a, b, c = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.blit(game_quit_btn, (move_list["退出按钮位置"][0], move_list["退出按钮位置"][1]))
    # 点击退出游戏
    if mouse_x > btx3 and mouse_x < btx3 + game_quit_rect.width and mouse_y > bty3 and mouse_y < bty3 + game_quit_rect.height and a:
        print("退出游戏")
        exit()
    else:
        pass

    # 点击按钮开始进入下一界面
    if mouse_x > btx1 and mouse_x < btx1+star1_rect.width and mouse_y> bty1 and mouse_y < bty1 + star1_rect.height:
        screen.blit(star2_btn, (move_list["按钮2位置"][0], move_list["按钮2位置"][1]))
        if a:
            speedx = 0
            speedy = -50
    else:
        screen.blit(star1_btn, (move_list["按钮1位置"][0], move_list["按钮1位置"][1]))

    for i in move_list:
        move_list[i][0] += speedx
        move_list[i][1] += speedy

    if move_list[i][1] < -800:
        speedy = 0

    pygame.display.update()

