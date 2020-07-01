# Pong Classes
import pygame as pg

WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 2
FRAMERATE = 120
fgColor = pg.Color("white")
bgColor = pg.Color("black")
ballColor = pg.Color("blue")
paddleColor = pg.Color("orange")
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
    WIDTH = 20

    def __init__(self, location):
        self.y = location

    def show(self, color):
        pg.draw.rect(screen, color, pg.Rect(WIDTH-self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))

    def update(self):       # Add parameter (prediction) for ML
        newY = pg.mouse.get_pos()[1]   # User Controlled
        # newY = prediction               # ML Controlled
        if newY-self.HEIGHT//2 > BORDER and newY+self.HEIGHT//2 < HEIGHT - BORDER:
            self.show(bgColor)
            self.y = newY
            self.show(paddleColor)


