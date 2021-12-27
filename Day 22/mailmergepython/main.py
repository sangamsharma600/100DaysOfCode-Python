DEFAULT_TEXT = '[name]'

with open('input/names/invited_names.txt') as names_list:
    names = names_list.readlines()

with open('input/letters/starting_letter.docx') as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(DEFAULT_TEXT, stripped_name)
        with open(f"output/ReadyToSend/letter_for_{stripped_name}.docx", mode='w') as final_letter:
            final_letter.write(new_letter)
