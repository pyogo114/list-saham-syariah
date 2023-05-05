# Prime number checker

def prime_checker(nmr):
    
    j = 2
    k = nmr -1

    print(f"{nmr} ",end="")

    for j in range(2, k):
        if nmr % j == 0:
            return "bukan prime"
    
    return "prime"

#n = int(input("Check this number? "))

lst_nmr = []

for i in range (1,100):
    lst_nmr.append(i)

for l in lst_nmr:
    print(prime_checker(l))
#prime_checker(number=n)