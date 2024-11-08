def index_paraula(list, word):
    if word in list:
        return list.index(word)
    else:
        return -1
    
def crear_llista_fitxer(filename):
    llista = []
    wordsFile = open(filename, "r")
    for line in wordsFile:
        for word in line.split():
            llista.append(word.strip())
    wordsFile.close()
    return llista

print(index_paraula(crear_llista_fitxer("words.txt"), "AI"))