import random
import turtle
from turtle import Turtle, Screen

# import colorgram
# c = colorgram.extract('colors.jpg', 30)
# for i in range(len(c)):
#     color_tuple = (c[i].rgb[0], c[i].rgb[1], c[i].rgb[2])
#     color_list.append(color_tuple)
# print(color_list)

turtle.colormode(255)
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56)]

my_turtle = Turtle()
my_turtle.speed('fastest')
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

for _ in range(10):

    for _ in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.setheading(0)




screen = Screen()
screen.exitonclick()
