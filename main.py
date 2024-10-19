import turtle
import random
from turtle_area import draw_fractal_circle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

colors = ["cyan", "yellow", "purple", "white"]

for i in range(4):
    angle = i * 90
    pen.setheading(angle)
    color = random.choice(colors)

    draw_fractal_circle(pen, 0, 0, 150, color)

pen.hideturtle()

screen.mainloop()
