l = 10
for i in range(l):
    print(i)
    l -= 1


 # for i in range(5):
        #     op_blood = font.render(str(e_blood[i]), True, (0, 0, 0))
        #     if e_blood[i] >= 150:
        #         screen.blit(enemy[i], (ex[i], ey[i]))
        #         screen.blit(op_blood, (ex[i] + 10, ey[i] - 15))
        #     if 100 <= e_blood[i] < 150:
        #         screen.blit(enemydown[0], (ex[i], ey[i]))
        #         screen.blit(op_blood, (ex[i] + 10, ey[i] - 15))
        #     if 50 <= e_blood[i] < 100:
        #         screen.blit(enemydown[1], (ex[i], ey[i]))
        #         screen.blit(op_blood, (ex[i] + 10, ey[i] - 15))
        #     if 10 <= e_blood[i] < 50:
        #         screen.blit(enemydown[2], (ex[i], ey[i]))
        #         screen.blit(op_blood, (ex[i] + 10, ey[i] - 15))
        #     if 0 < e_blood[i] < 10:
        #         screen.blit(enemydown[3], (ex[i], ey[i]))
        #         screen.blit(op_blood, (ex[i] + 10, ey[i] - 15))
        #     if e_blood[i] == 0:
        #         ex[i] = random.randint(0, 495 - 50)
        #         ey[i] = random.randint(-100, 0)
        #         if level == 0:
        #             e_blood[i] = 200
        #         if level == 1:
        #             e_blood[i] = 250
        #         kill += 1
        #     ey[i] += 0.3