#Ceaser Cipher#

alphabets=[
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
]




    

enc_dec=input("What would you like to do ? Encrypt or Decrypt :").lower()
if enc_dec=='encrypt' or enc_dec=='decrypt':
    shifts=int(input("How much shift do you want ?"))
    text=input("Enter your text: ").lower()

def encrypt(text,shifts):
    encrypted_text=''
    for letter in text:
        old_position=alphabets.index(letter)
        new_position=old_position+shifts
        encrypted_text +=alphabets[new_position]
    print(f"Your encrypted text is {encrypted_text}")


def decrypt(text,shifts):
    decrypted_text=''
    for letter in text:
        old_position=alphabets.index(letter)    
        new_position=old_position-shifts
        decrypted_text+=alphabets[new_position]
    print(decrypted_text)


# encrypt(text=text,shifts=shifts)

if enc_dec=='decrypt':
    decrypt(text,shifts)
elif enc_dec=='encrypt':
    encrypt(text,shifts)
else:
    print('Please enter encrypt or decrypt')
