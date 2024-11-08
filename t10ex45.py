def esta_ordenada(numlist):
    if numlist == sorted(numlist):
        return "ascendent"
    elif numlist == sorted(numlist, reverse=True):
        return "descendent"
    else:
        return "no ordenada"
    
print(esta_ordenada([5, 4, 2, 3, 1]))    