import pygame, sys

pygame.init()

size = width, height = 640, 640
speed = [2, 2]
black = 0, 0, 0
max_render_time = 10 # makes sure we don't update more than once ever 5ms - seems to be about a decent moving speed.

screen = pygame.display.set_mode(size)

ball = pygame.image.load("head.gif")
ballrect = ball.get_rect()
lastDrawTime = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    elapsed = pygame.time.get_ticks()-lastDrawTime
    if elapsed < max_render_time:
        pygame.time.wait(max_render_time-elapsed) 

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    lastDrawTime = pygame.time.get_ticks()

#player = pygame.Rect(10,10,10,10)
        
    