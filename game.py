import pygame, sys

import myInputs, movement, settings

pygame.init()

size = width, height = 640, 640
speed = [settings.scalar_speed, 0]
black = 0, 0, 0
max_render_time = settings.max_render_time
images_folder = "./images/"

screen = pygame.display.set_mode(size)

head = pygame.image.load(images_folder + "right_head.png")
body = pygame.image.load(images_folder + "right_body.png")

headrect = head.get_rect()
bodyrect = body.get_rect()

bodyrect.centerx = headrect.centerx - 100
bodyrect.centery = headrect.centery


ghost = head.get_rect()
bodyGhost = body.get_rect()

lastDrawTime = 0
justJumped = 0
bodyJustJumped = 0
turningPoints = list()
oldspeed = list()
while True:
    newSpeed = myInputs.getDirection()
  

    if newSpeed:
        if newSpeed != speed:
        # print(newSpeed)
            #print("before ", turningPoints)
            turningPoints.append(headrect.center)
            #print("after",turningPoints)
            imagePrefix = movement.getFacing(newSpeed)
            head = pygame.image.load(images_folder + imagePrefix.lower() + "_head.png")
            oldspeed.append(speed)
            speed = newSpeed
        
    elapsed = pygame.time.get_ticks()-lastDrawTime
    if elapsed < max_render_time:
        pygame.time.wait(max_render_time-elapsed) 

    headrect = headrect.move(speed)
    try:
        if len(turningPoints) == 0:
            bodyrect = bodyrect.move(speed)
        else:
            bodyrect = bodyrect.move(oldspeed[0])
            #print("before tps : %s speeds : %s" % (turningPoints, oldspeed))
            turningPoints, oldspeed = movement.checkTurn(bodyrect.centerx,bodyrect.centery, turningPoints,oldspeed)
            #print("after tps : %s speeds : %s" % (turningPoints, oldspeed))
    except:
        bodyrect = bodyrect.move(speed)


    ghost,justJumped = movement.edges(width,height,headrect,ghost,justJumped)
    bodyGhost,bodyJustJumped = movement.edges(width,height,bodyrect,bodyGhost,bodyJustJumped)

    screen.fill(black)
    screen.blit(head, headrect)
    screen.blit(body, bodyrect)

    if justJumped > 0 :
         
         screen.blit(head,ghost)
         ghost = ghost.move(speed)

    if bodyJustJumped > 0 :         
         screen.blit(body,bodyGhost)
         bodyGhost = bodyGhost.move(speed)

    pygame.display.flip()
    
    lastDrawTime = pygame.time.get_ticks()

#player = pygame.Rect(10,10,10,10)
        
    