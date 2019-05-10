import sys
from math import pi
from pygame.locals import *
from perso import *

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
#fonctions
def nofall(player_rect): # ne tombe pas
    player_rect.bottom = screen_height-20 
    player_y_change = 0

def colision(player_rect,objects): # fonction de colision
    for mur in objects:
        old_rect = player_rect_old
        if old_rect.right <= mur.left and player_rect.right > mur.left:
            player_rect.right = mur.left
        if old_rect.left >= mur.right and player_rect.left < mur.right:
            player_rect.left = mur.right
        if old_rect.bottom <= mur.top and player_rect.bottom > mur.top:
            player_rect.bottom = mur.top

# Personnages
player_surface = pygame.image.load("left1.png").convert_alpha()
player_rect = player_surface.get_rect(center=(100, 100))
player_y_change = 0 
player_face=0

# Fonts
comic_font = pygame.font.SysFont("Comi Sans MS", 32)
# Vie
vie = 4
vie_surface = comic_font.render("Vie: {}".format(vie), True, BLANC)

# murs
taille_mur = 50
mur_surf = pygame.Surface((taille_mur,taille_mur))
mur_surf.fill(BLANC)
mur0_rect = pygame.Rect(300, 330, taille_mur, taille_mur)
pygame.draw.rect(mur_surf, (255,255,255), mur0_rect)
mur1_rect = pygame.Rect(200, 330, taille_mur,taille_mur)
pygame.draw.rect(mur_surf,(255,255,255), mur1_rect)
mur2_rect = pygame.Rect(100, 330, taille_mur,taille_mur)
pygame.draw.rect(mur_surf,(255,255,255), mur2_rect)
objects = [mur0_rect, mur1_rect,mur2_rect]

jump_counter = True
jump = False
continuer = True
deplacement_left = False
deplacement_right = False

pygame.key.set_repeat(1,20)
while continuer:
    clock.tick(30)
    for event in pygame.event.get(): # regler le probleme de deplacement gauche droite
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            continuer = False
        if keys[pygame.K_RIGHT]:
            deplacement_right = True
        if keys[pygame.K_LEFT]:
            deplacement_left = True
        if keys[pygame.K_UP]:
            jump = True
    
    player_rect_old = player_rect.copy()

    if deplacement_left: # gauche
        player_rect.left -= 3
        player_face=(player_face+1)%2
        player_surface=player_left[0+player_face]
    deplacement_left = False
    if deplacement_right: # droite
        player_rect.left += 3
        player_face=(player_face+1)%2
        player_surface=player_right[0+player_face]
        deplacement_right = False
    if jump and jump_counter: # Sauter
        jump_counter = False
        player_y_change = -15
    player_y_change += GRAVITY
    player_rect.move_ip(0, player_y_change)
    jump = False
    
    if player_rect.bottom >= screen_height-20 and player_rect.left <= 400: #sur le sol
        nofall(player_rect)
        jump_counter = True
    if player_rect.bottom >= screen_height-20 and player_rect.right >= 450: #sur le sol
        nofall(player_rect)
        jump_counter = True
    if player_rect.top >= screen_height+20: #tombe
        player_rect= player_surface.get_rect(center=(100, 100))
        vie =- 1


    colision(player_rect,[mur for mur in objects if player_rect.colliderect(mur)])
        
    # Fond provisoire
    screen.fill(BLEU_CIEL)

    # sol
    pygame.draw.line(screen, ROUGE,(0, screen_height-20),(400, screen_height-20),5)
    pygame.draw.line(screen, ROUGE,(450, screen_height-20),(screen_width, screen_height-20),5)

    # arc de cerle pour compteur de vies
    for angle, color in zip((0, pi),(BLANC, VERT)):
        pygame.draw.arc(screen, color, pygame.Rect(600, 30, 80, 80), angle, angle + pi, 5)
    # Texte: VIE
    screen.blit(vie_surface,(610, 60))
   


    # affichage 
    pygame.display.flip()
    for mur in objects:
        screen.blit(mur_surf,mur)
    screen.blit(player_surface, player_rect)
    pygame.display.flip() 
    pygame.display.update() 

pygame.quit()