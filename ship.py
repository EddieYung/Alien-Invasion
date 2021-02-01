import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load("/Users/edwardquarshie/Desktop/alien_invation/images/ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ships position based on the flag."""
        if self.moving_right:
            self.rect.x +=1
            
        if self.moving_left:
            self.rect.x -=1
            
        if self.moving_up:
            self.rect.y -=1
        
        if self.moving_down:
            self.rect.y +=1
            
    def blitme(self):
        """draw a ship at its current location"""
        self.screen.blit(self.image, self.rect)
        