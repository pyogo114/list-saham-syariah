# Calculator

def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def devide(n1,n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : devide,
}

# function = operation["*"]
# function(2,3)

def calculator():

    play = True
    
    num1 = int(input("Whats is the first number?"))
    
    while play:
    
        num2 = int(input("What is the second number?"))

        for key in operation:
            print(key)

        op = input("What is the operation?")

        function = operation[op]
        
        hasil = function(num1,num2)
        
        print(f"Hasil perhitungan adalah {hasil}")
        
        respond = input(f"Ketik 'yes' menghitung dengan {hasil}, memulai baru 'restart' atau 'no' keluar. ")
        
        if respond == "yes":

            num1 = hasil

        elif respond == "restart":
            
            play = False

            calculator()

        else:
            play = False

calculator()