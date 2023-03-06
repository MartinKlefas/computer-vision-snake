import pygame, sys

import myInputs

pygame.init()

size = width, height = 640, 640
speed = [0, -2]
black = 0, 0, 0
max_render_time = 10 # makes sure we don't update more than once ever 5ms - seems to be about a decent moving speed.

screen = pygame.display.set_mode(size)

ball = pygame.image.load("head.gif")
ballrect = ball.get_rect()
lastDrawTime = 0
justJumped = 0

while True:
    
    elapsed = pygame.time.get_ticks()-lastDrawTime
    if elapsed < max_render_time:
        pygame.time.wait(max_render_time-elapsed) 

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 - justJumped:
        ghost =  ball.get_rect()
        ghost.left =ballrect.left
        ghost.top = ballrect.top

        ballrect.left = width + ballrect.left
        justJumped = ballrect.width

    if ballrect.right > width + justJumped:
        ghost =  ball.get_rect()
        ghost.left =ballrect.left
        ghost.top = ballrect.top

        ballrect.right = ballrect.right - width
        justJumped = ballrect.width


    if ballrect.top <0 - justJumped:
        ghost =  ball.get_rect()
        ghost.left =ballrect.left
        ghost.top = ballrect.top

        ballrect.top = height +  ballrect.top
        justJumped = ballrect.height

    if ballrect.bottom > height +justJumped:
        ghost =  ball.get_rect()
        ghost.left =ballrect.left
        ghost.top = ballrect.top

        ballrect.bottom = ballrect.bottom - height
        justJumped = ballrect.height

    if justJumped > 0 and ballrect.left >= 0 and ballrect.top >= 0 and ballrect.right <= width and ballrect.bottom <= height:
        
            print("reset jj")
            justJumped = 0

   # if ballrect.left < 0 or ballrect.right > width:
   #     speed[0] = -speed[0]
   # if ballrect.top < 0 or ballrect.bottom > height:
   #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
   

    if justJumped > 0 :
         screen.blit(ball,ghost)
         ghost = ghost.move(speed)

    pygame.display.flip()
    key = myInputs.getDirection()
    if key :
        print(key)
    lastDrawTime = pygame.time.get_ticks()

#player = pygame.Rect(10,10,10,10)
        
    