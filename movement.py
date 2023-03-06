import settings
import sys

scalar_speed = settings.scalar_speed
Directions = {"Left": [-1*scalar_speed,0], "Right": [scalar_speed,0], "Up":[0,-1*scalar_speed], "Down": [0,scalar_speed]}

def edges(width,height,ballrect,ghost,justJumped):
    if ballrect.left < 0 - justJumped:
        #ghost =  ball.get_rect()
        ghost.top = ballrect.top
        ghost.left = ballrect.left

        ballrect.left = width + ballrect.left
        justJumped = ballrect.width

    if ballrect.right > width + justJumped:
       # ghost =  ball.get_rect()
        ghost.top = ballrect.top
        ghost.left = ballrect.left

        ballrect.right = ballrect.right - width
        justJumped = ballrect.width


    if ballrect.top <0 - justJumped:
       # ghost =  ball.get_rect()
        ghost.top = ballrect.top
        ghost.left = ballrect.left

        ballrect.top = height +  ballrect.top
        justJumped = ballrect.height

    if ballrect.bottom > height +justJumped:
      #  ghost =  ball.get_rect()
        ghost.top = ballrect.top
        ghost.left = ballrect.left

        ballrect.bottom = ballrect.bottom - height
        justJumped = ballrect.height

    if justJumped > 0 and ballrect.left >= 0 and ballrect.top >= 0 and ballrect.right <= width and ballrect.bottom <= height:
            justJumped = 0

    return ghost, justJumped

def getFacing(movementDirection):
     for thisDirection in Directions:
          if movementDirection == Directions[thisDirection]:
              return thisDirection
