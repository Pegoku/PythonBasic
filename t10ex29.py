def imprimir_taula(dades):
    print("Any actual", any_actual)
    print(f"{'Nom':<10}{'Naixement':<10}{'Edat':<5}")
    print("-" * 25)
    for nom, naixament in dades:
        edat = any_actual - naixament
        print(f"{nom:<10}{naixament:<10}{edat:<5}")

any_actual = 2023
persones = [
    ("Joan", 1980),
    ("Maria", 1995),
    ("Pere", 2000),
    ("Anna", 2010)
]

imprimir_taula(persones)
