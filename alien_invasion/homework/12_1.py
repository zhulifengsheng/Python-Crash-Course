import sys

import pygame
from pygame.sprite import Sprite, Group

class Bullet(Sprite):
	
	def __init__(self, screen, ship):
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, 8, 5)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right
		self.color = (255, 0, 0)
		self.speed_factor = 1
		
	def update(self):
		self.rect.x += self.speed_factor
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		
		
class Ship():
	
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
def check_keydown_events(event, screen, ship, bullets):
	if event.key == pygame.K_UP and ship.rect.top > 0:
		ship.rect.centery -= 1
	elif event.key == pygame.K_DOWN and ship.rect.bottom < ship.screen_rect.bottom:
		ship.rect.centery += 1
	elif event.key == pygame.K_SPACE:
		new_bullet = Bullet(screen, ship)
		bullets.add(new_bullet)
	
def check_events(screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, screen, ship, bullets)
		 
def run_game():
	
	pygame.init()
	screen = pygame.display.set_mode((600, 450))
	pygame.display.set_caption('TEST')
	bg_color = (0, 0, 255)
	ship = Ship(screen)
	bullets = Group()
	
	while True:
		check_events(screen, ship, bullets)
		screen.fill(bg_color)
		ship.blitme()
		for bullet in bullets:
			if bullet.rect.right >= 600:
				bullets.remove(bullet)
			
				
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		bullets.update()
		pygame.display.flip()
	
run_game()
