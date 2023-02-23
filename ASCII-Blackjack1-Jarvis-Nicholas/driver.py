"""
Author: Nicholas Jarvis
Date: 1/30/2023
Purpose: Python Blackjack
"""

import game_participant
import game_utility as gu
import random


def main():

    defaultDeck = ["Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", 
                "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", 
                "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", 
                "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"]
    
    # Initial shuffle
    cardDeck = []
    for i in range (0, len(defaultDeck)):
        cardDeck.append(defaultDeck[i])
    random.shuffle(cardDeck)

    dealer = game_participant.GameParticipant()
    player = game_participant.GameParticipant()
    
    firstHand = True

    # Do while loop
    while True:
        if firstHand == True:
            gu.playFirstHand(dealer, player, cardDeck)
            firstHand = False
        else:
            userInput = int(input("Hit: 1\nStand: 2\n"))

            # Error case for input
            while userInput != 1 and userInput != 2:
                userInput = int(input("Please enter a valid input"))
            
            # Hit
            if userInput == 1:
                player.hit(cardDeck[0])
                cardDeck.pop(0)

            # Stand    
            if userInput == 2 or player.sum == 21:
                player.stand()
                gu.dealerMultiHit(cardDeck, dealer)

            gu.displayTable(dealer, player)
            
        # Game over
        if gu.gameOver(dealer, player) == True:
            while True:

                userInput = int(input("Play again: 1\nLeave Table: 0\n"))

                # Incorrect input loop
                if userInput != 1 and userInput != 0:
                    userInput = int(input("Please enter a valid input\n"))

                # Exit program
                if userInput == 0:
                    print("**************************************************")
                    print("                  ---------------\n                 | WINNING STATS |\n                  ---------------")  
                    print("Dealer wins:", dealer.wins)
                    print("Player wins:", player.wins)
                    exit()
                
                # Rematch
                elif userInput == 1:

                    # Shuffle deck
                    counter = len(cardDeck)
                    for i in range (0, counter):
                        cardDeck.pop(0)
                    for i in range (0, len(defaultDeck)):
                        cardDeck.append(defaultDeck[i])
                    random.shuffle(cardDeck)

                    # Clear relevant stats
                    dealer.newGame()
                    player.newGame()
                    firstHand = True

                    break

if __name__ == "__main__":
    main()