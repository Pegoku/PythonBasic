def capsCount(paraula):
    count = 0
    for lletra in paraula:
        if lletra.isupper():
            count += 1
    return count

print(capsCount("HoLa"))