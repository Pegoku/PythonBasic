print("Aixo es una applicacio de comprovacio de rima.")
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

def checkRima(paraula1, paraula2):
    if paraula1[-3:] == paraula2[-3:]:
        print("Les paraules rimen")
    elif paraula1[-2:] == paraula2[-2:]:
        print("Les paraules rimen un poc")
    elif paraula1[-1:] == paraula2[-1:]:
        print("Les paraules casi no rimen")
    else:
        print("Les paraules no rimen") 
        
checkRima(paraula1, paraula2)