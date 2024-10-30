def vocal():
    lletra = input("Introdueix UNA lletra: ")
    if len(lletra) != 1:
        print("Error, has d'introduir una sola lletra")
        vocal()
    else:
        if lletra == "a" or lletra == "e" or lletra == "i" or lletra == "o" or lletra == "u":
            print("La lletra "'"{}"'" es una vocal".format(lletra))
        else:
            print("La lletra "'"{}"'" no es una vocal".format(lletra))

vocal()
