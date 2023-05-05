#Password generator

import random

huruf = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y',
'z','A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','Q','Y','Z']

angka = ['0','1','2','3','4','5','6','7','8','9']

simbol = ['!','#','$','%','&','(',')','*','+']

print("Selamat datang di password generator!")

jumlahhuruf = int(input("Berapa jumlah huruf yang diingkan? "))

jumlahangka = int(input("Berapa jumlah angka? "))

jumlahsimbol = int(input("Berapa jumlah simbol? "))

# Easy
pswd = ""

for _ in range(jumlahhuruf):
    pswd = pswd + huruf[random.randint(0,51)]

for _ in range(jumlahangka):
    pswd = pswd + angka[random.randint(0,9)]

for _ in range(jumlahsimbol):
    pswd = pswd + simbol[random.randint(0,8)]

print(f"Paswordnya : {pswd}")
