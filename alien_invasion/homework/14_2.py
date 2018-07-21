import sys

import pygame
import pygame.font
from pygame.sprite import Sprite, Group

class GameStats():
	
	def __init__(self):
		self.game_active = False
		self.count = 0
		self.speed_factor = 2
	
	def initialize(self):
		self.ship_speed_factor = 1
		self.enemy_speed_factor = 1
		self.bullet_speed_factor = 2
		
	def increase_speed(self):
		self.ship_speed_factor *= self.speed_factor
		self.enemy_speed_factor *= self.speed_factor
		self.bullet_speed_factor *= self.speed_factor
	
class Button():
	
	def __init__(self, screen, msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, 
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class Ship():
	
	def __init__(self, stats, screen):
		self.screen = screen
		self.stats = stats
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery

		self.moving_up = False
		self.moving_down = False
	
	def update(self): 
		if self.moving_up and self.rect.top > 0 :
			self.rect.centery -= self.stats.ship_speed_factor
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.stats.ship_speed_factor
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def ship_center(self):
		self.rect.centery = self.screen_rect.centery
		
class Enemy(Sprite):
	
	def __init__(self, stats, screen):
		super().__init__()
		self.screen = screen
		self.stats = stats
		self.rect = pygame.Rect(0, 0, 10, 80)
		self.screen_rect = screen.get_rect()
		self.rect.centery = self.screen_rect.centery
		self.rect.right = self.screen_rect.right
		self.color = 100, 50, 110
		self.fleet_direction = 1
		
	def check_edges(self):
		if self.rect.top <= self.screen_rect.top:
			return True
		elif self.rect.bottom >= self.screen_rect.bottom:
			return True
			
	def update(self):
		self.rect.y += self.stats.enemy_speed_factor * self.fleet_direction
	
	def draw_enemy(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		
class Bullet(Sprite):
	
	def __init__(self, stats, screen, ship):
		super().__init__()
		self.screen = screen
		self.stats = stats
		self.rect = pygame.Rect(0, 0, 15, 3)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right
		self.color = 60, 60, 60

	def update(self):
		self.rect.x += self.stats.bullet_speed_factor
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

def check_events(screen, ship, stats, play_button, bullets, enemies):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, stats, screen, bullets, ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(screen, play_button, ship, enemies, bullets, 
				mouse_x, mouse_y, stats)

def check_play_button(screen, play_button, ship, enemies, bullets, mouse_x, 
		mouse_y, stats):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		stats.initialize()
		pygame.mouse.set_visible(False)
		stats.count = 0
		stats.game_active = True
		enemies.empty()
		bullets.empty()
		create_enemy(stats, screen, enemies)
		ship.ship_center()

def check_keydown_events(event, stats, screen, bullets, ship):
	if event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_buttle(bullets, stats, screen, ship)

def check_keyup_events(event, ship):
	if event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def fire_buttle(bullets, stats, screen, ship):	
	new_bullet = Bullet(stats, screen, ship)
	bullets.add(new_bullet)

def create_enemy(stats, screen, enemies):
	enemy = Enemy(stats, screen)
	enemies.add(enemy)

def check_enemy_edges(enemies):
	for enemy in enemies.sprites():
		if enemy.check_edges():
			change_enemy_direction(enemies)
			break

def change_enemy_direction(enemies):
	for enemy in enemies:
		enemy.fleet_direction *= -1
	
def run_game():
	
	pygame.init()
	screen = pygame.display.set_mode((1000, 500))
	pygame.display.set_caption("LEFT SHOT")
	play_button = Button(screen, "Play")
	bg_color = (230, 100, 235)
	stats = GameStats()
	ship = Ship(stats, screen)
	enemies = Group()
	bullets = Group()
	
	while True:
		check_events(screen, ship, stats, play_button, bullets, enemies)
		if stats.game_active :
			ship.update()
			bullets.update()
			for bullet in bullets.copy():
				if bullet.rect.left >= 1000:
					bullets.remove(bullet)
					stats.count += 1
					if stats.count == 3:
						stats.game_active = False
			collisions = pygame.sprite.groupcollide(bullets,enemies, True, True)
			if len(enemies) == 0:
				bullets.empty()
				stats.increase_speed()
				create_enemy(stats, screen, enemies)
				
			check_enemy_edges(enemies)
			enemies.update()
			
		screen.fill(bg_color)	
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		ship.blitme()
		for enemy in enemies.sprites():
			enemy.draw_enemy()
		
		if not stats.game_active:
			pygame.mouse.set_visible(True)
			play_button.draw_button()
		pygame.display.flip()
		
run_game()	
