import turtle

win = turtle.Screen()
win.screensize(400,400)

win.bgcolor("red")
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.color('yellow')
n = 4
a = 360/n
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.left(a)
t.end_fill()

turtle.done()
