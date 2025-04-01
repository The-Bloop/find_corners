import pygame
from pygame.locals import *
import numpy as np

class Point:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.r = np.array([[1,0,0],[0,1,0],[0,0,1]])
    
    def transform(self, angle, axis):
        if(axis == "x"):
            self.rotateX(angle)
        elif(axis == "y"):
            self.rotateY(angle)
        elif(axis == "z"):
            self.rotateZ(angle)
        pointNew = np.dot(self.r, np.array([self.x,self.y,self.z]))
        self.x = round(pointNew[0],2)
        self.y = round(pointNew[1],2)
        self.z = round(pointNew[2],2)
        self.r = np.array([[1,0,0],[0,1,0],[0,0,1]])
        return 0
    
    def rotateX(self, angle):
        theta = np.radians(angle)
        c = np.cos(theta)
        s = np.sin(theta)
        self.r = np.dot(self.r, np.array([[1,0,0], [0,c,-s], [0,s,c]]))

    def rotateY(self, angle):
        theta = np.radians(angle)
        c = np.cos(theta)
        s = np.sin(theta)
        self.r = np.dot(self.r, np.array([[c,0,s],[0,1,0],[-s,0,c]]))

    def rotateZ(self, angle):
        theta = np.radians(angle)
        c = np.cos(theta)
        s = np.sin(theta)
        self.r = np.dot(self.r, np.array([[c,-s,0],[s,c,0],[0,0,1]]))