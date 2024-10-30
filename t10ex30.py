def mostrar_majors_que(input, num):
    return [i for i in input if i > num]

print(mostrar_majors_que([1, 2, 3, 4, 5, 6, 5], 3))