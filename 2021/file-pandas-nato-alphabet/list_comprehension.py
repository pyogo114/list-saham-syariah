
# Buka file 1 dan file 2
# File 1
from distutils.command.clean import clean

def bacafile(alamat):
    with open(alamat) as file:
        l_file = file.readlines()
        clean_file = [int(s.replace("\n", "")) for s in l_file ]
        return clean_file

angka1 =bacafile("file1.txt")
angka2 = bacafile("file2.txt")

tersaring = [n for n in angka1 if n in angka2 ]
print(tersaring)
