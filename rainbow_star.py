import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
for i in range(200):
    t.pencolor(colors[i % 7])
    t.pensize(7)
    t.forward(i*1.5)
    t.left(120)
    t.forward(i*2)
    t.right(60)
turtle.done
