# with open('Day 23/weather_data.csv') as csv_file:
#     data=csv_file.readlines()

# print(data)

# import csv
# with open("Day 23/weather_data.csv") as csv_file:
#     data=csv.reader(csv_file)
#     temperature=[]
#     for temp in data:         
#         if temp[1]!='temp':
#             temperature.append(int(temp[1]))

#     print("The temperature is : ")
#     print(temperature)


# data = pandas.read_csv('weather_data.csv')
# print(data['temp'].mean())
# print(data['temp'].max())

#  Get Data From Rows #
# print(data[data.temp == max(data.temp)])

# monday = data[data.day == 'Monday']
# monday_temperature = (monday['temp'] * 9/5) + 32
# print(monday_temperature)


#  Creating a DataFrame from Scratch  #

# data_dict = {
#     'students': ['Sangam', 'Suman', 'Kiran'],
#     'marks': [53, 65, 69]
# }

# data = pandas.DataFrame(data_dict)
# # print(data)
# print(data_dict)
# data.to_csv("new_data.csv")
import pandas


data = pandas.read_csv('squirrel_data.csv')

grey_squirrel = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])


color_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}

print(color_dict)
data = pandas.DataFrame(color_dict)
data.to_csv("Squirrel Colors Data.csv")
