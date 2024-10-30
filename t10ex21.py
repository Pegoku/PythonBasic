def crear_repetits(count, item):
    output = ""
    for i in range(count):
        output += item
    return output

print(crear_repetits(25, 'hola'))