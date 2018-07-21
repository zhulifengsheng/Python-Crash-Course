import sys

import pygame
from pygame.sprite import Sprite, Group
from random import randint

class Star(Sprite):
	
	def __init__(self,screen):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		self.rect.y += 1

def get_number_stars_x(star_width):
	available_space_x = 1280 - 2 * star_width
	number_stars_x = int(available_space_x / (2 * star_width))
	return number_stars_x

def get_number_rows(star_height):
	available_space_y = 750
	number_rows = int(available_space_y / (2 * star_height))
	return number_rows

def create_star(screen, stars, star_number, row_number):
	star = Star(screen)
	star_width = star.rect.width
	star.x = star_width + 2 * star_width * star_number
	star.rect.x = star.x
	star.rect.y = star.rect.height + 2 * star.rect.height * row_number
	stars.add(star)

def create_fleet(screen, stars):
	star = Star(screen)
	number_stars_x = get_number_stars_x(star.rect.width)
	number_rows = get_number_rows(star.rect.height)
	for row_number in range(number_rows):
		for star_number in range(randint(0,number_stars_x)):
			create_star(screen, stars, randint(0, number_stars_x), randint(0, number_rows))
		
def run_game():
	
	pygame.init()
	screen = pygame.display.set_mode((1280,700))
	pygame.display.set_caption('ABC')
	bg_color = (120, 150, 20)
	stars = Group()
	create_fleet(screen, stars)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		stars.draw(screen)
		stars.update()
		for star in stars.copy():
			if star.rect.top > 700:
				flag = 1
				stars.remove(star)
		
		if flag:
			star = Star(screen)
			number_stars_x = get_number_stars_x(star.rect.width)
			for star_number in range(number_stars_x):
				create_star(screen, stars, star_number, 0)
			flag = 0
		
		pygame.display.flip()
		
run_game()
		
