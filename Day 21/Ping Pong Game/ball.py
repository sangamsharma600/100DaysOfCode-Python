from turtle import Screen, Turtle

screen=Screen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move=10
        self.y_move=20
        self.ball_speed=0.1


    def bounce_y(self):
        self.y_move *= -1
        if self.ball_speed>0:
            self.ball_speed=self.ball_speed*0.97
    def bounce_x(self):
        self.x_move *= -1 
        if self.ball_speed>0:
            self.ball_speed=self.ball_speed*0.97

    def move_ball(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def reset_postion(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed=0.1