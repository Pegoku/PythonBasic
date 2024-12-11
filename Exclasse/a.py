def llegir_llista():
    llista = []
    a = "a"
    
    while a != "":
        a = input("Introdueix un element de la llista: ")
        if a != "":
            llista.append(a)
    return llista

def paraulaMesLlarga(llista):
    paraula = ""
    nLlargaries = {}
    for i in llista:
        if len(i) > len(paraula):
            paraula = i
        nLlargaries[len(i)] = nLlargaries.get(len(i), 0) + 1
    nLlargaries = dict(sorted(nLlargaries.items()))
    return paraula, nLlargaries

def main():
    llista = llegir_llista()
    paraula, nLlargaries = paraulaMesLlarga(llista)
    
    print("La paraula més llarga és: {}".format(paraula))
    for i in nLlargaries:
        print("Hi ha {} paraules de llargaria {}".format(nLlargaries[i], i))
        
if __name__ == "__main__":
    main()
    