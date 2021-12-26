file=open('Day 22/text.txt')
contents=file.read()
print(contents)
write_text=open('Day 22/text.txt',mode='w')
file.close()

with open('Day 22/text.txt',mode='w') as file2:
    file2.write('This is a new text.')
    print(file)

with open('Day 22/text.txt',mode='a') as file2:
    file2.write(' This is a appended text.')
    print(file2)