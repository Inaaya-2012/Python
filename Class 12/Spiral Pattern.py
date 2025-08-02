import turtle

import turtle

win = turtle.Screen()
win.screensize(400,400)

win.bgcolor("darkgreen")
t = turtle.Turtle()
t.color('lightgreen')
a = 4
while True:
    t.forward(a)
    t.right(90)
    a+=5

turtle.done()    