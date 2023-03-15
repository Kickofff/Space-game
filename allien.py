import pygame

class Allien(pygame.sprite.Sprite):
#класс для 1 корабля

    def __init__(self, screen):
    #настройка начальной позиции
        super(Allien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'images\allien_ship.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        
    def draw_allien(self):
    #вывод пришельца на экран 
        self.screen.blit(self.image, self.rect)
        
        
    def update(self):
    # обновление местоположения прешельцев 
        self.y += 0.1
        self.rect.y = self.y