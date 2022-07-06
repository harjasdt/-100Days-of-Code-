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
data= pandas.read_csv("weather_data.csv")
list= data["temp"].max()
print(data[data.temp==list])

