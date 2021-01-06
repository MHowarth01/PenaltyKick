# ------------------------------------------------------------------------------
# Melanie Howarth
# 3/21/2018
# penaltyKick_Howarth.py
# ------------------------------------------------------------------------------
from turtle import *
import time
import random

setup(1010, 700)
bgcolor("forestgreen")


#field lines
#goal
draw=Pen()
draw.color("white")
draw.up()
draw.speed(0)
draw.goto(-255,340)
draw.down()
draw.setheading(270)
draw.width(3)
draw.forward(75)
draw.left(90)
draw.forward(500)
draw.left(90)
draw.forward(75)
draw.ht()

#marker lines
draw.up()
draw.goto(-400,340)
draw.down()
draw.setheading(270)
draw.forward(330)
draw.left(90)
draw.forward(800)
draw.left(90)
draw.forward(330)

#circles
##draw.speed(0)
##draw.up()
##draw.goto(-185,10)
##draw.down()
##draw.setheading(270)
##for i in range (180):
##    draw.forward(3)
##    draw.left(1)

draw.up()
draw.goto(0,115)
draw.down()
draw.begin_fill()
draw.circle(5)
draw.end_fill()

                  

# ******************************************************************************
# shootBall
# ******************************************************************************

def shootBall():
    ball.up()
    ang = ball.towards(ballX, ballY)
    ball.setheading(ang)

    goalie.up()
    draw1.clear()
    
    while ball.ycor() < 310:
        global randX
        randX = random.randint(-250, 250)
        goalie.up()
        goalie.goto(randX, 300)
        goalie.down()
        ball.fd(40)

    goalOrBlocked()
    

# ******************************************************************************
# goalOrBlocked
# ******************************************************************************

def goalOrBlocked():
    global randX
    draw.up()
    draw.goto(0,-285)
    draw.down()
    saves=0
    goals=0

    if ball.ycor() >= 310:
        if ball.xcor()<-255 or ball.xcor()>245:
            draw.color("red")
            draw.write("Missed!", align="center",font=("georgia",85,"bold"))
            
        elif ball.xcor()== randX:
            draw.color("yellow")
            draw.write("Saved!", align="center",font=("georgia",85,"bold"))
            saves=saves+1
            
        elif ball.xcor()<= randX+75 and ball.xcor()>= randX-75 :
            draw.color("yellow")
            draw.write("Saved!", align="center",font=("georgia",85,"bold"))
            saves=saves+1
            
        else:
            draw.color("blue")
            draw.write("Goal!", align="center",font=("georgia",85,"bold"))
            goals=goals+1
            
            
         
    
# ******************************************************************************
# placeBall
# ******************************************************************************

def placeBall(x,y):
    
    global ballX
    global ballY
    ballX = x
    ballY = y
    shootBall()

# ******************************************************************************
# main
# ******************************************************************************


register_shape("ball.gif")

ball = Pen()
ball.shape("ball.gif")
ball.speed(0)
ball.up()
ball.left(90)
ball.goto(0,-300)

global ballX 
global ballY 
ballX = 0
ballY = 0

register_shape("goalie1.gif")


goalie = Pen()
goalie.shape("goalie1.gif")
goalie.up()
goalie.goto(0,310)
goalie.down()
goalie.shapesize(1,5)

#message
draw1=Pen()
draw1.up()
draw1.ht()
draw1.goto(0,25)
draw1.down()
draw1.color("blue")
draw1.write("Click and drag on the ball to determine angle of shot, release click to shoot.",align="center", font=("georgia",15,"bold"))

ball.onrelease(placeBall)
done()
