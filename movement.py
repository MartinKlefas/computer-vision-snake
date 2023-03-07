import settings
import sys

scalar_speed = settings.scalar_speed
Directions = {"Left": [-1*scalar_speed,0], "Right": [scalar_speed,0], "Up":[0,-1*scalar_speed], "Down": [0,scalar_speed]}

def edges(width,height,headrect,ghost,justJumped):
    if headrect.left < 0 - justJumped:
        #ghost =  head.get_rect()
        ghost.top = headrect.top
        ghost.left = headrect.left

        headrect.left = width + headrect.left
        justJumped = headrect.width

    if headrect.right > width + justJumped:
       # ghost =  head.get_rect()
        ghost.top = headrect.top
        ghost.left = headrect.left

        headrect.right = headrect.right - width
        justJumped = headrect.width


    if headrect.top <0 - justJumped:
       # ghost =  head.get_rect()
        ghost.top = headrect.top
        ghost.left = headrect.left

        headrect.top = height +  headrect.top
        justJumped = headrect.height

    if headrect.bottom > height +justJumped:
      #  ghost =  head.get_rect()
        ghost.top = headrect.top
        ghost.left = headrect.left

        headrect.bottom = headrect.bottom - height
        justJumped = headrect.height

    if justJumped > 0 and headrect.left >= 0 and headrect.top >= 0 and headrect.right <= width and headrect.bottom <= height:
            justJumped = 0

    return ghost, justJumped

def getFacing(movementDirection):
     for thisDirection in Directions:
          if movementDirection == Directions[thisDirection]:
              return thisDirection
