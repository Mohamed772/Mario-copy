import pygame
from math import pi
# pygame.display.set_caption("Nom de la fenetre")
# logo = pygame.image.load("logo.png").convert()
# pygame.display.set_icon(logo)

pygame.init()
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])

BLANC = (255, 255, 255)
BLEU_CIEL = (185, 240, 240)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    
    # Fond provisoire
    screen.fill(BLEU_CIEL)
    # sol
    pygame.draw.line(screen, ROUGE,(0, 380),(700, 380),10)
    # rectangle
    pygame.draw.rect(screen, VERT, pygame.Rect(200, 330, 50, 45))
    # arc de cerle pour compteur de vies
    for angle, color in zip((0, pi),(ROUGE, VERT)):
        pygame.draw.arc(screen, color, pygame.Rect(620, 10, 70,70), angle, angle + pi, 5)
    pygame.display.flip()
  
    
    


pygame.quit()