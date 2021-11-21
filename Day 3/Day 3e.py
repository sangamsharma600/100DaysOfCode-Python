#/*LOVE CALCULATOR*\#
print("Calculate your love percentage............")
boy=input("Enter a male name :")
girl=input("Enter a female name :")
boy=boy.lower()
girl=girl.lower()
true_count=0
love_count=0
true_count+=girl.count('t')
true_count+=girl.count('r')
true_count+=girl.count('u')
true_count+=girl.count('e')
true_count+=boy.count('t')
true_count+=boy.count('r')
true_count+=boy.count('u')
true_count+=boy.count('e')

love_count+=girl.count('l')
love_count+=girl.count('o')
love_count+=girl.count('v')
love_count+=girl.count('e')
love_count+=boy.count('l')
love_count+=boy.count('o')
love_count+=boy.count('v')
love_count+=boy.count('e')

true_count=str(true_count)
love_count=str(love_count)
score=true_count+love_count

score=int(score)
if score<10 and score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

#END OF CODE#


