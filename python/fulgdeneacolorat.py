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
tim.speed(5)

def vshape():
    tim.right(25)
    tim.forward(50)
    tim.backward(50)
    tim.left(50)
    tim.forward(50)
    tim.backward(50)
    tim.right(25)

def snowflakeArm():
    for x in range(0,4):
        tim.pencolor(random.choice(colours))
        tim.forward(30)
        vshape()
    tim.backward(120)

def snowflake():
    for x in range(0,10):
        snowflakeArm()
        tim.right(36)

snowflake()

screen.mainloop()