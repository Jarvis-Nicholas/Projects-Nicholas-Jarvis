"""
Author: Nicholas Jarvis
Date: 1/30/2023
Purpose: Python Blackjack
"""

def cardArt(card):

    # String partition
    splitWord = card.split()
    firstWord = splitWord[0]
    lastWord = splitWord[-1]

    # Border
    art = ["......."]

    # Top left
    if firstWord == "Ace":
        art.append("|A    |")
    elif firstWord == "10":
        art.append("|10   |")
    elif firstWord == "Jack":
        art.append("|J    |")
    elif firstWord == "Queen":
        art.append("|Q    |")
    elif firstWord == "King":
        art.append("|K    |")
    else:
        art.append("|" + firstWord + "    |")  

    # Border
    art.append("|     |")

    # Middle
    if lastWord == "Hearts":
        art.append("|  ♥  |")

    elif lastWord == "Spades":
        art.append("|  ♠  |") 

    elif lastWord == "Diamonds":
        art.append("|  ♦  |") 

    elif lastWord == "Clubs":
        art.append("|  ♣  |") 

    # Border
    art.append("|     |")

    # Bottom right
    if firstWord == "Ace":
        art.append("|    A|")
    elif firstWord == "10":
        art.append("|   10|")
    elif firstWord == "Jack":
        art.append("|    J|")
    elif firstWord == "Queen":
        art.append("|    Q|")
    elif firstWord == "King":
        art.append("|    K|")
    else:
        art.append("|    " + firstWord + "|")  

    # Border
    art.append(".......")
    return art