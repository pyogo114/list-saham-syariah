#urutan hangman
# 1 ambil kata secara acak
import random, string
from english_words import words
from hangman_logo import stages,logo

print(logo)

kata_pilihan = random.choice(words).upper()

while "-" in kata_pilihan or " " in kata_pilihan:
    kata_pilihan = random.choice(words).upper()

#print(f"Kata yang dipilih komputer : {kata_pilihan}")

# 2 Perintahkan user untuk menebak huruf apa dalam kata tersebut dan masukkan \
# dalam variabel. Rubah huruf tebakan dalam huruf kecil

list_display = [] #create list

nyawa = 6

for _ in range(len(kata_pilihan)):  # Mengisi list
    list_display += "_"     

# While loop bahwa di list sudah tidak ada lagi '_'
# While loop akan berhenti dan print kamu menang.

end_game = False

while not end_game and nyawa > 0:

    huruf_tebak = input("Tebak huruf apa yang ada di kalimat rahasia : ").upper()

    # 3 Cek apakah huruf dalam kata tebakan tersebut ada dalam salah satu kata komputer.
    if huruf_tebak in kata_pilihan:
        for posisi in range(len(kata_pilihan)): # posisi bila digabungkan dengan len maka ia jadi char huruf
            huruf_komputer = kata_pilihan[posisi]   # kata_pilihan adalah string dengan posisi maka char

            if huruf_komputer == huruf_tebak:
                list_display[posisi] = huruf_tebak
    else:
        nyawa -= 1

    print(stages[nyawa])
    
    print(list_display)

    if "_" not in list_display:
        print("Kamu Menang!")
        end_game = True

if nyawa == 0:
    print("Kamu kalah!!!")

print(f"Kata yang benar : {kata_pilihan}")

  
