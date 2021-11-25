import random
import hangman_words
import hangman_ascii
#Hangman Game#


lives=6
guesses_letters=[]
is_game_over=False

choosen_word=random.choice(hangman_words.words)
# print(f"Choosen word is : {choosen_word}")
#/******************************\#
print(hangman_ascii.icon)
print('Welcome to Hangman ..........')
for _ in choosen_word:
        guesses_letters.append('_')
while not is_game_over:
    char=input('Guess a letter: ').lower()
    for i in range(0,len(choosen_word)):
        if choosen_word[i]==char:
            if char in guesses_letters:
                print(f"You have already guessed this lettter.{char}\n")

            guesses_letters[i]=char
            
    print(guesses_letters)

    if not choosen_word.__contains__(char):
        print(f"The word you've choosen : {char}, is not in the word\n")
        print(hangman_ascii.hangman[lives-1])
        lives-=1
        if lives==0:
            print("Game Over!\n")
            is_game_over=True
    if "_" not in guesses_letters:
        is_game_over=True
        print("You win ! \n")

# END OF CODE #
    
    



