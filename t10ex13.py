def gran():
    num1 = float(input("Introdueix el primer numero: "))
    num2 = float(input("Introdueix el segon numero: "))
    if num1 > num2:
        print("{} es mes gran que {}".format(num1, num2))
    else:
        if num2 > num1:
            print("{} es mes gran que {}".format(num2, num1))
        else:
            print("Els dos numeros son iguals")

gran()