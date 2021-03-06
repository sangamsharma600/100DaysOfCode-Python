# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()

##################################################################


import pandas

data=pandas.read_csv("Day 24/nato_phonetic_alphabet.csv")
# print (data.to_dict())
phonetic_dict = {row.letter:row.code for (_, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
repeat = True
while repeat == True:
    word = input("Enter a word: ").upper()
    try:
        phonetic_code_word = [phonetic_dict[letter] for letter in word]
        print(f"{phonetic_code_word} \n")
        repeat = False
        
    except KeyError as error_message:
        print("Please enter a alphabet only. \n")
    
