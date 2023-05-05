
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

#print(add(10,20,30,40,50,60,70,80,90,100))

def calculate(n, **kwargs):
    #for key,value in kwargs.items():
        #print(key)
        #print(value)
    n += kwargs["add"]
    print(n)

    n *= kwargs["kali"]
    print(n)
    return n


print(calculate(2, add=3, kali=2))

class Car:

    tempatduduk = 4

    def __init__(self, **kwargs):
        self.model = kwargs["model"]    # jika pakai braket index, maka bila tidak diisi akan errror
        self.make = kwargs.get("make")  # jika pakai get, bila tidak diisi tetap bisa jalan. dia mengeluarkan none
        self.tempatduduk = kwargs.get("tempatduduk")

mycar = Car(model="Honda", make="crv")
print(mycar.tempatduduk)