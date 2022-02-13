#/*Password Generator*\#
import random
letter=0
password=0
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

letters=['1','2','3','4','5','6','7','8','9','0']
symbols=['~','!','@','#','$','%','^','&','*','(',')','-','_','=','+']


print("Generate a stronger password ........")
num_alphabet=int(input("How many alphabets would you like to use in your password : "))
num_letters=int(input("How many letters do you want : "))
num_symbols=int(input('How many symbols do you want : '))
total_length=int(num_letters)+int(num_alphabet)+int(num_symbols)

# combined_letters=alphabets+symbols+letters

password=""
strong_password=""
for i in range(0,num_alphabet):
    char=str(random.choice(alphabets))
    password+=char

for i in range(0,num_letters):
    char=str(random.choice(letters))
    password+=char

for i in range(0,num_symbols):
    char=str(random.choice(symbols))
    password+=char


print(f"\nYour generated password is : {password}")
print(f"Your generated stronger password is : {strong_password.join(random.sample(password,len(password)))}\n")

# END OF CODE #




