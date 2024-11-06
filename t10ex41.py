num = 0

while num < 1 or num > 20:
    num = int(input("Introdueix un nombre entre 1 i 20: "))

def taulaMultiplicar(num):
    for i in range(1, 11):
        print("{} * {} = {}".format(num, i, num*i))
        
taulaMultiplicar(num)