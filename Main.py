import pygame
pygame.display.set_caption("Nom de la fenetre")
#logo = pygame.image.load("logo.png").convert()
#pygame.display.set_icon(logo)

pygame.init()
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
pygame.quit()