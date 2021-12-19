import time
from turtle import Screen
from snake import Snake

screen=Screen()
snake=Snake()
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

screen.update()







 

























screen.exitonclick()