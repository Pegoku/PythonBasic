print("Calculadora Simple V1")

def suma():
    num1 = float(input("Introdueix el primer numero: "))
    num2 = float(input("Introdueix el segon numero: "))
    print("El resultat de la suma es: ", num1 + num2)

def resta():
    num1 = float(input("Introdueix el primer numero: "))
    num2 = float(input("Introdueix el segon numero: "))
    print("El resultat de la resta es: ", num1 - num2)

def multiplicacio():
    num1 = float(input("Introdueix el primer numero: "))
    num2 = float(input("Introdueix el segon numero: "))
    print("El resultat de la multiplicacio es: ", num1 * num2)

def divisio():
    num1 = float(input("Introdueix el primer numero: "))
    num2 = float(input("Introdueix el segon numero: "))
    print("El resultat de la divisio es: ", num1 / num2)

def elevar():
    num = float(input("Introdueix el numero: "))
    exponent = float(input("Introdueix l'exponent: "))
    print("El resultat de l'operacio es: ", num ** exponent)

def canviar_base():
    option = int(input("Vols convertir de (1: binari, 2: octal:, 3: decimal, 4: hexadecimal): "))
    match(option):
        case 1:
            num = int(input("Introdueix el numero: "))
            print("El numero en binari es: ", bin(int(str(num), 2)))
            print("El numero en octal es: ", oct(int(str(num), 2)))
            print("El numero en decimal es: ", int(str(num), 2))
            print("El numero en hexadecimal es: ", hex(int(str(num), 2)))
            
        case 2:
            num = input("Introdueix el numero: ")
            print("El numero en binari es: ", bin(int(str(num), 8)))
            print("El numero en octal es: ", oct(int(str(num), 8)))
            print("El numero en decimal es: ", int(str(num), 8))
            print("El numero en hexadecimal es: ", hex(int(str(num), 8)))
            
        case 3:
            num = int(input("Introdueix el numero: "))
            print("El numero en binari es: ", bin(int(str(num), 10)))
            print("El numero en octal es: ", oct(int(str(num), 10)))
            print("El numero en decimal es: ", int(str(num), 10))
            print("El numero en hexadecimal es: ", hex(int(str(num), 10)))
        
        case 4:
            num = input("Introdueix el numero: ")
            print("El numero en binari es: ", bin(int(str(num), 16)))
            print("El numero en octal es: ", oct(int(str(num), 16)))
            print("El numero en decimal es: ", int(str(num), 16))
            print("El numero en hexadecimal es: ", hex(int(str(num), 16)))
        
def calc():
    option = int(input("Quina operacio vols fer? (1: suma, 2: resta, 3: multiplicacio, 4: divisio, 5: elevar, 6: canviar base:, 7: sortir): "))
    match(option):
        case 1:
            suma()
            calc()
        case 2:
            resta()
            calc()
        case 3:
            multiplicacio()
            calc()
        case 4:
            divisio()
            calc()
        case 5:
            elevar()
            calc()
        case 6:
            canviar_base()
            calc()
        case 7:
            print("Adeu")
    
calc()
