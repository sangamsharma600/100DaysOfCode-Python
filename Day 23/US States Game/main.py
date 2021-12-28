import turtle
import pandas
states_data = pandas.read_csv('50_states.csv')
is_game_on = True
screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
screen.title("U.S States Naming Game")
turtle.shape(image)
while is_game_on:
    answer_state = screen.textinput(title="Guess the name", prompt="What's the next state? ").title()
    is_city = answer_state == states_data['state']
    if is_city:
        turtle.Turtle.goto(states_data[answer_state].x)
















screen.exitonclick()
