def hi_ha_duplicats(numlist):
    if len(numlist) == len(set(numlist)):
        return "No hi ha duplicats"
    else:
        return "Hi ha duplicats"


print(hi_ha_duplicats([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]))