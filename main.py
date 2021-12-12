import pygame 
import sys 
def ball_animation():
    global ball_speed_x, ball_speed_y
    # moveing the ball 
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # limiting ball to go out of boundaries of screen 
    if ball.top <=0 or ball.bottom >=screen_height:
        ball_speed_y *= -1
    if ball.left<=0 or ball.right>=screen_width:
        ball_speed_x *= -1

    # collision detection 
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height
pygame.init()

clock = pygame.time.Clock()

screen_width = 1000
screen_height= 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong-game')
ball_speed_x = 5 
ball_speed_y = 5
player_speed =0
# Game Rectangle 
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30,30)
player = pygame.Rect(screen_width-20, screen_height/2-70, 10,140)
opponent = pygame.Rect(10, screen_height/2-70, 10, 140)
bg_color = pygame.Color('gray12')
light_gray = (200,200,200)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_DOWN:
                player_speed +=5
                print('keey down')
            if event.key ==pygame.K_UP:
                player_speed -=5
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_DOWN:
                player_speed -=5
            if event.key ==pygame.K_UP:
                player_speed +=5
                
    player_animation()
        
    ball_animation()
    # Draw Visuals 

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)
    pygame.draw.ellipse(screen, light_gray, ball)
    # drawing line 
    pygame.draw.aaline(screen,light_gray, (screen_width/2, 0), (screen_width/2, screen_height))

    pygame.display.flip()
    clock.tick(60)
