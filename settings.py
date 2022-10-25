class Settings:
    """A class to store all the settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_colour = (230, 230, 230)
        
        #Ship settings
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_height = 10
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        
        #Alien Settings
        self.fleet_drop_speed = 5
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        self.ship_speed = 1.5

        # How quickly the game speeds up
        self.speedup_scale = 1.5

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        # self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.2  

        # Scoring
        self.alien_points = 50

        
    def increase_speed(self):
        """Increase apeed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
