# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
    # new_data = []
    #
    # for line in data:
    #     sub_list = line.rstrip().split(',')  # using rstrip to remove the \n
    #     new_data.extend(sub_list)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# Print whole DataFrame (= table)
# ===============================
print(data)

# Print some Series (column "temp")
# =================================
print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
#
# print(data["temp"].max())

# print(data[data["temp"] == data["temp"].max()])

# Get data in Row, filtered as 'Monday'
# ====================================
# monday = data[data.day == "Monday"]
# print(monday)

# Get particular Condition cell from that row (will be 'Sunny')
# =============================================================
# print(monday.condition)

#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])
#
# sunny = data[data["condition"] == "Sunny"]
# fahrenheit = 32 + ((9 * int(monday.temp)) / 5)
# print(int(sunny["condition"].count()))


# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# grey_squirrels_count =  len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count =  len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count =  len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
#
# print(data_dict)

