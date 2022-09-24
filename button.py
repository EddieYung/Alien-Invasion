import pygame.font

class Button:
    """A class to create a button"""

    def __init__(self,ai_game, msg):
        """Initialize the button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #setting the dimensions and properties of the button
        self.width, self.height = 80, 35
        self.button_colour = (0, 100, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 25)

        #build the buttons rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center 

        # The button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center the text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_colour,
                self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Display the button on the screen"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)