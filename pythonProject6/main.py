#LIBRARIES:
import turtle
#functions:
def LEVEL1():
    #Screen
    wn = turtle.Screen()
    wn.title("new game")
    wn.bgcolor("Turquoise")
    wn.tracer(0)
    wn.setup(width=800,height=500)
    #Terrain
    terrain = turtle.Turtle()
    terrain.color("Brown")
    terrain.shape("square")
    terrain.penup()
    terrain.goto(0,-200)
    terrain.pendown()
    terrain.shapesize(stretch_wid=6,stretch_len=50)
    #Grass
    grass = turtle.Turtle()
    grass.color("Green")
    grass.shape("square")
    grass.penup()
    grass.goto(0,-140)
    grass.pendown()
    grass.shapesize(stretch_wid=1.5,stretch_len=50)
    #Sun
    sun = turtle.Turtle()
    sun.color("Yellow")
    sun.shape("circle")
    sun.penup()
    sun.goto(330,180)
    sun.pendown()
    sun.shapesize(outline=80)
    #CASTLE:

    #WALL1OUTLINE:
    Wall1outline = turtle.Turtle()
    Wall1outline.color("black")
    Wall1outline.penup()
    Wall1outline.goto(174,-20)
    Wall1outline.pendown()
    for i in range(2):
        Wall1outline.forward(54)
        Wall1outline.right(90)
        Wall1outline.forward(104)
        Wall1outline.right(90)
#    Wall1outline.penup()
    x = 174
    y = -20
    Wall1outline.penup()
    Wall1outline.goto(x,y)
    Wall1outline.pendown()
    Wall1outline.right(90)
    for i in range(6):
        x=x+9
        Wall1outline.penup()
        Wall1outline.goto(x,y)
        Wall1outline.pendown()
        Wall1outline.forward(104)
    Wall1outline.penup()
    Wall1outline.goto(174, -20)
    Wall1outline.pendown()
    Wall1outline.left(90)
    x=174
    y=-20
    for i in range(26):
        y=y-4
        Wall1outline.penup()
        Wall1outline.goto(x, y)
        Wall1outline.pendown()
        Wall1outline.forward(54)
    # WALL 2:
    Wall2 = turtle.Turtle()
    Wall2.color("Brown")
    Wall2.shape("square")
    Wall2.penup()
    Wall2.goto(320, -73)
    Wall2.pendown()
    Wall2.shapesize(stretch_wid=5, stretch_len=2.5)
    # WALL 1:
    Wall1 = turtle.Turtle()
    Wall1.color("Brown")
    Wall1.shape("square")
    Wall1.penup()
    Wall1.goto(178, -21.3)
    Wall1.pendown()
    Wall1.shapesize(stretch_wid=0.12, stretch_len=0.35)
    x=178
    y=-21.3
    for i range(26):
        y=y-


    while True:
        wn.update()



#MAIN PROGRAMM
LEVEL1()