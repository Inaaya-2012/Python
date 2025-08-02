import turtle

win = turtle.Screen()
win.screensize(400,400)

win.bgcolor("purple")
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.color('lightpink')
n = 3
a = 360/n
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.left(a)

t.left(90)
t.penup()
t.forward(65)
t.pendown()
t.right(90)
for i in range(n):
    t.forward(100)
    t.right(a)
t.end_fill()    
turtle.done()