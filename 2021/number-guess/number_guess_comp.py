import random 

def tebakankomputer(x,y):
    z = random.randint(x,y)
    return z
        

angkarandom = int(input(f"Masukan angka integer tebakan anda (1-1000)")) 
#3
angkastart = 1
angkaend = 1000
angkatebakan = tebakankomputer(angkastart,angkaend)
tepat = 0

while tepat != 3:
    print(f"Tebakan komputer adalah : {angkatebakan}")    
    cek = int(input(f"Apakah tebakan komputer terlalu rendah (1), terlalu tinggi (2) atau tepat(3)? "))
        
    if cek == 1:
        angkastart = angkatebakan + 1
           
        
    elif cek == 2:
        angkaend = angkatebakan - 1
    
    else:    
        print("Tepat!")
        tepat = 3
    
    angkatebakan = tebakankomputer(angkastart,angkaend)         
        

