import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun): 
    #создание пули для пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = 34, 177, 77
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
            
    def bullet_go(self):
    #передвижение пули по y
        self.y -= self.speed
        self.rect.y = self.y
        
        
    def bullet_draw(self):
    #рисование пули 
        pygame.draw.rect(self.screen, self.color, self.rect)