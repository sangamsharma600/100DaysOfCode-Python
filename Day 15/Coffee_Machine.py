# /*Coffee Machine. Serve yourself a hot cup of Cofee*\

from rate import rate_content

water=1000
coffee=400
milk=300
money_collected=0
isOver=False

is_enough_resources=True

def rate_list():
    print('\nThe rate of each coffee is : \nEspresso : Rs 40\nLatte : 90\nCappuccino : 150\n')

rate_list()

while not isOver and is_enough_resources:
    coffee_type=input('What would you like? (espresso/latte/cappuccino): ').lower()


    if coffee_type=='espresso' or coffee_type=='latte' or coffee_type=='cappuccino':
        if water>rate_content[coffee_type]['water'] and milk>rate_content[coffee_type]['milk'] and coffee>rate_content[coffee_type]['coffee']:
            money=int(input("\nEnter coin to make your coffee: "))
            if money>rate_content[coffee_type]['rate']:
                water-=rate_content[coffee_type]['water']
                coffee-=rate_content[coffee_type]['coffee']
                milk-=rate_content[coffee_type]['milk']
                print(f'\nEnjoy your {coffee_type} ☕ ☕ ☕')
                money-=rate_content[coffee_type]['rate']
                money_collected+=rate_content[coffee_type]['rate']
                print(f"\nHere is your change {money} 💵\n")
            else:
                print(f"\nNot sufficient money to make {coffee_type} 😞\n")
        else:
            if water<rate_content[coffee_type]['water']:
                print(f"\nSorry, Coffee Machine doesn't have sufficient water to make {coffee_type}")
            elif milk<rate_content[coffee_type]['milk']:
                print(f"\nSorry, Coffee Machine doesn't have sufficient milk to make {coffee_type}")
            elif coffee<rate_content[coffee_type]['coffee']:
                print(f"\nSorry, Coffee Machine doesn't have sufficient coffee to make {coffee_type}")
    elif coffee_type=='report':
        print(f"\nThe resources remaining is : \nWater :{water} ml\nMilk :{milk} ml\nCoffee :{coffee} gm\nMoney Collected: {money_collected}\n")

    elif coffee_type=='off':
        print('\nMachine Turning Off...........')
        break

    else:
        print("Please enter a valid input")

        # END OF CODE #
