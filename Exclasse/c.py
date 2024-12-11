a = ["Pere", "Jaume", "Mere", "Maria", "Joan", "Jordi"]

def lletraMitg(p):
    longitud = int(len(p))
    if longitud % 2 == 0:
        return p[longitud//2-1:longitud//2+1]
    else:
        return p[longitud//2]
l = []
for i in a:
    l.append(lletraMitg(i))

tested = []
for n, i in enumerate(l):
    for m, x in enumerate(l):
        if sorted((n,m)) in tested:
            continue
        tested.append(sorted((n,m)))
        if n == m:
            continue
        if i == x:
            if len(i) == 1:
                print("La {}a paraula ({}) i la {}a paraula ({}) tenen en comu la lletra '{}'".format(n+1, a[n], m+1, a[m], i))
            else: 
                print("La {}a paraula ({}) i la {}a paraula ({}) tenen en comu les lletres '{}' ".format(n+1, a[n], m+1, a[m], i))
            break
