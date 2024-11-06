import random
import time
import os

punts = 0
combinacio = 0
intents = 0

def inici():
    print("Benvingut a la partida de MasterMind")
    tutorial = input("Voleu una petita explicacio del joc? s/N ")
    
    if tutorial == "si" or tutorial == "s":
        print("MasterMind és un joc de lògica en el qual un jugador ha d'encertar una combinació de 4 xifres que l'altre jugador (o ordinador) ha escollit. El jugador que ha de trobar la combinació en el menor nombre d'intents i temps possibles.")
    
    playerCount = players()
        
    if playerCount == 1:
        singlePlayer()
    elif playerCount == 2:
        multiPlayer()
        
def players():
    while True:
        players = input("Voleu jugar sol o amb un altre jugador? (1/2) ")
        if players == "1":
            return 1
        elif players == "2":
            return 2
        else:
            print("Opció no vàlida")
            # print("Quants jugadors participaran, 1 o 2?")
    
def singlePlayer():
    print("Has escollit jugar sol. L'ordinador escollirà una combinació de 4 xifres. Tens 10 intents per endevinar-la.")
    input("Prem qualsevol tecla per començar a jugar...")

    os.system("clear")

    # combinacio = 1234
    global combinacio
    combinacio = random.randint(1000, 9999)
    endevinar()
    
    
def multiPlayer():
    print("Heu escollit jugar 2 persones. Un dels dos escollirà una combinació de 4 xifres, i s'altre tindra 10 intents per endevinar-la.")        
    input("Prem qualsevol tecla per començar a jugar...")

    os.system("clear")
    
    global combinacio
    combinacio = input("Introdueixi la combinacio secreta de 4 xifres (no la mostris al company): ")

    os.system("clear")

    endevinar()

    

def endevinar():
    global punts
    global combinacio
    global intents
    intents = 0
    while intents < 10:
        while True:
            guess = input("Introdueixi la combinació de 4 xifres: ")
            if len(guess) != 4:
                print("La combinació ha de ser de 4 xifres")
            else:
                break
        intents += 1
        # guess = int(input("Introdueixi la combinació de 4 xifres: "))
        
        checkGuess(guess)
    print("Fi del joc, has perdut")
    print("La combinació era: {}".format(combinacio))
    punts = 0

def checkGuess(guess):
    global combinacio
    if int(guess) == int(combinacio):
        print("Felicitats, has endevinat la combinació en {} intents!".format(intents))
        exit()
    else:
        combinacio_str = str(combinacio)
        guess_str = str(guess)
        
        correct_place = 0
        correct_content = 0
        # print("Combinació: {}".format(combinacio_str))
        for i in range(4):
            if guess_str[i] == combinacio_str[i]:
                correct_place += 1
            elif guess_str[i] in combinacio_str:
                correct_content += 1
        
        print ("Has encertat {} xifres en la posició correcta i {} xifres correctes en posicions incorrectes".format(correct_place, correct_content))
                
                
                
inici()