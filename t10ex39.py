num = 0
while num < 1 or num > 900000:
    num = int(input("Introdueix un nombre entre 1 i 900000: "))

        
print("El nombre introduit te {} xifres".format(len(str(num))))