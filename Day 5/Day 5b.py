#/*Highest Number Fider*\#
print("Welcome to highest number finder........")
numbers=input("Enter the numbers : ").split()
max=0
for i in range(0,len(numbers)):
    numbers[i]=(int(numbers[i]))
    if max<numbers[i]:
        max=numbers[i]
print(f"The maximum number is : {max}")

#END OF CODE#