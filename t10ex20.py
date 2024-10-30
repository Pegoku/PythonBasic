def superposicio(llista1, llista2):
    superposicio = set(llista1) & set(llista2)
    if superposicio != '':
        print(superposicio)
    else:
        print("No hi ha cap element en comú")

superposicio([1,2,3,4,5], [5,2,7,9])