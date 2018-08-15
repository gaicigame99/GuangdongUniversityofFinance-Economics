import pygame
import Marble_game,game,football_game,GoldMiner,Cargame,PlantWar,pushgame

class Setting(object):

	def __init__(self):

		#记录从第0-6游戏
		self.count=0

		#7个游戏
		self.length=7
		#
		self.images0=pygame.image.load(r'images\g1.jpg')
		self.images1=pygame.image.load(r'images\g2.jpg')
		self.images2=pygame.image.load(r'images\g3.jpg')
		self.images3=pygame.image.load(r'images\g4.jpg')
		self.images4=pygame.image.load(r'images\g5.jpg')
		self.images5=pygame.image.load(r'images\g6.jpg')
		self.images6=pygame.image.load(r'images\g7.jpg')
		
		self.images=[self.images0,self.images1,self.images2,self.images3,self.images4,self.images5,self.images6]

		#设置字体
		self.font=pygame.font.Font("C:\Windows\Fonts\Calibriz.ttf",50)
		self.start_images=self.font.render('Play Game By Space',True,(0,0,0))

		#映射游戏
		self.dic={'0':Marble_game,'1':game,'2':football_game,'3':GoldMiner,'4':Cargame,'5':PlantWar,'6':pushgame}



