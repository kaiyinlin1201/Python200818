import turtle
import time
a=turtle.Turtle()
b=turtle.Turtle()
a.color('cyan')
a.pensize(5)
b.color('green')
b.pensize(5)
for i in range (360):
    a.forward(1)
    a.left(1)
    b.forward(1)
    b.right(1)