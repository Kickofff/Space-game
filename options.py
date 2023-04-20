import pygame
pygame.init()
import sys
import random
from bullet import Bullet
from allien import Allien
import time
#from Buttons import Button

pygame.mixer.music.load(r'images\background_sound.mp3')
pygame.mixer.music.set_volume(0.1)

die_gun_sound = pygame.mixer.Sound(r'images\Boom.mp3')
die_gun_sound.set_volume(0.2)


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
            #стрельба из пушки
                new_bullet =  Bullet(screen, gun)
                bullets.add(new_bullet)
            elif event.key == pygame.K_ESCAPE:
            #пауза
                pause(screen)
                
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
    pygame.mixer.Sound.play(die_gun_sound)
    stats.guns_left -= 1
    alliens.empty()
    bullets.empty()
    create_army(screen, alliens)
    gun.create_gun()
    game_over(screen)
    time.sleep(1)
    
def game_over(screen):
    #меню конца игры
    stopped = True
    
    pygame.mixer.music.pause()
    
    while stopped:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()

        print_text(screen, "Game over. Press enter to play game, esc to exit",
        70, 300)

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            pygame.mixer.music.unpause()
            return False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

        pygame.display.update() 
    
        

    
    
def pause(screen):
    #реализация паузы
    paused = True
    
    pygame.mixer.music.pause()
    
    while paused:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()

        print_text(screen, "Paused. Press enter to continue", 160, 300)

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            #пауза
            paused = False

        pygame.display.update() 
        
    pygame.mixer.music.unpause()

    
def print_text(screen, message, x, y, font_color=(252, 252, 252),
               font_type=r'images\beer-money12.ttf', font_size=30):
    # Написание текста для пользователя
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
    
            
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
    allien = Allien(screen)
    allien_width = allien.rect.width
    allien_height = allien.rect.height
    number_allien_x = int((700 - 2 * allien_width) / allien_width)
    number_allien_y = 5
    allien_spacing = 0
    
    # создаем список всех возможных позиций пришельцев на экране
    positions = []
    for row_number in range(number_allien_y):
        for allien_number in range(number_allien_x):
            x = allien_width + allien_width * allien_number
            y = allien_height + allien_height * row_number
            positions.append((x, y))
    
    # перемешиваем список позиций, чтобы выбирать случайную позицию из разных мест на экране
    random.shuffle(positions)
    
    # добавляем пришельцев на экран, по одному из каждой доступной позиции
    for position in positions:
        allien = Allien(screen)
        allien.rect.x = position[0] 
        allien.rect.y = position[1]
        allien.x = float(allien.rect.x)
        allien.y = float(allien.rect.y)
        
        
        # проверяем, не пересекается ли текущий пришелец с уже созданными пришельцами
        collision_rect = pygame.Rect(allien.rect.x - allien_spacing, allien.rect.y - allien_spacing, allien_width + 2 * allien_spacing, allien_height + 2 * allien_spacing)
        if not any(allien.rect.colliderect(a.rect) for a in alliens) and collision_rect.collidelist([a.rect for a in alliens]) == -1:
            alliens.add(allien)
            print(position)
            # задержка перед созданием следующего пришельца, чтобы они появлялись постепенно сверху экрана
