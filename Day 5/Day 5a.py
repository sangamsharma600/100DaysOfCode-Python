#/*Average Marks Calculator*\#
print("\nWecome to average marks calculator: \n")
total=0
numOfSubjects=0
average=0
marks=input("Enter the marks from each subject: ").split()
for i in marks:
    marks=int(i)
    total+=marks
    numOfSubjects+=1
print("\n*********************\n")
average=total/numOfSubjects
print(round(average))
print("\n*********************\n")


#END OF CODE#

