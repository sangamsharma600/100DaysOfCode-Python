#Ceaser Cipher#

alphabets=[
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
]

is_continue=True

while is_continue:
    enc_dec=input("What would you like to do ? Encrypt or Decrypt :").lower()
    if enc_dec=='encrypt' or enc_dec=='decrypt':
        shifts=int(input("How much shift do you want ?"))
        shifts%=26
        text=input("Enter your text: ").lower()


        def caesar(text,shifts,enc_dec):
            final_result=''
            for letter in text:
                if letter in alphabets:
                    old_position=alphabets.index(letter)
                    if enc_dec=='encrypt':
                        new_position=old_position+shifts
                        final_result+=alphabets[new_position]
                    elif enc_dec=='decrypt':
                        new_position=old_position-shifts
                        final_result+=alphabets[new_position]
                else:
                    final_result+=letter
            print(f'Your {enc_dec}ed data is {final_result}')
    
        caesar(text,shifts,enc_dec)
        result=input('Do you like to use the program again ? Yes or No : ')
        if result=='no':
            is_continue=False
            print("Thank You for using.\n Good Luck")
    else:
        print("Please enter a valid input")

    #ENDOFCODE#
