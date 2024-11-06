resultat = 0

def quadratsAnteriors(n):
    global resultat
    while n > 0:
        resultat += n**2
        n -= 4
        
quadratsAnteriors(int(input("Quin nombre vols introduir? ")))
print("La suma dels quadrats dels nombres anteriors és: {}".format(resultat))