def dibuixPunts(max):
    for i in range(1, max+1):
        print("*" * i)
    for i in range(max-1, 0, -1):
        print("*" * i)

dibuixPunts(5)