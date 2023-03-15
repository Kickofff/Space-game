import pygame
import sys
from bullet import Bullet
from allien import Allien
import time

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            # move right
            if event.key == pygame.K_d:
                gun.mright = True
            # move left
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet =  Bullet(screen, gun)
                bullets.add(new_bullet)
                
        elif event.type == pygame.KEYUP:
            # stop moving right
            if event.key == pygame.K_d:
                gun.mright = False
            # stop moving left
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, gun, alliens, bullets):
    #обновление экрана 
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.bullet_draw()
    gun.inference()
    alliens.draw(screen)
    pygame.display.flip()
    
def update_bullets(screen, alliens, bullets):
    #обновление(удаление) позиции пуль
    bullets.update()
    for bullet in bullets:
        bullet.bullet_go()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, alliens, True, True)
    if len(alliens) == 0:
        bullets.empty()
        create_army(screen, alliens)
    
    
def gun_die(stats, screen, gun, alliens, bullets):
    #столкновение пушки и короблей
    stats.guns_left -= 1
    alliens.empty()
    bullets.empty()
    create_army(screen, alliens)
    gun.create_gun()
    time.sleep(1)
    
            
def update_alliens(stats, screen, gun, alliens, bullets):
    #обновляет местоположение пришельцев
    alliens.update()
    if pygame.sprite.spritecollideany(gun, alliens):
        gun_die(stats, screen, gun, alliens, bullets)
    alliens_check(stats, screen, gun, alliens, bullets)
        
def alliens_check(stats, screen, gun, alliens, bullets):
    #проверка добрались ли корабли до края экрана 
    screen_rect = screen.get_rect()
    for allien in alliens.sprites():
        if allien.rect.bottom >= screen_rect.bottom:
            gun_die(stats, screen, gun, alliens, bullets)
            break


def create_army(screen, alliens):
    #копирование пришельцев 
    allien = Allien(screen)
    allien_width = allien.rect.width
    number_allien_x = int((700 - 2 * allien_width) / allien_width)
    allien_height = allien.rect.height
    number_allien_y = int((800 - 100 - 2 * allien_height) / allien_height)
    
    for row_number in range(number_allien_y - 1):
        for allien_number in range(number_allien_x):
            allien = Allien(screen)
            allien.x = allien_width + allien_width * allien_number
            allien.y = allien_height + allien_height * row_number
            allien.rect.x = allien.x
            allien.rect.y = allien.rect.height + allien.rect.height * row_number
            alliens.add(allien)