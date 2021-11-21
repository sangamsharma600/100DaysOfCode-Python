#/*HIDE THE TREASURE*\#
row1=["✅","✅","✅"]
row2=["✅","✅","✅"]
row3=["✅","✅","✅"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
# Enter a location in a nested array format like : 13 or 32 or 23
location=input("Where do you want to hide the treasure ? : ")
column=location[0]
column=int(column)-1
row=location[1]
row=int(row)-1
map[row][column]='X'

print(f"{row1}\n{row2}\n{row3}")
