from turtle import *

turtle = Turtle()
turtle.color("red")
turtle.begin_fill()
turtle.left(120)
turtle.forward(100)
for I in range (0,110):
    turtle.forward(1)
    turtle.right(2)
turtle.left(180)
for I in range (0,110):
    turtle.forward(1)
    turtle.right(2)
turtle.forward(100)
turtle.end_fill()
input()