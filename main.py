from turtle import Turtle, Screen
import random

timey_turtle = Turtle()
screen = Screen()

import colorgram
colors = colorgram.extract('image.png',10)
colors_list = []
for i in colors:
    colors_list.append(i.rgb)
    print(type(i.rgb))

print(colors_list)
timey_turtle.teleport(-225,-225)
screen.colormode(255)
timey_turtle.ht()
for x in range(10):
    for i in range(10):
        timey_turtle.dot(20, random.choice(colors_list))
        timey_turtle.penup()
        timey_turtle.forward(50)
    turtle_position = timey_turtle.pos()
    print(turtle_position)
    timey_turtle.teleport(turtle_position[0]-500,turtle_position[1]+50)

screen.exitonclick()