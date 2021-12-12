import pygame 
import sys 

pygame.init()

clock = pygame.time.Clock()

screen_width = 1000
screen_height= 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong-game')

# Game Rectangle 
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30,30)
player = pygame.Rect(screen_width/-20, screen_height/2-70, 10,140)
opponent = pygame.Rect(10, screen_height/2-70, 10, 140)
bg_color = pygame.Color('gray12')
light_gray = (200,200,200)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quite()
            sys.exit()
    pygame.display.flip()
    clock.tick(60)
