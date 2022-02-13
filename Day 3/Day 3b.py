#/*BMI Calculator Version 2.0*\#
height=float(input("Enter your height in meter : "))
weight=float(input("Enter your weight in kg : "))
bmi=round(weight/(height*height),1)
if bmi<18.5:
    print(f"Your BMI is : {bmi}.You are underweight.")
elif bmi>18.5 and bmi<25:
    print(f"Your BMI is : {bmi}. You have a normal weight.")
elif bmi>25 and bmi<30:
    print(f"Your BMI is : {bmi}. You have overweight.")
elif bmi>30 and bmi<35:
    print(f"Your BMI is : {bmi}. You are obese.")
else:
    print(f"Your BMI is : {bmi}. You have clinically obese.")

    #END OF CODE#