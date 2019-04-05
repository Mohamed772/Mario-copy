import sys
from math import pi
from pygame.locals import *
import pygame
#from perso import *

# pygame.display.set_caption("Nom de la fenetre")
# logo = pygame.image.load("logo.png").convert()
# pygame.display.set_icon(logo)



pygame.init()
GRAVITY = 0.9
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])
clock = pygame.time.Clock() 
player_vitesse = 0

BLANC = (255, 255, 255)
BLEU_CIEL = (185, 240, 240)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Personnages
player_surface = pygame.image.load("left1.png").convert_alpha()
player_rect = player_surface.get_rect(center=(200, 100)) 
player_y_change = 0 
player_left = [pygame.image.load("left1.png"),pygame.image.load("left2.png"),pygame.image.load("left3.png"),pygame.image.load("left4.png"),pygame.image.load("left5.png")]
# Fonts
comic_font = pygame.font.SysFont("Comi Sans MS", 32)
# Vie
Vie = 4
text_surface = comic_font.render("Vie: {}".format(Vie), True, BLANC)

move = False
continuer = True
deplacement_left = False
deplacement_right = False

pygame.key.set_repeat(1,20)
while continuer:
    clock.tick(20) 
    for event in pygame.event.get(): # regler le probleme de deplacement gauche droite
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            continuer = False
        if keys[pygame.K_RIGHT]:
            deplacement_right = True
        if keys[pygame.K_LEFT]:
            deplacement_left = True
        if keys[pygame.K_UP]:
            move = True

    if deplacement_left:
        player_rect.left -= 3
        for i in range(len(player_left)):
            player_surface = player_left[i]
            if i == len(player_left):
                i = 0
        deplacement_left = False
    if deplacement_right:
        player_rect.left += 3
        deplacement_right = False
    if move: # Sauter
     player_y_change = -9
    else:
     player_y_change += GRAVITY
    player_rect.move_ip(0, player_y_change)
    move = False
    if player_rect.y < 10: 
     player_rect.y = 10 
     player_y_change = 0 
    elif player_rect.bottom >= screen_height-20: 
     player_rect.bottom = screen_height-20 
     player_y_change = 0 

    # Fond provisoire
    screen.fill(BLEU_CIEL)

    # sol
    pygame.draw.line(screen, ROUGE,(0, screen_height-20),(screen_width, screen_height-20),5)

    # rectangle
    pygame.draw.rect(screen, ROUGE, pygame.Rect(200, 330, 50, 50))

    # arc de cerle pour compteur de vies
    for angle, color in zip((0, pi),(BLANC, VERT)):
        pygame.draw.arc(screen, color, pygame.Rect(600, 30, 80, 80), angle, angle + pi, 5)
    # Texte: VIE
    screen.blit(text_surface,(610, 60))
    
    # affichage 
    pygame.display.flip() 
    screen.blit(player_surface, player_rect)
    pygame.display.flip() 
    pygame.display.update() 

pygame.quit()