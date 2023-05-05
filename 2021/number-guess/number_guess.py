import random 

def tebak():
    angkarandom = random.randint(1,10)
    angkatebakan = 0
    
    while angkatebakan != angkarandom:
        angkatebakan = int(input(f"Masukan angka integer tebakan anda (1-10)"))
        
        if angkatebakan > angkarandom:
            print("Terlalu tinggi")
            
        elif angkatebakan < angkarandom:
            print("Terlalu rendah")
            
        else:
            print(f"Tepat angkarandom komputer adalah {angkarandom}")
        
tebak()
    