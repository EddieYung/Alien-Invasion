import pygame

class Shooter:
    """ A class to model a contra shooter"""
    
    def __init__(self, contra_shooter):
        """Initialize the attributes of shooter"""
        self.screen = contra_shooter.screen
        self.screen_rect = contra_shooter.screen.get_rect()
        
        #Load the image to the screen from it source
        self.image = pygame.image.load("/Users/edwardquarshie/Desktop/alien_invation/images/shooter.bmp")
        self.rect = self.image.get_rect()
        
        #start the shooter at the left bottom of every new game
        self.rect.left = self.screen_rect.left
        
        #Moving Right flag
        self.move_right = False
        self.move_left = False
        self.jump = False
        
    def update_shooter(self):
        if self.move_right:
            self.rect.x += 1
            
        if self.move_left:
            self.rect.x -= 1
        
        if self.jump:
            self.rect.y -= 10
        
         
    def blitme(self):
        """Draws the shooter onto the screen"""
        self.screen.blit(self.image, self.rect)