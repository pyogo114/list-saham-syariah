import random

# 0 batu, 1 kertas, 2 gunting
you = int(input("Selamat datang di batu, kertas, gunting. Pilih 0 untuk batu, 1 untuk kertas dan 2 untuk gunting."))
comp = random.randint(0,2)
if you == comp:
    print("Seri!")
elif you == 0: #batu
    if comp == 1:
        print("Computer pilih : Kertas. Kamu kalah!")
    else:
        print("Computer pilih : Gunting. Kamu menang!")
elif you == 1: #kertas
    if comp == 0:
        print("Computer pilih : Batu. Kamu menang!")
    else:
        print("Computer pilih : Gunting. Kamu kalah!")
elif you == 2: #gunting
    if comp == 0:
        print("Computer pilih : Batu. Kamu kalah!")
    else:
        print("Computer pilih : Kertas. Kamu menang!")
else:
    print ("Kamu pilih apa? Kamu kalah dong!")