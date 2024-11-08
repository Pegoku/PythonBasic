num = int(input("Introdueix un nombre: "))

listdigits = []

for i in range(len(str(num))):    
    listdigits.append(int(str(num)[i]))
# print (listdigits)
for i in listdigits:
    if i % 2 == 0:
        print("El dígit {} és parell".format(i))