import pygame
import sys
from math import pi
from perso import *
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode(700,400)

menu = True
jeu = False

while menu:
    clock.tick(30)
    for event in pygame.event.get(): 
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            menu = False
    pygame.draw.rect(screen, (250,250,0),(250,250,50,50)
    pygame.display.update()
    
pygame.quit()
