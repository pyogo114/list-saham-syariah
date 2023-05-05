from art_caesar import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lanjut = True

while lanjut:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(txt, sft, drt):

        if sft > 26:
            sft = sft % 26

        txtencode = "encoded"

        if drt == "decode":
            sft *= -1
            txtencode = "decoded"

        encrypt_huruf = ""

        for huruf in txt:
            posisi = alphabet.index(huruf)
            posisi_baru = posisi + sft

            encrypt_huruf += alphabet[posisi_baru]

        print(f"The {txtencode} text is {encrypt_huruf}") 


    caesar(txt = text, sft = shift, drt = direction)
    
    is_lanjut = input("Ketik 'yes' untuk memulai lagi, ketik selain itu untuk keluar.")

    if is_lanjut != "yes":
        print("Daaggg ...")
        lanjut = False
