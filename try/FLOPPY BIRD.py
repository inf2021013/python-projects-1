from turtle import *
import turtle

speed(0)

#BACKGROUND
wn = turtle.Screen()
wn.bgcolor("Turquoise")
wn.tracer(0)
wn.title("new game")
wn.setup(width=800,height=500)
#Grass
pendown()
color("Green")
shape("square")
penup()
goto(-400,-100)
pendown()
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(30)
    right(90)
end_fill()
#GROUND
pendown()
color("Brown")
shape("square")
penup()
goto(-400,-130)
pendown()
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(370)
    right(90)
end_fill()
# Sun
sun = turtle.Turtle()
sun.color("Yellow")
sun.shape("circle")
sun.penup()
sun.goto(330, 180)
sun.pendown()
sun.shapesize(outline=80)
#right(90)
#forward(800)
#right(90)
#forward(10)
while True:
    wn.update()