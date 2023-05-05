#import csv

#temperatures = []

#with open("./file.csv") as file:
#    csvdata = csv.reader(file)

#    for row in csvdata:
#        if not row[1] == "temp":
#            temperatures.append(int(row[1]))

#print(temperatures)


import pandas

data = pandas.read_csv("file.csv")
print(data["temp"])


