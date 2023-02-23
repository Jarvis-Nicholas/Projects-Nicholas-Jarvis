"""
Author: Nicholas Jarvis
Date: 1/30/2023
Purpose: Python Blackjack
"""
# Command line executables:
# python3 -m coverage run test_game_utility.py -v -b
# python3 -m coverage report 

import unittest
import game_utility as gu
import game_participant as gp

class testGameUtility(unittest.TestCase):
    
    def test_dealerMultiHit(self):

        # Deck full of 0s (to not change sum)
        zero_deck = ["0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs",
                     "0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs"]

        dealer = gp.GameParticipant()

        # Dealer Bust
        dealer.sum = 30
        gu.dealerMultiHit(zero_deck, dealer)
        self.assertTrue(dealer.isBusted())
        self.assertFalse(dealer.isStanding)

        # Dealer Standing
        dealer.sum = 18
        gu.dealerMultiHit(zero_deck, dealer)
        self.assertTrue(dealer.isStanding)
        self.assertFalse(dealer.isBusted())
    
    def test_GameOver(self):

        # Not Busted (sums are naturally 0 when initialized) and Not Standing
        player_Not_Busted = gp.GameParticipant()
        dealer_Not_Busted = gp.GameParticipant()

        # Busted 
        player_Busted = gp.GameParticipant()
        dealer_Busted = gp.GameParticipant()
        player_Busted.sum = 30
        dealer_Busted.sum = 30

        # Dealer Standing
        dealer_Standing = gp.GameParticipant()
        dealer_Standing.isStanding = True

        # Player busted
        self.assertTrue(gu.gameOver(dealer_Not_Busted, player_Busted))

        # Dealer busted
        self.assertTrue(gu.gameOver(dealer_Busted, player_Not_Busted))

        # Tie Game
        self.assertTrue(gu.gameOver(dealer_Standing, player_Not_Busted))
        self.assertEquals(dealer_Standing.sum, player_Not_Busted.sum)

        # Dealer Sum wins
        dealer_Standing.sum = 1
        self.assertTrue(gu.gameOver(dealer_Standing, player_Not_Busted))
        self.assertGreater(dealer_Standing.sum, player_Not_Busted.sum)

        # Player Sum wins
        player_Not_Busted.sum = 2
        self.assertTrue(gu.gameOver(dealer_Standing, player_Not_Busted))  
        self.assertGreater(player_Not_Busted.sum, dealer_Standing.sum)

        # No busts and no Stand
        self.assertFalse(gu.gameOver(dealer_Not_Busted, player_Not_Busted))   
    
    def test_playFirstHand(self):

        # Deck full of 0s (to not change sum)
        zero_deck = ["0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs",
                     "0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs"]

        # Player natural blackjack
        player_Natural_Blackjack = gp.GameParticipant()
        dealer = gp.GameParticipant()

        # Dealer not standing (sum == 0)
        gu.playFirstHand(dealer, player_Natural_Blackjack, zero_deck)
        self.assertFalse(dealer.isStanding)

        # Dealer standing (if branch covered)
        player_Natural_Blackjack.sum = 21
        gu.playFirstHand(dealer, player_Natural_Blackjack, zero_deck)
        self.assertTrue(dealer.isStanding)

if __name__ == '__main__':
    unittest.main()