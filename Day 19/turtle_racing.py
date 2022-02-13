from turtle import Turtle,Screen
import random
colors=['red','green','blue','yellow','orange','purple']
turtle_position=[-80,-50,-20,20,50,80]
turtle_list=[]
is_game_over=False
screen=Screen()
screen.setup(width=500,height=400)


user_bet=screen.textinput(title='Make your bet ',prompt='Which one will win the race? Enter a color: ')

for i in range(6):
    my_turtle=Turtle(shape='turtle')
    my_turtle.color(colors[i])
    my_turtle.penup()
    my_turtle.goto(x=-230,y=turtle_position[i])
    turtle_list.append(my_turtle)

if user_bet:
    is_game_over=False

while not is_game_over:

    for i in turtle_list:
        random_distance=random.randint(0,10)
        i.forward(random_distance)

        if i.xcor()>230:
            winning_turtle=i.pencolor()
            if(user_bet==winning_turtle):
                print(f"Yayyyyy, you win. {winning_turtle} turtle is the winner")
            else:
                print(f"Oops, you lose. {winning_turtle} turtle is the winner")
            is_game_over=True

screen.exitonclick()