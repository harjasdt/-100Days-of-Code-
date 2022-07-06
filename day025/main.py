# with open("weather_data.csv") as file:
#     list = file.readlines()
# print(list)

# import csv
# with open("weather_data.csv") as file:
#     data=csv.reader(file)
#     temperature=[]
#     for row in data:
#         temperature.append(row[1])
#
#     temperature.pop(0)
#     for i in range(0, len(temperature)):
#         temperature[i]=int(temperature[i])
#     print(temperature)

import pandas
data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = 0
black_count = 0
cin_count = 0
for color in data["Primary Fur Color"]:
    if color == "Gray":
        grey_count += 1
    elif color == "Black":
        black_count += 1
    elif color == "Cinnamon":
        cin_count += 1
    else:
        pass

new_dict={
    "color" : ["grey", "black", "red"],
    "count" : [grey_count, black_count ,cin_count]
}

new_data = pandas.DataFrame(new_dict)
new_data.to_csv("count.csv")
