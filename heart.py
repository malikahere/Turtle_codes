import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("pink")

# Create a turtle named "heart"
heart = turtle.Turtle()
heart.pensize(6)
heart.speed(5)
boundary_color = "purple"
fill_color = "violet"

# Set the turtle color and fill color
heart.color(boundary_color, fill_color)

# Move the turtle to the starting point
heart.penup()
heart.goto(0, -200)
heart.pendown()

# Draw the heart shape
heart.begin_fill()
heart.left(140)
heart.forward(224)
heart.circle(-112, 200)
heart.left(120)
heart.circle(-112, 200)
heart.forward(224)
heart.end_fill()

# Hide the turtle and display the result
heart.hideturtle()
turtle.done()
