# Versi kedua seperti sebelumnya

# Ambil nama file
with open("./Input/Names/invited_names.txt", mode="r") as file_names:
    l_names = file_names.readlines()

# Ambil blank letter
with open("./Input/Letters/starting_letter.docx", mode="r") as file_letter:
    blankletter = file_letter.read()

# Looping sepanjang nama list undangan
for name in l_names:

    # Sisipkan nama undahngan ke undangan kosong
    shortname = name.strip()
    letterwithname = blankletter
    letterwithname = letterwithname.replace("[name]", shortname)

    # buat file baru dengan undangan yang sudah bernama
    with open("./Output/ReadyToSend/letter_for_" + shortname + ".docx",mode="w") as file_jadi:
        file_jadi.write(letterwithname)

    letterwithname = ""


