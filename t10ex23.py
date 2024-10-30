def crear_punts(count):
    output = ""
    for i in range(count):
        output += "."
    return output


for i in range(4):
    for i in range(4):
        print(crear_punts(i+1))
        
    for i in range(3, 0, -1):
        print(crear_punts(i))