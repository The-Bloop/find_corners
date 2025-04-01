import pygame
from pygame.locals import *
import numpy as np
from Cube import Cube

if __name__ == "__main__":
    cube1 = Cube()

    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    screen.fill((0,0,0))
    gameOn = True

    for line in cube1.lines:
        pygame.draw.line(screen, (255,255,255), (line.point1.x + 500, line.point1.y + 500), (line.point2.x + 500, line.point2.y + 500))

    while gameOn:
        for event in pygame.event.get():
        #event.type is to define the type of Key action. KEYDOWN means event is triggered if a key is pushed down.
        #event.key is the exact key that is being pressed. 
            if (event.type == KEYDOWN):
                screen.fill((0,0,0))
                if(event.key == K_BACKSPACE):
                    print("Sike")
                elif(event.key == K_x):
                    #print("Enter Angle for Rotation along X axis")
                    #angleX = int(input())
                    cube1.transform(45, "x")
                elif(event.key == K_y):
                    #print("Enter Angle for Rotation along Y axis")
                    #angleY = int(input())
                    cube1.transform(45, "y")
                elif(event.key == K_z):
                    #print("Enter Angle for Rotation along Z axis")
                    #angleZ = int(input())
                    cube1.transform(45, "z")
                elif(event.key == K_ESCAPE):
                    print('Bye Bye.')
                    gameOn = False

                for line in cube1.lines:
                    pygame.draw.line(screen, (255,255,255), (line.point1.x + 500, line.point1.y + 500), (line.point2.x + 500, line.point2.y + 500))
                points = cube1.findCornerPoints()
                for point in points:
                    pygame.draw.circle(screen,(255, 0, 0), (point.x + 500, point.y + 500), 2)

            elif (event.type == QUIT):
                print('Bye Bye.')
                gameOn = False
        pygame.display.flip()
