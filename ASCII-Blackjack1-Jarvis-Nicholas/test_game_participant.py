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

    def test_newGame(self):
        participant = gp.GameParticipant()

        # Make sure everything is reset
        participant.newGame()
        self.assertFalse(participant.hand)
        self.assertEquals(participant.sum, 0)
        self.assertFalse(participant.isStanding)
        self.assertEquals(participant.aceCount, 0)
        self.assertEquals(participant.alternateAceSum, 0)

    def test_aceCombos(self):
        participant = gp.GameParticipant()

        # Ace count 1 Alt
        participant.aceCount = 1
        participant.aceCombos()
        self.assertEqual(participant.alternateAceSum, 11)

        # Ace count > 1 Alt
        participant.aceCount = 2
        participant.aceCombos()
        self.assertEqual(participant.alternateAceSum, 12)

        # "sum" should always be less than the alternate
        self.assertLess(participant.sum, participant.alternateAceSum)

    def test_determineSum(self):
        participant = gp.GameParticipant()
        ace_card = "Ace of clubs"
        jack_card = "Jack of clubs"
        queen_card = "Queen of clubs"
        king_card = "King of clubs"
        number_card = "5 of clubs"

        # Ace 
        old_ace_count = participant.aceCount
        participant.determineSum(ace_card)
        self.assertEqual(old_ace_count + 1, participant.aceCount)

        # Alt ace sum taking over sum (11 ace winner)
        participant.determineSum(jack_card)
        self.assertEqual(21, participant.sum)

        # Face cards
        old_sum_count = participant.sum
        participant.determineSum(queen_card)
        self.assertEqual(old_sum_count + 10, participant.sum)

        participant.determineSum(king_card) 
        self.assertEqual(old_sum_count + 20, participant.sum)

        # Number card
        participant.determineSum(number_card) 
        self.assertEqual(old_sum_count + 25, participant.sum)

    def test_hit(self):
        participant = gp.GameParticipant()
        card = "King of clubs"
        empty_length = len(participant.hand)

        # See if card is added
        participant.hit(card)
        self.assertEqual(empty_length + 1, len(participant.hand))
        self.assertEqual(card, participant.hand[len(participant.hand) - 1])

    def test_stand(self):
        participant = gp.GameParticipant()

        # Alt sum test
        participant.sum = 5
        participant.alternateAceSum = 17
        participant.stand()
        self.assertEqual(participant.sum, participant.alternateAceSum)

        # Standing test (core feature)
        self.assertTrue(participant.isStanding)

    def test_isBusted(self):
        participant = gp.GameParticipant()

        # No bust
        participant.sum = 2
        self.assertFalse(participant.isBusted())

        # Bust
        participant.sum = 30
        self.assertTrue(participant.isBusted())

if __name__ == '__main__':
    unittest.main()