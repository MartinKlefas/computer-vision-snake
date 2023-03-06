import pygame, sys

import myInputs, movement, settings

pygame.init()

size = width, height = 640, 640
speed = [2, 0]
black = 0, 0, 0
max_render_time = settings.max_render_time
images_folder = "./images/"

screen = pygame.display.set_mode(size)

ball = pygame.image.load(images_folder + "right_head.png")
ballrect = ball.get_rect()
ghost = ball.get_rect()
lastDrawTime = 0
justJumped = 0

while True:
    newSpeed = myInputs.getDirection()
    if newSpeed:
       # print(newSpeed)
        imagePrefix = movement.getFacing(newSpeed)
        ball = pygame.image.load(images_folder + imagePrefix.lower() + "_head.png")
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
        
    