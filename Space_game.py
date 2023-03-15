import pygame
from gun_work import Gun
import options
from pygame.sprite import Group
from statistics import Stats


def start():
    
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Defenders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group() 
    alliens = Group()
    options.create_army(screen, alliens)
    stats = Stats() 
    
    while True:
        options.events(screen, gun, bullets)  
        gun.update_gun()
        options.update(bg_color, screen, gun, alliens, bullets)
        options.update_bullets(screen, alliens, bullets)
        options.update_alliens(stats, screen, gun, alliens, bullets)
start()