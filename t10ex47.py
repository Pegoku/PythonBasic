import random

def llista_20_elements():
    llista = []
    for i in range(20):
        llista.append(random.randint(1, 100))
    return (llista)
    
llista_20_elements()