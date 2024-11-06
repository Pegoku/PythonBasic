Cinicial = float(input("Introdueix la quantitat inicial: "))
while Cinicial < 50000 or Cinicial > 800000:
    print("La quantitat inicial ha de ser entre 50000 i 800000")
    Cinicial = float(input("Introdueix la quantitat inicial: "))

interes = float(input("Introdueix l'interes anual: "))
while interes < 0.5 or interes > 13:
    print("L'interes anual ha de ser entre 0.5 i 13")
    interes = float(input("Introdueix l'interes anual: "))
    
anys = float(input("Introdueix el nombre d'anys: "))    
while anys < 3 or anys > 40:
    print("Els anys han de ser entre 3 i 40")
    anys = float(input("Introdueix el nombre d'anys: "))

Cfinal = round(Cinicial * (1 + interes/100) ** anys, 2)

print ( "{}€ a {}% d’interés a {} anys s’ha de convertir en {}€".format(Cinicial, interes, anys, Cfinal))