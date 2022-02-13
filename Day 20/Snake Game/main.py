import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
my_turtles=[]


is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collision with Food # 
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    # Detect Collision with Wall #
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_on=False
        score.game_over()

    # Detect Collision with Tail #
    for segment in snake.my_turtles[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            score.game_over()
screen.update()







 

























screen.exitonclick()