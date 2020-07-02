# Pong Classes
import pygame as pg
from csv import writer
from sklearn.neighbors import KNeighborsRegressor
import convert as Convert
import numpy as np

# Global Variables
WIDTH = 2600
HEIGHT = 1200
BORDER = 20
VELOCITY = 10
FRAMERATE = 120
fgColor = pg.Color("white")
bgColor = pg.Color("black")
ballColor = pg.Color(0, 255, 255)
paddleColor = pg.Color(124,252,0)
screen = pg.display.set_mode((WIDTH, HEIGHT))

class Ball: 

    RADIUS = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, color):
        global screen
        pg.draw.circle(screen, color,(self.x, self.y), self.RADIUS)

    def update(self, paddle):
        global bgColor, ballColor, BORDER
        
        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER + self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS:
            self.vy = -self.vy
        elif newx + self.RADIUS > WIDTH-Paddle.WIDTH and abs(newy-paddle.y) < Paddle.HEIGHT//2:
            self.vx = -self.vx
        else:
            self.show(bgColor)  #Remove previous location
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(ballColor)  #Create new location

class Paddle:
    
    HEIGHT = 100
    WIDTH = 30

    def __init__(self, location):
        self.y = location

    def show(self, color):
        global WIDTH
        pad = pg.Rect(float(WIDTH - self.WIDTH), float(self.y - self.HEIGHT//2), float(self.WIDTH), float(self.HEIGHT))
        pg.draw.rect(screen, color, pad)

    def update(self, prediction):       # Add parameter (, prediction) for ML
        #newY = pg.mouse.get_pos()[1]   # User Controlled
        newY = prediction               # ML Controlled
        if newY-self.HEIGHT//2 > BORDER and newY+self.HEIGHT//2 < HEIGHT - BORDER:
            self.show(bgColor)
            self.y = newY
            self.show(paddleColor)


