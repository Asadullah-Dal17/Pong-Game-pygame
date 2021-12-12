import pygame 
import sys 

pygame.init()

clock = pygame.time.Clock()

screen_width = 1000
screen_height= 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong-game')

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quite()
            sys.exit()
    pygame.display.flip()
    clock.tick(60)
