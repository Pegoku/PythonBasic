def filtrar_paraules(paraules, llargaria):
    paraula_llarga = ""
    for paraula in paraules:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga += paraula
    return paraula_llarga

print(filtrar_paraules(['hola', 'adeu', 'bon dia', 'buenas tardes', 'buenas noches'], 5))