import sys
from time import sleep 
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        
        #Create an instance to store game statistics.
        # And create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

        # Make the button a play button 
        self.play_button = Button(self, "Play")
        self.level_one = Button(self, "Level One")
        self.level_two = Button(self,"Level Two")
        self.level_three = Button(self, "Level Three")

        
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
        
            
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            
            #Moves the ship to the right or left setting the moving flags
            #to true, to enable continous smoth movement
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when a player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reset the game to settings 
            self.settings.initialize_dynamic_settings()

            #reset the game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            #get rid of any remaining alien and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the cursor when play begins
            pygame.mouse.set_visible(False)

    
    def _start_game(self):
        """start the game the 'P' is pressed"""
        self.stats.game_active = True

          
                
    def _check_keydown_events(self, event):
            """respond to keypresses"""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True 
                         
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
                                
            elif event.key == pygame.K_UP:
                self.ship.moving_up = True
                    
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = True
                
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

            elif event.key == pygame.K_p:
                self._start_game()
                
            elif event.key == pygame.K_q:
                sys.exit()
          
                        
    def _check_keyup_events(self, event):
        """responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False   
            
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False   
            
    
    def _fire_bullet(self):
        """create a new bullet and add it to the bullet sprite group"""  
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)   
        
        
    def _update_bullets(self):
        """updates position of bullets and get rid old bullets."""
        #Update bullet positions
        self.bullets.update()
        
        #Get rid of bullets that have disappeared 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
                
        self._check_bullet_allien_collisions()
        
    def _check_bullet_allien_collisions(self):
        """Respond to bullet-alien collisions."""
        #Get rid of bullet and the alien that have collided
        collisions = pygame.sprite.groupcollide(
                     self.bullets,self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score
        
        
        if not self.aliens:
            #Destroy existing bullets and create ne fleet
            self.bullets.empty()
            self._create_fleet()
                
    def _update_aliens(self):
        """Update the positions of all aliens if it hits an edge"""
        self._check_fleet_edges()
        self.aliens.update()
        
        #Check for Alien and ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
            #Look for alens hitting the bottom of the screen.
            self._check_aliens_bottom()

            
    def _ship_hit(self):
        """Respond to ship and alien collision"""
        if self.stats.ships_left > 0:
            # Derement ships left
            self.stats.ships_left -= 1
            
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            # create new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
        
            #Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            
            
    def _check_aliens_bottom(self):
        """Check if any alien has reached the bottom of the screen."""  
        screen_rect = self.screen.get_rect()        
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same way when a ship gets hit.
                self._ship_hit()
                break     
                
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien object and find the number of aliens in a row
        #NB: spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #calculation to determine how man aliens can fit the screen size.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * alien_height) - ship_height)
        
        number_rows = available_space_y // (2 * alien_height)
    
        #Create the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
            
    def _create_alien(self, alien_number, row_number):
        #Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        #add alien to the sprite group of aliens
        self.aliens.add(alien)
        
        
    def _check_fleet_edges(self):
        """Check if fleet has hit an edge, and change direction"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleets direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
                
               

                                         
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
        #draw an alien on the surface of the screen
        self.aliens.draw(self.screen)

        # Draw the scores on the screen
        self.sb.show_score()
            
        # Draw the play button if the game is active
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.level_one.draw_button()
            self.level_two.draw_button()
            self.level_three.draw_button()

        

            
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
            
if __name__ == '__main__':
    # make a game instace, and run the game.
    ai = AlienInvasion()
    ai.run_game()
        
    
