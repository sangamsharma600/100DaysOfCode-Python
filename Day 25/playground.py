###########################################################
# Addition with *args (Unlimited Positional Arguements) # 
def add(*num):
    sum=0
    for n in num:
        sum+=n
    return sum
        
print(add(5,6,9,20,13))
############################################################

############################################################
def calculate(**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
 
    print(kwargs["add"])
calculate(add=3, multiply=5)
#############################################################