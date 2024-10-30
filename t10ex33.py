def es_de_traspas(anyActual):
    if anyActual % 4 == 0:
        if anyActual % 100 == 0:
            if anyActual % 400 == 0:
                print("l'any {} es de traspas.".format(anyActual))
            else:
                print("l'any {} no es de traspas.".format(anyActual))
        else:
            print("l'any {} es de traspas.".format(anyActual))
    else:
        print("l'any {} no es de traspas.".format(anyActual))

es_de_traspas(2024)