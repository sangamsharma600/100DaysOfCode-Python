import random
from turtle import Screen, Turtle
my_turtle=Turtle()
my_turtle.color('green')


colors=['red','green','blue','yellow','black','pink','orange','brown']

for i in range(3,11):
    turning_degree=360/i
    my_turtle.pencolor(colors[random.randint(0,len(colors))])
    for _ in range(i):
        my_turtle.forward(100)
        my_turtle.right(turning_degree)
    






screen=Screen()
screen.exitonclick()