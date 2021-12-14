from turtle import Screen, Turtle, color
import colorgram
import random
color_list=[]
my_turtle=Turtle()
my_turtle.pensize(4)

c=colorgram.extract('colors.jpg',8)
print(c)

# def move_forward():
#     my_turtle.dot(15)    
#     my_turtle.penup()
#     my_turtle.forward(30)
#     my_turtle.pendown()

# def turn_left():
#     my_turtle.penup()
#     my_turtle.left(90)
    

# def turn_right():
#     my_turtle.penup()
#     my_turtle.right(90)
    

# for _ in range(9):
#     move_forward()
#     turn_left()
#     move_forward()
#     turn_right()
    
    # for _ in range(9):
    #     my_turtle.color(random.choice(colors))
    #     my_turtle.dot(15)    
    #     my_turtle.penup()
    #     my_turtle.forward(30)
    #     my_turtle.pendown()


# Define pictures, lines, polygons using OpenGl in C #
screen=Screen()
screen.exitonclick()




