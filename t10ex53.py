def sumaEntre(num1, num2):
    suma = 0
    for i in range(num1, num2 + 1):
        suma += i
    return suma

print(sumaEntre(1, 10))