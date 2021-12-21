from turtle import Turtle
import turtle
FONT=("Arial",16,"normal")

class Scoreboard:
    
    def __init__(self):
        self.score=0
        turtle.penup()
        turtle.hideturtle()
        turtle.color('white')
        turtle.goto(0,275)

        turtle.write(f'Score : {self.score}',font=FONT,align='center')

    def increase_score(self):
        self.score+=1
        turtle.clear()
        turtle.write(f'Score : {self.score}',font=FONT,align='center')

        
    def game_over(self):
        turtle.goto(0,0)
        turtle.write('GAME OVER',font=FONT,align="center")