import random
import time
import os

points = 0
combination = 0
attempts = 0

def start():
    print("Welcome to the MasterMind game")
    tutorial = input("Would you like a brief explanation of the game? y/N ")
    
    if tutorial.lower() in ["yes", "y"]:
        print("MasterMind is a logic game where a player has to guess a combination of 4 digits that the other player (or computer) has chosen. The player must find the combination in the fewest attempts and shortest time possible.")
    
    playerCount = players()
        
    if playerCount == 1:
        singlePlayer()
    elif playerCount == 2:
        multiPlayer()
        
def players():
    while True:
        players = input("Do you want to play alone or with another player? (1/2) ")
        if players == "1":
            return 1
        elif players == "2":
            return 2
        else:
            print("Invalid option")
    
def singlePlayer():
    print("You have chosen to play alone. The computer will choose a combination of 4 digits. You have 10 attempts to guess it.")
    input("Press any key to start playing...")

    os.system("clear")

    global combination
    combination = random.randint(1000, 9999)
    guess()
    
    
def multiPlayer():
    print("You have chosen to play with 2 players. One of you will choose a combination of 4 digits, and the other will have 10 attempts to guess it.")        
    input("Press any key to start playing...")

    os.system("clear")
    
    global combination
    combination = input("Enter the secret combination of 4 digits (do not show it to your partner): ")

    os.system("clear")

    guess()

def guess():
    global points
    global combination
    global attempts
    attempts = 0
    while attempts < 10:
        while True:
            guess = input("Enter the combination of 4 digits: ")
            if len(guess) != 4:
                print("The combination must be 4 digits")
            else:
                break
        attempts += 1
        
        checkGuess(guess)
    print("Game over, you lost")
    print("The combination was: {}".format(combination))
    points = 0

def checkGuess(guess):
    global combination
    if int(guess) == int(combination):
        print("Congratulations, you guessed the combination in {} attempts!".format(attempts))
        exit()
    else:
        combination_str = str(combination)
        guess_str = str(guess)
        
        correct_place = 0
        correct_content = 0
        for i in range(4):
            if guess_str[i] == combination_str[i]:
                correct_place += 1
            elif guess_str[i] in combination_str:
                correct_content += 1
        
        print("You have {} digits in the correct position and {} correct digits in incorrect positions".format(correct_place, correct_content))
                
start()