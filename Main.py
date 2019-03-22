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

# Personnage
personnage = pygame.image.load("redball.png").convert_alpha()

# Fonts
comic_font = pygame.font.SysFont("Comi Sans MS", 32)
# Vie
Vie = 4
text_surface = comic_font.render("Vie: {}".format(Vie), True, BLANC)


continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    
    # Fond provisoire
    screen.fill(BLEU_CIEL)

    # sol
    pygame.draw.line(screen, ROUGE,(0, screen_height-20),(screen_width, screen_height-20),10)

    # rectangle
    pygame.draw.rect(screen, VERT, pygame.Rect(200, 330, 50, 45))

    # arc de cerle pour compteur de vies
    for angle, color in zip((0, pi),(BLANC, VERT)):
        pygame.draw.arc(screen, color, pygame.Rect(600, 30, 80, 80), angle, angle + pi, 5)
    # Texte: VIE
    screen.blit(text_surface,(610, 60))
    
    # affichage personnage
    screen.blit(personnage, (20, 242))
    pygame.display.flip()
  
    
    


pygame.quit()