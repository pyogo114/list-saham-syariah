#import csv

########### 1 #############
#temperatures = []

#with open("./file.csv") as file:
#    csvdata = csv.reader(file)

#    for row in csvdata:
#        if not row[1] == "temp":
#            temperatures.append(int(row[1]))
#print(temperatures)

########### 2 #############

from statistics import mean
import pandas

data = pandas.read_csv("file.csv")

#print(type(data)) # data ini DataFrame atau tabel keseluruhan, 2 dimensi x dan y
#print(data["temp"]) # data["temp"] adalah Series atau data kolom, 1 dimensi y saja

#l_data = data["temp"].to_list()
#print(l_data)
#print(mean(l_data))
#print(data["temp"].mean())
#print(data["temp"].max()) #format bisa begini
#print(data.temp.max())  # bisa juga temp itu dari header table temperature nya

########### 3 #############

# Ini adalah if ala pandas. ambil baris data table yang data.day ialah senin
#print(data[data.day == "Monday"])

# Ini adalah if ala pandas. ambil baris data table yang data.temp adalah data temperatur tertinggi
#print(data[data.temp == data.temp.max()])

#
#monday = data[data.day == "Monday"]
#print((monday.temp*1.8) + 32)

########### 4 #############

# Membuat tabel dari scratch
data_dict = {
    "Murid" : ["Amy","James","Angela"],
    "Score" : [76,56,65],
}

tabel = pandas.DataFrame(data_dict)
tabel.to_csv("CsvDariPython.csv")
print(tabel)
