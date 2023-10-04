import turtle
import math

def drawCircle(turtle, center, radius):
    circumference = 2 * math.pi * radius
    distance = circumference / 120.0
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    turtle.setheading(0)
    for _ in range(120):
        turtle.forward(distance)
        turtle.left(3)

def main():
    turtle.setup(width=800, height=600)
    turtle.speed(0)
    turtle.hideturtle()
    x = 50
    y = 75
    radius = 100
    drawCircle(turtle, (x, y), radius)
    turtle.done()

if __name__ == "__main__":
    main()
