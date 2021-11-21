#/*Who will Pay the Bill*\#
import random
print("Who will pay the bill today ...........")
names=input("Enter everybody's name in your group : ")
names=names.split(", ")
luck=random.randint(0,len(names)-1)
print(f"{names[luck]} will pay the bill today.")

#END OF CODE# 