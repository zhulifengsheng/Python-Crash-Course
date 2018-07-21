import sys

import pygame
from pygame.sprite import Group, Sprite
from random import randint

class Ball(Sprite):
	
	def __init__(self, screen):
		
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, 40, 40)
		self.screen_rect = screen.get_rect()
		self.rect.top = self.screen_rect.top
		self.rect.centerx = randint(20, 880)
		self.color = 60, 60, 60 
		self.speed_factor = 1
	
	def update(self):
		self.rect.y += self.speed_factor
	
	def draw_ball(self):
		pygame.draw.rect(self.screen, self.color, self.rect)	

class Ship():
	
	def __init__(self, screen):
		
		self.screen = screen
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.ship_speed_factor = 2
		
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ship_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.ship_speed_factor
			
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
def check_keydown_events(event, ship):
	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_events(event, ship):
	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_collision(ship, balls):
	
	if pygame.sprite.spritecollideany(ship, balls):
		balls.empty()
		
def run_game():
	
	count = 0
	pygame.init()
	screen = pygame.display.set_mode((900, 600))
	pygame.display.set_caption("ABC")
	bg_color = (10, 185, 45)
	balls = Group()
	ship = Ship(screen)
	
	while True:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ship)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)
				
		if count < 3:
			if len(balls) < 1:
				new_ball = Ball(screen)
				balls.add(new_ball)	
				
			ship.update()
			balls.update()
			
			check_collision(ship, balls)
			for ball in balls.copy():
				if ball.rect.bottom >= 600:
					balls.remove(ball)
					count += 1
			
		screen.fill(bg_color)
		for ball in balls.sprites():
			ball.draw_ball()
		ship.blitme()
		pygame.display.flip()

run_game()
