from calculator import logo

def add(num1,num2):
  return num1+num2

def subtract(num1,num2):
  return num1-num2

def multiply(num1,num2):
  return num1*num2

def divide(num1,num2):
  return num1/num2

total=0 

calc_dict={
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide,
}


def calculator():
    print(logo)

    want_continue=True

    operand1=float(input('Enter the first number: '))
    for key in calc_dict:
        print(key)

    operator=input("Enter the operator you want : ")

    operand2=float(input('Enter the second number: '))

    total = round(calc_dict[operator](operand1,operand2),2)

    print(f"{operand1} {operator} {operand2} = {total}")

    while want_continue:
        choice=input('Do you want another operation? Press \'y\' to continue and \'n\' to start a new calculation: ').lower()
        if choice=='y':
            operator=input("Enter the operator you want : ")
            operand3=float(input('Enter another number : '))
            old_total=total
            total=round(calc_dict[operator](total,operand3),2)
            print(f"{old_total} {operator} {operand3} = {total}")
        else:
            want_continue=False
            calculator()
    
calculator()

#END OF CODE#



