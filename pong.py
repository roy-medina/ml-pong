"""
Created: Tuesday June 30, 2020

Author: Roy Emmanuel Medina

Description: The game of pong that uses ML to allow the paddle to deflect the pong. 

Note: Influenced by www.youtube.com/computerphile
"""

from pong_classes import *
from ml_pong import *
from run_time import import_csv
from csv import writer
from time import sleep
import pygame as pg
import os
import random2 as rd
import pandas as pd
import numpy as np
import convert
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#Create Objects

ball = Ball(WIDTH-Ball.RADIUS-Paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)

right_paddle = Paddle(HEIGHT//2)

clock = pg.time.Clock()

#Start Gaming Module

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

# Create data collection file for ML/ Check if data collection file is present, creates one if isn't
if os.path.isfile("./pong_game.csv") == False:
    sample = open("pong_game.csv", "w")
    append_list_as_row("pong_game.csv", ['x','y','vx','vy','right_paddle.y'])

#   Use data to teach ML

pong = pd.read_csv("pong_game.csv")
pong = clean_dataset(pong, WIDTH-((right_paddle.WIDTH - 5)))
pong.to_csv("pong_game.csv", index = False)
X = pong.drop(columns = 'right_paddle.y')
y = pong['right_paddle.y']

#Run ML

from sklearn.neighbors import KNeighborsRegressor
if MANUAL_RUN == False:
    clf = KNeighborsRegressor(n_neighbors = 100)
    clf.fit(X,y)
    df = pd.DataFrame(columns = ['x', 'y', 'vx', 'vy'])

# Initialize start time for Generation Tracking
start_time = dt.datetime.now()
print("Start Time: " + str(start_time))

#Keeps the game running until quit
while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        # Run-time collection for generation
        end_time = dt.datetime.now()
        print("End Time: " + str(end_time))
        elapsed_time = (end_time - start_time).total_seconds()
        print("Elapsed Time: " + str(elapsed_time) + " seconds.")
        last_row = import_csv('run_time.csv')
        time_content = [int(last_row) + 1, elapsed_time, MANUAL_RUN, True]
        append_list_as_row('run_time.csv', time_content)
        break
    elif ball.x >= WIDTH-((right_paddle.WIDTH - 10)):
        if LIVES > 0:
            ball.show(bgColor)  #Remove previous location
            LIVES -= 1.0
            sleep(1)
            ball = Ball(WIDTH-Ball.RADIUS-Paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)
            ball.show(ballColor)
            end_time = dt.datetime.now()
            print("End Time: " + str(end_time))
            elapsed_time = (end_time - start_time).total_seconds()
            print("Elapsed Time: " + str(elapsed_time) + " seconds.")
            last_row = import_csv('run_time.csv')
            print("Observation: {}" .format(int(last_row)+1))
            time_content = [int(last_row) + 1, elapsed_time, MANUAL_RUN]
            append_list_as_row('run_time.csv', time_content)
            start_time = dt.datetime.now()
            print("\nStart Time: " + str(start_time))
        else:
            break

    clock.tick(FRAMERATE)
   
    pg.display.flip()

    if MANUAL_RUN == False:
        toPredict = df.append({'x' : ball.x, 'y' : ball.y, 'vx' : ball.vx, 'vy' : ball.vy}, ignore_index = True)
        MLposition = clf.predict(toPredict)

    if MANUAL_RUN == True:
        right_paddle.update() #User controlled
    else:
        right_paddle.updateML(MLposition) #ML controlled
    
    ball.update(right_paddle)

    #ML Data Collection
    row_contents = [float(ball.x), float(ball.y), float(ball.vx), float(ball.vy), float(right_paddle.y)]
    append_list_as_row('pong_game.csv', row_contents)
    

#Quits the Game
pg.quit()



