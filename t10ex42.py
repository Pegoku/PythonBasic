num = int(input("Introdueix un nombre: "))

resultat = 0
for i in range(len(str(num))):    
    resultat = resultat + int(str(num)[i])

print("La suma dels dígits del nombre introduit és: {}".format(resultat))
if resultat % 2 == 0:
    print("La suma dels dígits és parell")
else:
    print("La suma dels dígits és senar")