class Settings():
	#A class to store all settings for Alien Invasion
	
	def __init__(self):
		
		"""Initialize the game's settings."""
		#Screen settings
		
		self.screen_width = 1300
		self.screen_height = 900
		self.bg_color = (250, 250, 250)
		
		#Ship Settings.
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		#Bullet settings.
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 0, 60 ,60
		self.bullets_allowed = 5
		
		#Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
