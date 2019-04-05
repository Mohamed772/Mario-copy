import pygame, sys
from pygame.locals import*
 
clock = pygame.time.Clock()
pos = 0
 
fenetre = pygame.display.set_mode((500,500))
gif_ball = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png","12.png","13.png","14.png","15.png","16.png","17.png"]
 
while 1:
    for i in gif_ball:
        clock.tick(15)
        ball = pygame.image.load(i).convert_alpha()
        fenetre.blit(ball, [0,1])
        pygame.display.flip()
 
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                    pos = 1
                elif event.type == KEYUP and event.key == K_RIGHT:
                    pos = 0