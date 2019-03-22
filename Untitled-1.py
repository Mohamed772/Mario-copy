import sys 
import pygame 


class Player(pygame.sprite.Sprite): 

    def __init__(self, x, y): 
     super(Player, self).__init__() 
     self.image = pygame.image.load("redball.png").convert_alpha()
     self.rect = self.image.get_rect(center=(x, y)) 
     self.y_change = 0 


pygame.init() 
GRAVITY = .9 
window_height = 600 
screen = pygame.display.set_mode((800, window_height)) 
player = Player(200, 100) 
all_sprites_list = pygame.sprite.Group(player) 
clock = pygame.time.Clock() 
move = False 
running = True 

while running: 
    for event in pygame.event.get(): 
     if event.type == pygame.QUIT: 
      running = False 
     if event.type == pygame.KEYDOWN: 
      move = True 
     if event.type == pygame.KEYUP: 
      move = False 

    if move: # Fly upwards. 
     player.y_change = -9 
    else: # Add the gravity to the y-velocity. 
     player.y_change += GRAVITY 
    player.rect.move_ip(0, player.y_change) 
    # Clamp the rect.y value to the range 50 to 450-rect.h. 
    # You could also use rect.clamp_ip((0, 50, 800, 450)). 
    if player.rect.y < 50: 
     player.rect.y = 50 
     player.y_change = 0 
    elif player.rect.bottom >= window_height-150: 
     player.rect.bottom = window_height-150 
     player.y_change = 0 

    screen.fill((30, 100, 140)) 
    all_sprites_list.draw(screen) 
    pygame.display.flip() 
    pygame.display.update() 
    clock.tick(30) 

pygame.quit() 
sys.exit() 