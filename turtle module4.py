# set up our graphical canvas
# width = 500, height = 500
import turtle
turtle.setup(500, 500)

# move to the top left side of the screen
turtle.penup()
turtle.goto(-50, 90)
turtle.pendown()

# draw a very thin line
turtle.pensize(0.1)
turtle.forward(100)

# move back to the left side of the screen
# and a little further down
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()

# set the pen color to RED using RGB color values
turtle.pencolor(1.0, 0, 0)

# thicker line
turtle.pensize(2)
turtle.forward(100)

# move back to the left side of the screen
# and a little further down
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()

# set the pen color to BLUE using RGB color values
turtle.pencolor(0, 0, 1.0)

# thicker line
turtle.pensize(7)
turtle.forward(100)

# move back to the left side of the screen
# and a little further down
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

# set the pen color to a custom color using RGB color values
turtle.pencolor(0.7, 0.5, 0.2)

# thicker line
turtle.pensize(20)
turtle.forward(100)
