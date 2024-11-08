def sequnciaNombres(max):
    for i in range(max, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
        
sequnciaNombres(5)