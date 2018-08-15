
import pygame
import setting

pygame.init()
s=setting.Setting()

screen=pygame.display.set_mode((800,600))


def GameBegin():
	s.dic[str(s.count)].begin()

def change(key):
	if key == pygame.K_LEFT:
		s.count-=1
		s.count=s.count%s.length
		screen.blit(s.images[s.count],(0,0))
				
	elif key == pygame.K_RIGHT:
		s.count+=1
		s.count=s.count%s.length
		screen.blit(s.images[s.count],(0,0))

	elif key == pygame.K_SPACE:
		GameBegin()
		#pass



while True:
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			exit()
		elif event.type == pygame.KEYDOWN:
			change(event.key)
	if s.count==0:
		screen.blit(s.images0,(0,0))
	screen.blit(s.start_images,(200,300))
	pygame.display.update()
	
