# Squirel data
import pandas

data = pandas.read_csv("SquirrelData.csv")

# data brown
gray, cinnamon, black = 0,0,0
#print(data.columns.to_list())

# Dari tabel "data" ambil row yang "Primary Fur Color" nya Gray, masukkan ke var gray 
gray = data[data["Primary Fur Color"] == "Gray"]

# Lalu hitung berapa jumlah data squirrel gray yang ada?
print(len(gray))

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
print(len(cinnamon))

black = data[data["Primary Fur Color"] == "Black"]
print(len(black))

d_squirrel = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [len(gray),len(cinnamon),len(black)],
}

tabel = pandas.DataFrame(d_squirrel)
print(tabel)

# Mengambil data series dari dataframe ( 1 cell data dari tabel)
print(tabel.loc[tabel['Fur Color']=='Gray','Fur Color'].values[0])


#untuk print ke csv
#tabel.to_csv("squirrel_count.csv")
