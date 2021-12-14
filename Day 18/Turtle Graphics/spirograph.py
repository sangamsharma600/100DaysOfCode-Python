from turtle import Screen, Turtle, tiltangle
import random
import turtle

my_turtle=Turtle()
my_turtle.speed('fastest')
turtle.colormode(255)
def random_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors

for _ in range (int(360/10)):
    my_turtle.color(random_colors())
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading()+10)



screen=Screen()
screen.exitonclick()