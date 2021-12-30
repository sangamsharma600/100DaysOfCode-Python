import turtle
import pandas
states_data = pandas.read_csv('50_states.csv')
is_game_on = True
screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
screen.title("U.S States Naming Game")
turtle.shape(image)
states_list = states_data.state.to_list()
x_cor = states_data.x.to_list()
y_cor = states_data.y.to_list()
correct_guesses = []
score_count = 0

while is_game_on and score_count != 50:
    answer_state = screen.textinput(title=f"{score_count}/50 Guess the name", prompt="What's the next state? ").title()
    if answer_state == 'Exit':
        missing_states = []
        for states in states_list:
            if states not in correct_guesses:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing Names to remember.csv")
        break
    if answer_state in states_list:
        x_index = x_cor[states_list.index(answer_state)]
        y_index = y_cor[states_list.index(answer_state)]
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.goto(x_index, y_index)
        my_turtle.write(answer_state)
        correct_guesses.append(answer_state)
        score_count += 1

if score_count == 50:
    print("You guessed all correct. Congratulations")

print(missing_states)











# screen.exitonclick()
