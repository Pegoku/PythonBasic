def noms_que_comencen_per(noms, lletra):
    return [nom for nom in noms if nom[0] == lletra]

print(noms_que_comencen_per(["Joan", "Maria", "Pere", "Anna"], "M"))