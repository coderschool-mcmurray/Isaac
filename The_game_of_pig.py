#Comment your code!!

import random

def roll_da_dice():
    return random.randint(1,6)

# This class is either going to be a Robot or Human Player
class Enity:
    def __init__(self):
        self.playerType = "robot"
        self.name = ""
        self.turns = 1
        self.turntotal = 0
        self.score = 0

allPlayers = []
currentPlayer = 0

playerCount = int(input("How many players are playing? "))
if playerCount != 1:
    currentPlayer = 1
    for i in range(playerCount):
        playerT = input("Are you a human or robot?")
        allPlayers.append(i + 1)
        allPlayers[i] = Enity()
        if playerT == "human":
            allPlayers[i].playerType = "human"
            allPlayers[i].name = input("What is your name?")
else:
    allPlayers.append(1)
    allPlayers[0] = Enity()


while not any(player.score >= 100 for player in allPlayers):
    choice = ""
    if allPlayers[currentPlayer - 1].playerType == "robot":
        if allPlayers[currentPlayer - 1].turntotal == 0:
            choice = 'r'
        else:
            choice = random.choice(['r', 'b']) 
    else:
        choice = input("Would you like to roll or bank? ")

    if choice in ("roll", "r"):
        print()
        roll = roll_da_dice()
        if (allPlayers[currentPlayer - 1].playerType == "human"):
            print(allPlayers[currentPlayer - 1].name + " rolled a " + str(roll) +".")
        else:
            print("Player " + str(currentPlayer) + " rolled a " + str(roll) +".")
        if roll == 1:
            print("You rolled a 1! You get no points for this round!")
            print("Now onto the next player")
            allPlayers[currentPlayer - 1].turntotal = 0
            allPlayers[currentPlayer - 1].turns += 1
            print()
            if playerCount == currentPlayer:
                currentPlayer = 1
            elif playerCount != 1:
                currentPlayer += 1
            print()
            print("Now onto the next player")
            print("Player " + str(currentPlayer) + "'s turn")
            print("Turn " + str(allPlayers[currentPlayer - 1].turns))
            print("Your Current Score is: " + str(allPlayers[currentPlayer - 1].score))
            print("This round you have: " + str(allPlayers[currentPlayer - 1].turntotal))

        else:
            allPlayers[currentPlayer - 1].turntotal = roll + allPlayers[currentPlayer - 1].turntotal
            print("This round you have: " + str(allPlayers[currentPlayer - 1].turntotal))
    elif choice in ("bank", "b"):
        allPlayers[currentPlayer - 1].turns += 1
        allPlayers[currentPlayer - 1].score += allPlayers[currentPlayer - 1].turntotal
        allPlayers[currentPlayer - 1].turntotal = 0
        print("Banking")
        if allPlayers[currentPlayer - 1].score >= 100:
            break
        
        print()
        if playerCount == currentPlayer:
            currentPlayer = 1
        else:
            currentPlayer += 1
        
        print()
        print()
        print("Now onto the next player")
        print("Player " + str(currentPlayer) + "'s turn")
        print("Turn " + str(allPlayers[currentPlayer - 1].turns))
        print("Your Current Score is: " + str(allPlayers[currentPlayer - 1].score))
        print("This round you have: " + str(allPlayers[currentPlayer - 1].turntotal))

winner = None
for i, player in enumerate(allPlayers):
    if player.score >= 100:
        winner = i
        break
print(
    "Congratulations! Player "
    + str(winner + 1)
    + " won in "
    + str(allPlayers[winner].turns)
    + " turns!"
    + " With a final score of "
    + str(allPlayers[winner].score)
    + "."
)
