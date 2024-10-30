def major_edat():
    anys = int(input("Quants anys tens?: "))

    if anys < 18:
        print("Ets menor d'edat")
    else:
        if anys == 18:
            print("Tens exactament 18 anys")
        else:
            print("Ets major d'edat")

major_edat()