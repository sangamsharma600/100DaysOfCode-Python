#Statement Flow#
#/*Pizza ordering system*\
print("Welcome to Pizza Ordering App")
bill=0
#PRICES
small_pizza=15
medium_pizza=20
large_pizza=25
size=input("Enter the size of pizza you want : S , M , L :")
add_pepperoni=input("Do you want to add pepperoni ? Y or N:")
add_cheese=input("Do you want extra cheese ? Y or N:")

if size =='S' or size=='s':
    bill=small_pizza
elif size=='M'or size=='m':
    bill=medium_pizza
elif size=='L'or size=='l':
    bill=large_pizza
else:
    bill += 25

if add_pepperoni=='Y' or add_pepperoni=='y':
    if size=='S'or size=='s':
        bill +=2
    else:
        bill+=3

if add_cheese=='Y' or add_cheese=='y':
    bill+=1

print(f"Your total bill is : ${bill}")


#END OF COEE#