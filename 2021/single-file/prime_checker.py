# Prime number checker

def prime_checker(nmr):
    
    k = nmr -1

    print(f"{nmr} ",end="")

    for j in range(2, k):
        if nmr % j == 0:
            return "bukan prime"
    
    return "prime"


n = int(input("Check this number? "))

print(prime_checker(nmr = n))