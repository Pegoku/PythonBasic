def crear_llista_fitxer(filename):
    llista = []
    wordsFile = open(filename, "r")
    for line in wordsFile:
        for word in line.split():
            llista.append(word.strip())
    wordsFile.close()
    return llista

print(crear_llista_fitxer("words.txt"))