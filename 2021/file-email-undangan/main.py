#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Ambil nama file
file_names = open("./Input/Names/invited_names.txt", mode="r")
l_names = file_names.readlines()
#print(l_names)
file_names.close()
#print(l_names[0].strip())

# Buka surat undangan
file_letter = open("./Input/Letters/starting_letter.docx", mode="r")
blankletter = file_letter.read()
file_letter.close()

# Looping sepanjang nama list undangan
for name in l_names:
    #print(name.strip())
    # Sisipkan nama undahngan ke undangan kosong
    shortname = name.strip()
    letterwithname = blankletter
    letterwithname = letterwithname.replace("[name]", shortname)

    # print atas namanya sendiri
    file_jadi = open("./Output/ReadyToSend/letter_for_" + shortname + ".docx",mode="w")
    file_jadi.write(letterwithname)
    file_jadi.close()
    letterwithname = ""


