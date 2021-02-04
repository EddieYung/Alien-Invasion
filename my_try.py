import sys
import pygame
from shooter import Shooter

class ContraGame():
    """creating a class to model a game character"""
    
    def __init__(self):
        """Initialize the game properties"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_colour = (200, 175,220)
        
        pygame.display.set_caption('Contra')
        self.shooter = Shooter(self)
        
    def play_game(self):
        """Runs the game with its properties"""
        
        while True:
            self._check_status()
            self.shooter.update_shooter()
            self._update_visuals()
            
            
    def _check_status(self):
        #watch for keyboard and mouse responses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            #moves the character to right by setting a moving flag 
            # to true   
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.shooter.move_right = True
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.shooter.move_left = True
                        
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.shooter.jump = True
                        
            #stops the movement of the character by setting a moving
            #flag to false        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.shooter.move_right = False
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.shooter.move_left = False
                        
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            self.shooter.jump = False
                    
    def _update_visuals(self):        
        self.screen.fill(self.bg_colour)
        
        self.shooter.blitme()

        pygame.display.flip()
        
if __name__ == '__main__':      
    contra_1 = ContraGame()
    contra_1.play_game()