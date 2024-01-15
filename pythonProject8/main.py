import turtle

turtle.bgcolor('black')
turtle.speed(60)
turtle.pensize()
colors = ('magenta', 'yellow', 'dark green', 'red', 'orange',)

for i in range(1):
    turtle.forward(i * 2)
    turtle.right(91)
    turtle.color(colors[i % 5])

    for x in range(1):
        turtle.forward(x * 2)
        turtle.right(91)

        for a in range(1):
            turtle.forward(a * 2)
            turtle.right(91)

            for m in range(239):
                turtle.forward(m * 2)
                turtle.right(891)