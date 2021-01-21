import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #Moves the ship to the right by setting the moving_right attribute
            #to true, to enable continous smoth movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                    
            #sets the moving_right flag attribute of ship to false when the
            #key is released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                                         
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()
            
if __name__ == '__main__':
    # make a game instace, and run the game.
    ai = AlienInvasion()
    ai.run_game()
        
    
