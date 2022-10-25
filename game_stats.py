class GameStats:
    """Track game Statistics"""
    
    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in a non active state.
        #this means something will have to be done to activate the game
        self.game_active = False
        
        # High score should never be reset
        self.high_score = 0


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0 
        self.level = 1
        # self.highscore = 