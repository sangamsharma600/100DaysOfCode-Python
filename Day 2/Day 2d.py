#/*Tip Calculator*\#
print("Welcome to tip calculator............")
totalBill=float(input("Enter the bill amount : "))
tipsPercent=float(input("How much percentage of tips would you like to give ? "))
split=float(input("How many people to split bill : "))
if((tipsPercent)!=0):
    tipsAmount=((totalBill)*1/(tipsPercent))
    totalAmount=tipsAmount+(totalBill)
    splittedAmount=totalAmount/(split)
    splittedAmount="{:.2f}".format(splittedAmount)
    print(f"You each should pay : Rs {splittedAmount} ")
else:
    splittedAmount=totalBill/split
    splittedAmount="{:.2f}".format(splittedAmount)
    print(f"You each need to pay : Rs {splittedAmount} ")

    #END OF CODE 
