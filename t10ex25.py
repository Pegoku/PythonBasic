def paraula_mes_llarga(paraules):
    paraula_llarga = ""
    for paraula in paraules:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga = paraula
    return paraula_llarga

print(paraula_mes_llarga(['hola', 'adeu', 'bon dia', 'buenas tardes', 'buenas noches']))