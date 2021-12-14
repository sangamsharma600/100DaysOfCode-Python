from turtle import Screen, Turtle
import random
import turtle

turtle.colormode(255)
def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)

    return random_color
# colors=['red','green','blue','yellow','black','pink','orange','brown','cyan']


my_turtle=Turtle()
my_turtle.pensize(4)

directions=[0,90,180,270]    


for _ in range(0,50):
    my_turtle.color(colors())
    my_turtle.shape('turtle')
    my_turtle.speed(3)
    my_turtle.forward(40)

    my_turtle.setheading(random.choice(directions))







screen=Screen()
screen.exitonclick()