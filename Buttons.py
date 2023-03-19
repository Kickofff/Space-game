import pygame
import sys

class Button():
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        
        
    def draw(self, x, y, message, actione = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(dispaly, (23, 204, 58), 
                (x, y, self.width, self.height))

                if click[0] == 1:
                
                
        else:
            pygame.draw.rect(display, (13, 162, 58),
            (x, y, self.width, self.height))