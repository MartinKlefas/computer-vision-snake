import pygame, sys

import myInputs, movement

pygame.init()

size = width, height = 640, 640
speed = [2, 0]
black = 0, 0, 0
max_render_time = 10 # makes sure we don't update more than once ever 5ms - seems to be about a decent moving speed.

screen = pygame.display.set_mode(size)

ball = pygame.image.load("head.gif")
ballrect = ball.get_rect()
ghost = ball.get_rect()
lastDrawTime = 0
justJumped = 0

while True:
    newSpeed = myInputs.getDirection()
    if newSpeed:
       # print(newSpeed)
        speed = newSpeed
        
    elapsed = pygame.time.get_ticks()-lastDrawTime
    if elapsed < max_render_time:
        pygame.time.wait(max_render_time-elapsed) 

    ballrect = ballrect.move(speed)
    
    ghost,justJumped = movement.edges(width,height,ballrect,ghost,justJumped)

    screen.fill(black)
    screen.blit(ball, ballrect)
   

    if justJumped > 0 :
         
         screen.blit(ball,ghost)
         ghost = ghost.move(speed)

    pygame.display.flip()
    
    lastDrawTime = pygame.time.get_ticks()

#player = pygame.Rect(10,10,10,10)
        
    