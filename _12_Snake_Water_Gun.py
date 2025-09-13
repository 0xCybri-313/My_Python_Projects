import random

def result(player, computer):
    if player == computer:
        print("Draw")
    elif player == 0 and computer == 1:
        print("Win")
    elif player == 0 and computer == 1:
        print("Win")
    elif player == 1 and computer == 2:
        print("Win")
    elif player == 2 and computer == 0:
        print("Win")
    else:
        print("Lose")

    
def choices(choice):

    if choice.lower == "snake":
        choice = 0

    elif choice.lower == "water":
        choice = 1

    else :
        choice = 2

    return choice

# Game like rock paper secssior

print('''Enter "Snake", "Water" or "Gun"
''')
playerchoice = str(input())

playerchoice = choices(playerchoice)

computerchoice = random.randrange(0, 3)

result(playerchoice, computerchoice)