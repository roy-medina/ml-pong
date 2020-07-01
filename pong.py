"""
Created: Tuesday June 30, 2020

Author: Roy Emmanuel Medina

Description: The game of pong that uses ML to allow the paddle to deflect the pong. 

Note: Influenced by youtube.com/computerphile
"""

from pong_classes import *
import pygame as pg
import random2 as rd

#Global Variables

WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 2
FRAMERATE = 120
fgColor = pg.Color("white")
bgColor = pg.Color("black")
ballColor = pg.Color("blue")
paddleColor = pg.Color("orange")


#Create Objects

ball = Ball(WIDTH-Ball.RADIUS-Paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)

right_paddle = Paddle(HEIGHT//2)

#Gaming Module

pg.init()

#Create border/window for game
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.draw.rect(screen, fgColor, pg.Rect((0,0), (WIDTH, BORDER)))
pg.draw.rect(screen, fgColor, pg.Rect(0,0,BORDER, HEIGHT))
pg.draw.rect(screen, fgColor, pg.Rect(0, HEIGHT-BORDER,WIDTH, BORDER))

#Display ball
ball.show(ballColor)
#Display paddle
right_paddle.show(paddleColor)

clock = pg.time.Clock()


#Keeps the game running until quit

while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break

    clock.tick(FRAMERATE)
   
    pg.display.flip()

    # toPredict = df.append({'x':ball.x, 'y':ball.y, 'vx':ball.vx, 'vy':ball.vy,}, ignore_index = True)
    # MLposition = clf.predict(toPredict)

    right_paddle.update() #User controlled
    # paddle.update(MLposition) #ML controlled
    ball.update(right_paddle)

    # print("{}, {}, {}, {}, {}" .format(ball.x, ball.y, ball.vx, ball.vy, paddle.y), file = sample)


pg.quit()



