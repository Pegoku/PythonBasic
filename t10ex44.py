def eliminarcapicua(numlist):
    numlist.remove(numlist[0])
    numlist.remove(numlist[-1])
    return numlist

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(eliminarcapicua(numlist))