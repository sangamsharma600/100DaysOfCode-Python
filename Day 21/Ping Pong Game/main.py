from turtle import Screen
from pong import Pong
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
ball=Ball()
screen.tracer(0)
pong_a=[]
pong_b=[]
screen.setup(height=600,width=800)
screen.bgcolor('black')
screen.title("Ping Pong")

r_pong=Pong((350,0))
l_pong=Pong((-350,0))
scoreboard=Scoreboard()

is_game_on=True

screen.listen() 
screen.onkey(r_pong.go_up,"Up")
screen.onkey(r_pong.go_down,"Down")
screen.onkey(l_pong.go_up,"w")
screen.onkey(l_pong.go_down,"s")




     

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Detecting the Collission with Wall #
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y() # Bounce the ball

    # Detecting collission with Right Paddle #
    if ball.distance(r_pong)<50 and ball.xcor()>320 or ball.distance(l_pong)<50 and ball.xcor()<-320:
        ball.bounce_x()
    
    # Detect Left Paddle Miss #
    if ball.xcor()>360  :
        ball.reset_postion()         
        scoreboard.l_point()


    # Detect Left Paddle Miss
    if ball.xcor()<-360  :
        ball.reset_postion()
        scoreboard.r_point()       


     

screen.exitonclick()

