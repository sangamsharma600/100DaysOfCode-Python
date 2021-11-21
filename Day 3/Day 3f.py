#/*Treasure Island Game*\#
print("Welcome to Treasure Island.......")
print("You have to find a treasure in this island: ")
move=input("You are at the center of the island. Where do you want to go ? \n Left or Right: ")
move=move.lower()
if move=='left':
    choice=input("You came to a great ocean. What do you like to do ?\nWait or Swim: ")
    choice=choice.lower()
    if choice=='wait':
        doors=input("Thank God. A boat came and take you to the house.\nThere are three doors, which do you want to open ?\nYellow, Blue or Red : ")
        doors=doors.lower()
        if doors=='yellow':
            print('You win. Congratulations.')
        elif doors=='red':
            print("You are burned by fire. Gave Over.")
        elif doors=='blue':
            print("You are eaten by beasts. Game Over.")
        else:
            print("You went to the washroom. Game Over.")
    elif choice=='swim':
        print("You are attacked by a trout. Game Over")
    else:
        print("You made a dumb choice. Game Over.")
elif move=='right':
    print("You fell into a hole. Game Over")
else:
    print("You made a dumb choice. Game Over")

 
#END OF CODE#