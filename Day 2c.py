#/*Number of Days, Weeks and Year left*\#
#REFERENCE : https://waitbutwhy.com/2014/05/life-weeks.html #

age=input('Enter your age in years : ')
age=int(age)
yearsLeft=90-age
daysLeft=yearsLeft*365
monthsLeft=yearsLeft*12
weeksLeft=(yearsLeft*365)/7
print(f"You have {daysLeft} days, {int(weeksLeft)} weeks and {monthsLeft} months left till your death. ")

#END OF CODE
