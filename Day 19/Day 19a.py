from turtle import Turtle, Screen

my_turtle=Turtle()
screen=Screen()



def move_forward():
    my_turtle.forward(15)
def move_backward():
    my_turtle.backward(15)
def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
def move_left():
    my_turtle.left(10)
def move_right():
    my_turtle.right(10)


screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='c',fun=clear_screen)
screen.onkey(key='a',fun=move_left)
screen.onkey(key='d',fun=move_right)




screen.exitonclick()