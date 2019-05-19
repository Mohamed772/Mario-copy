import pygame
pygame.init()


#screen=pygame.display.set_mode(700,400)
#pygame.time.Clock()

player_left1 = pygame.transform.scale(pygame.image.load("left1.png"),(25,25))
player_left2 = pygame.transform.scale(pygame.image.load("left2.png"),(25,25))
player_right2= pygame.transform.scale(pygame.image.load("right2.png"),(25,25))
player_right1 = pygame.transform.scale(pygame.image.load("right1.png"),(25,25))
player_left = [player_left1,player_left2]
player_right = [player_right1,player_right2]

#music
pygame.mixer.music.load('game_music.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

