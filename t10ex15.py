
def longitud():
    longitud = 1
    llista = input("introdueix una llista de paraules separades per comes: ")
    for i in llista:
        if i == ",":
            longitud += 1
    print(longitud)

longitud()