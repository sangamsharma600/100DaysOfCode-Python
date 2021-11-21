#/*SCISSORS PAPERS AND ROCK*\#
import random

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

papers='''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

rock='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

print("Welcome to the game...........")
choose=int(input("Choose:\n1 for scissors,2 for paper and 3 for rock: "))
if choose>=1 and choose<=3:
    print(choose)
    if choose==1:
        print(f"You choose scissors.\n{scissors}")
    elif choose==2:
        print(f"You choose papers.\n{papers}")
    elif choose==3:
        print(f"You choose rock.\n{rock}")
    com_choose=random.randint(1,3)
    if com_choose==1:
        print(f"Computer choose scissors.\n{scissors}")
    elif com_choose==2:
        print(f"Computer choose papers.\n{papers}")
    elif com_choose==3:
        print(f"Computer choose rock.\n{rock}")
    else:
        print("Enter a valid choice.")

    if choose==1 and com_choose==2:
        print("You win!")
    elif choose==1 and com_choose==3:
        print("You Lose.")
    elif choose==2 and com_choose==1:
        print("You Lose.")
    elif choose==2 and com_choose==3:
        print("You Win!.")
    elif choose==3 and com_choose==1:
        print("You Win!.")
    elif choose==3 and com_choose==2:
        print("You Lose.")
    elif choose==com_choose:
        print("\nGame Draw\n")
    else:
        print("You entered an invalid key. You loose.")
else:
    
    print("Enter a valid choice.")