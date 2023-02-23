"""
Author: Nicholas Jarvis
Date: 1/30/2023
Purpose: Python Blackjack
"""

import card_art

class GameParticipant:

    # default constructor
    def __init__(self):
        self.hand = []
        self.wins = 0
        self.sum = 0
        self.isStanding = False
        self.aceCount = 0
        self.alternateAceSum = 0

    # clear stats / hand
    def newGame(self):
        self.hand.clear()
        self.sum = 0
        self.isStanding = False
        self.aceCount = 0
        self.alternateAceSum = 0

    def aceCombos(self):

        if self.aceCount == 1:
            self.alternateAceSum = self.sum + 11

        elif self.aceCount > 1:
            self.alternateAceSum = self.alternateAceSum + 1

        # Sum will always be the smaller possibility
        self.sum = self.sum + 1

    def determineSum(self, card):
        
        # String partition
        splitWord = card.split()
        firstWord = splitWord[0]

        # Ace
        if firstWord == "Ace":
            self.aceCount = self.aceCount + 1
            self.aceCombos()

        # Face cards
        elif firstWord == "Jack" or firstWord == "Queen" or firstWord == "King":
            self.sum = self.sum + 10
            self.alternateAceSum = self.alternateAceSum + 10
        
        # 1-10 cards
        else:
            self.sum = self.sum + int(firstWord)
            self.alternateAceSum = self.alternateAceSum + int(firstWord)

        # 11 Ace winner
        if self.alternateAceSum == 21:
            self.sum = 21
        
    def hit(self, card):
        self.hand.append(card)
        self.determineSum(card)
         
    def stand(self):
        self.isStanding = True

        # If alternate Ace is a better hand, regard it as the better hand
        if self.alternateAceSum >= self.sum and self.alternateAceSum <= 21:
            self.sum = self.alternateAceSum

    def isBusted(self):
        if self.sum > 21:
            return True
        return False

    def displayHand(self):
        # Prints cards horizontally across termminal
        print('\n'.join(map('  '.join, zip(*[card_art.cardArt(self.hand[i]) for i in range(len(self.hand))]))))