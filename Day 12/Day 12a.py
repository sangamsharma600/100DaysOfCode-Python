# /*NUMBER GUESSING GAME*\ #
#For Flowchart Visit : "shorturl.at/yLM35"
from random import randint
defined_num=randint(1,100)
chances=0
is_over=False
def choosing_level():
    global chances #Using Global Variable
    level=input("Enter the level you want to play: Easy or Hard: ").lower()
    if(level=='easy'):
        chances=10
    elif(level=='hard'):
        chances=5
    else:
        print("Enter the valid input")
        choosing_level()
def take_user_input():
    global chances #Using Global Variable
    global defined_num #Using Global Variable
    global is_over
    while not is_over:
        guessed_number=int(input("Enter the guessed number between 1 to 100:"))

        if guessed_number==defined_num:
            print("Yaayyyy, You win ! 💐💐")
            print(f"The answer was {defined_num}")
            is_over=True
        elif guessed_number<defined_num:
            print("Too Low 😢")
            chances-=1
            print(f"You have now {chances} chances left")
        elif guessed_number>defined_num:
            print("To High 😃")
            chances-=1
            print(f"You have now {chances} chances left")
        if chances==0:
            print("You did not guessed the right number. \nGame Over. 😐")
            is_over=True
        else:
            take_user_input()

choosing_level()
take_user_input()

# END OF CODE #