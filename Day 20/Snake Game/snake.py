from turtle import Turtle,Screen
import time

STARGING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

screen=Screen()
class Snake:
    def __init__(self):
       self.my_turtles=[]
       self.create_snake()
       self.head=self.my_turtles[0]

    def create_snake(self):
        for i in STARGING_POSITIONS:
           self.add_length(i)

    def add_length(self,i):
         my_turtle=Turtle('square')
         my_turtle.color('white')
         my_turtle.penup()
         my_turtle.goto(i)
         self.my_turtles.append(my_turtle)
    
    def extend_snake(self):
        self.add_length(self.my_turtles[-1].position())

    def move(self):
        for my_turtle_num in range(len(self.my_turtles)-1,0,-1):
            new_x=self.my_turtles[my_turtle_num-1].xcor()
            new_y=self.my_turtles[my_turtle_num-1].ycor()
            self.my_turtles[my_turtle_num].goto(new_x,new_y)
        self.my_turtles[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

    
    
    