from turtle import Screen, Turtle

screen = Screen()

class Pong(Turtle):
    def __init__(self,pong_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(pong_position)

    
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)

