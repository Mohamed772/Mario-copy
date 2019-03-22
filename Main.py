import pygame
from math import pi
# pygame.display.set_caption("Nom de la fenetre")
# logo = pygame.image.load("logo.png").convert()
# pygame.display.set_icon(logo)

# Personnages
class Player(pygame.sprite.Sprite): 

    def __init__(self, x, y): 
     super(Player, self).__init__() 
     self.image = pygame.image.load("redball.png").convert_alpha()
     self.rect = self.image.get_rect(center=(x, y)) 
     self.y_change = 0 

pygame.init()
GRAVITY = 0.9
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])
player = Player(200, 100) 
all_sprites_list = pygame.sprite.Group(player) 
clock = pygame.time.Clock() 
player_vitesse = 0

BLANC = (255, 255, 255)
BLEU_CIEL = (185, 240, 240)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)


# Fonts
comic_font = pygame.font.SysFont("Comi Sans MS", 32)
# Vie
Vie = 4
text_surface = comic_font.render("Vie: {}".format(Vie), True, BLANC)

move = False
continuer = True
deplacement_left = False
deplacement_right = False

while continuer:
    for event in pygame.event.get(): # regler le probleme de deplacement gauche droite
        if event.type == pygame.QUIT:
            continuer = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            move = True
        """if event.type == pygame.KEYDOWN: 
            if event.key == K_UP
                move = True 
            if event.key == K_RIGHT:
                deplacement_right = True
            if event.key == K_LEFT:
                deplacement_left = True
         if event.type == pygame.KEYUP: 
            if event.key == K_UP
                move = False
            if event.key == K_RIGHT:
                deplacement_right = False
            if event.key == K_LEFT:
                deplacement_left = False"""

    if deplacement_left:
        player.x_change -=1
        player.rect.move_ip(player.x_change, 0)
    if deplacement_right:
        player.x_change +=1
        player.rect.move_ip(player.x_change, 0)
    if move: # Fly upwards. 
     player.y_change = -9
    else:
     player.y_change += GRAVITY
    player.rect.move_ip(0, player.y_change)
    move = False
    if player.rect.y < 10: 
     player.rect.y = 10 
     player.y_change = 0 
    elif player.rect.bottom >= screen_height-20: 
     player.rect.bottom = screen_height-20 
     player.y_change = 0 

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
    all_sprites_list.draw(screen) 
    pygame.display.flip() 
    pygame.display.update() 
    clock.tick(30) 

pygame.quit()