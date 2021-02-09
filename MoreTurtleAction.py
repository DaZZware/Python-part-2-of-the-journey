# more turtle action

from turtle import *

shape("turtle")
color("white")
speed(10)
pensize(6)

Screen().bgcolor("turquoise") # screen function of window

def vshape(): # Vshapre on the snowflake to call in  
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)
    
def snowflake():
    for x in range(0,6):
        snowflakeArm()
        right(60)
        
snowflake()

    