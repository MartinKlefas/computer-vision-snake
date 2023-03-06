import pygame
import sys
import settings

scalar_speed = settings.scalar_speed
Directions = {"Left": [-1*scalar_speed,0], "Right": [scalar_speed,0], "Up":[0,-1*scalar_speed], "Down": [0,scalar_speed]}

def getDirection():
    for event in pygame.event.get():
       
       if event.type == pygame.QUIT:
           #print("Called quit properly?")
           sys.exit()
       elif event.type == 32787:
           print("Alternate quit call")
           sys.exit
       
       
       elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return Directions["Left"]
            elif event.key == pygame.K_RIGHT:
                return Directions["Right"]
            elif event.key == pygame.K_UP:
                return Directions["Up"]
            elif event.key == pygame.K_DOWN:
                return Directions["Down"]
            elif event.key == pygame.K_a:
                return Directions["Left"]
            elif event.key == pygame.K_d:
                return Directions["Right"]
            elif event.key == pygame.K_w:
                return Directions["Up"]
            elif event.key == pygame.K_s:
                return Directions["Down"]
            elif event.key == pygame.K_q:
                sys.exit()
            else:
                return ""
       else:
           return ""

        
