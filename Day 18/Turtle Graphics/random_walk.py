from turtle import Screen, Turtle
import random
colors=['red','green','blue','yellow','black','pink','orange','brown']
my_turtle=Turtle()
my_turtle.color('green')
my_turtle.pensize(5)

directions=[0,90,180,270]    


for _ in range(0,1000):
    my_turtle.color(random.choice(colors))
    my_turtle.forward(50)
    












screen=Screen()
screen.exitonclick()