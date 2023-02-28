"""
Author: Nicholas Jarvis
Date: 1/30/2023
Purpose: Python Blackjack
"""
# Command line executables:
# python3 -m coverage run test_game_participant.py -v -b
# python3 -m coverage report 

import unittest
import game_participant as gp

class testGameParticipant(unittest.TestCase):


    def setUp(self):
        self.participant = gp.GameParticipant()

    def test_newGame(self):

        # Make sure everything is reset
        self.participant.newGame()
        self.assertFalse(self.participant.hand)
        self.assertEquals(self.participant.sum, 0)
        self.assertFalse(self.participant.isStanding)
        self.assertEquals(self.participant.aceCount, 0)
        self.assertEquals(self.participant.alternateAceSum, 0)

    def test_aceCombos_alternate_sum_one(self):

        # Ace count 1 Alt
        self.participant.aceCount = 1
        self.participant.aceCombos()
        self.assertEqual(self.participant.alternateAceSum, 11)

    def test_aceCombos_alternate_sum_greater(self):

        # Ace count > 1 Alt
        self.participant.alternateAceSum = 11
        self.participant.aceCount = 2
        self.participant.aceCombos()
        self.assertEqual(self.participant.alternateAceSum, 12)

        # "sum" should always be less than the alternate
        self.assertLess(self.participant.sum, self.participant.alternateAceSum)

    def test_determineSum(self):
        ace_card = "Ace of clubs"
        jack_card = "Jack of clubs"
        queen_card = "Queen of clubs"
        king_card = "King of clubs"
        number_card = "5 of clubs"

        # Ace 
        old_ace_count = self.participant.aceCount
        self.participant.determineSum(ace_card)
        self.assertEqual(old_ace_count + 1, self.participant.aceCount)

        # Alt ace sum taking over sum (11 ace winner)
        self.participant.determineSum(jack_card)
        self.assertEqual(21, self.participant.sum)

        # Face cards
        old_sum_count = self.participant.sum
        self.participant.determineSum(queen_card)
        self.assertEqual(old_sum_count + 10, self.participant.sum)

        self.participant.determineSum(king_card) 
        self.assertEqual(old_sum_count + 20, self.participant.sum)

        # Number card
        self.participant.determineSum(number_card) 
        self.assertEqual(old_sum_count + 25, self.participant.sum)

    def test_hit(self):

        card = "King of clubs"
        empty_length = len(self.participant.hand)

        # See if card is added
        self.participant.hit(card)
        self.assertEqual(empty_length + 1, len(self.participant.hand))
        self.assertEqual(card, self.participant.hand[len(self.participant.hand) - 1])

    def test_stand(self):

        # Alt sum test
        self.participant.sum = 5
        self.participant.alternateAceSum = 17
        self.participant.stand()
        self.assertEqual(self.participant.sum, self.participant.alternateAceSum)

        # Standing test (core feature)
        self.assertTrue(self.participant.isStanding)

    def test_isBusted(self):

        # No bust
        self.participant.sum = 2
        self.assertFalse(self.participant.isBusted())

        # Bust
        self.participant.sum = 30
        self.assertTrue(self.participant.isBusted())

if __name__ == '__main__':
    unittest.main()