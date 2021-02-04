class Settings:
    """A class to store all the settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        
        #ship settings
        self.ship_speed = 1.5
        
        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_height = 10
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)