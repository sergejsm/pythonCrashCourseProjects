import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""
	def __init__(self, ai_settings, screen, ship):

		super(Bullet, self).__init__()
		self.screen = screen

		self.image = pygame.image.load('images/bullet.png')
		self.rect = self.image.get_rect()


		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store a decimal value for the bullet's position.
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.y -= self.speed_factor
		# Update the rect position.
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		self.screen.blit(self.image, self.rect)
