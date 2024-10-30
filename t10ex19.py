def es_palindrom():
    palindrom = input("Introdueix una paraula: ")
    if palindrom == palindrom[::-1]:
        print("És un palíndrom")
    else:
        print("No és un palíndrom")

es_palindrom()