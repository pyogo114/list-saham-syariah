#Password generator hard

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

panjangpswd = jumlahangka + jumlahhuruf + jumlahsimbol

n = 0

while n < panjangpswd:

    i = random.randint(0,2)

    if i == 0 and jumlahhuruf > 0:

        pswd = pswd + huruf[random.randint(0,51)]
        
        jumlahhuruf -= 1

        n += 1

        continue
    
    elif i == 1 and jumlahangka > 0:

        pswd = pswd + angka[random.randint(0,9)]

        jumlahangka -= 1

        n += 1

        continue
    
    elif i == 2 and jumlahsimbol > 0:

        pswd = pswd + simbol[random.randint(0,8)]

        jumlahsimbol -= 1

        n += 1

        continue
    
    else:     
        continue


print(f"Paswordnya : {pswd}")

print(f"Panjang password : {len(pswd)}")