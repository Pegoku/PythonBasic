a = 0
e = 0
i = 0
o = 0
u = 0

def comptar_vocals(paraula):
    global a, e, i, o, u
    for lletra in paraula:
        if lletra == "a":
            a += 1
        if lletra == "e":
            e += 1
        if lletra == "i":
            i += 1
        if lletra == "o":
            o += 1
        if lletra == "u":
            u += 1
    # return a, e, i, o, u

comptar_vocals("hola")

print("a:", a, "\ne:", e, "\ni:", i, "\no:", o, "\nu:", u)