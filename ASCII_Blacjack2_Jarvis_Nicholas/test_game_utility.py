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


# Has built in integration and unit testing
class testGameUtility(unittest.TestCase):
    
    def setUp(self):

        self.dealer = gp.GameParticipant()

        # Not Busted (sums are naturally 0 when initialized) and Not Standing
        self.player_Not_Busted = gp.GameParticipant()
        self.dealer_Not_Busted = gp.GameParticipant()

        # Busted 
        self.player_Busted = gp.GameParticipant()
        self.dealer_Busted = gp.GameParticipant()
        self.player_Busted.sum = 30
        self.dealer_Busted.sum = 30

        # Dealer Standing
        self.dealer_Standing = gp.GameParticipant()
        self.dealer_Standing.isStanding = True
        self.dealer_Standing.sum = 1

        # Player natural blackjack
        self.player_Natural_Blackjack = gp.GameParticipant()
        self.player_Natural_Blackjack.sum = 21

        # Deck full of 0s (to not change sum)
        self.zero_deck = ["0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs",
                     "0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs","0 of clubs"]

    def test_dealerMultiHit_bust(self):

        # Dealer Bust
        self.dealer.sum = 30
        gu.dealerMultiHit(self.zero_deck, self.dealer)
        self.assertTrue(self.dealer.isBusted())
        self.assertFalse(self.dealer.isStanding)

    def test_dealerMultiHit_standing(self):

        # Dealer Standing
        self.dealer.sum = 18
        gu.dealerMultiHit(self.zero_deck, self.dealer)
        self.assertTrue(self.dealer.isStanding)
        self.assertFalse(self.dealer.isBusted())
    
    def test_GameOver_dealer_busted(self):

        # Dealer busted
        self.assertTrue(gu.gameOver(self.dealer_Busted, self.player_Not_Busted))

    def test_GameOver_player_busted(self):

        # Player busted
        self.assertTrue(gu.gameOver(self.dealer_Not_Busted, self.player_Busted))

    def test_GameOver_tie(self):

        # Tie Game
        self.dealer_Standing.sum = 0
        self.assertTrue(gu.gameOver(self.dealer_Standing, self.player_Not_Busted))
        self.assertEquals(self.dealer_Standing.sum, self.player_Not_Busted.sum)

    def test_GameOver_dealer_sum_wins(self):

        # Dealer Sum wins
        self.assertTrue(gu.gameOver(self.dealer_Standing, self.player_Not_Busted))
        self.assertGreater(self.dealer_Standing.sum, self.player_Not_Busted.sum)

    def test_GameOver_palyer_sum_wins(self):
        
        # Player Sum wins
        self.player_Not_Busted.sum = 2
        self.assertTrue(gu.gameOver(self.dealer_Standing, self.player_Not_Busted))  
        self.assertGreater(self.player_Not_Busted.sum, self.dealer_Standing.sum)

    def test_GameOver_no_busts_stands(self):

        # No busts and no Stand
        self.assertFalse(gu.gameOver(self.dealer_Not_Busted, self.player_Not_Busted))   
    
    def test_playFirstHand(self):

        # Dealer not standing (sum == 0)
        gu.playFirstHand(self.dealer, self.player_Not_Busted, self.zero_deck)
        self.assertFalse(self.dealer.isStanding)

        # Dealer standing (if branch covered)
        gu.playFirstHand(self.dealer, self.player_Natural_Blackjack, self.zero_deck)
        self.assertTrue(self.dealer.isStanding)

if __name__ == '__main__':
    unittest.main()