from turtle import Screen
import turtle
import random

screen = Screen()
screen.bgcolor("turquoise")
colours = ["blue", "purple", "white", "yellow", "green", "orange"]
tim = turtle.Turtle()
tim.color("white")
tim.shape('turtle')
tim.pensize(6)
tim.speed(10)

def vshape(size):
    tim.right(25)
    tim.forward(size)
    tim.backward(size)
    tim.left(50)
    tim.forward(size)
    tim.backward(size)
    tim.right(25)

def snowflakeArm(size):
    for x in range(0,4):
        tim.forward(size)
        vshape(size)
    tim.backward(size*4)

def snowflake(size):
    tim.pencolor(random.choice(colours))
    for x in range(0,10):
        snowflakeArm(size)
        tim.right(36)

for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    tim.penup()
    tim.goto(x,y)
    tim.pendown()
    snowflake(size)

screen.mainloop()