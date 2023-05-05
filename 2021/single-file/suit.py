# Suit
import random

def play():
    user = input("Suiit. Pilih 'j' untuk jempol, 't' telunjuk dan 'k' kelingking? ")

    comp = random.choice(['j','t','k'])

    if user == comp:
        print(f"Kamu {user}, Computer {comp} ")
        return "Seri!"
    
    if menang(user,comp):
        print(f"Kamu {user}, Computer {comp} ")
        return "Kamu menang!"
    
    print(f"Kamu {user}, Computer {comp} ")
    return "Kamu kalah!"

# j>t, t>k, k>j
def menang(u,c):
    if (u == 'j' and c == 't') or (u == 't' and c == 'k') or (u == 'k' and c == 'j'):
        return True
    

print(play())
